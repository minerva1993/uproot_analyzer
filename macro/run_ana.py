import uproot, uproot_methods
import matplotlib.pyplot as plt
import mplhep as hep
import os, sys, multiprocessing
import argparse, psutil

from analysis_helper import *
from datasets import *
import numpy as np
#from histos import *
#from systematic import *

parser = argparse.ArgumentParser(description='Options for analyzer')
parser.add_argument('--year', '-Y', action='store', type=int, default=2017, help='Set year')
options = parser.parse_args()

plt.style.use(hep.style.CMS)
process = psutil.Process(os.getpid())

year = options.year
rootDir = {2017:'/data/users/minerva1993/ntuple/V9_6/200101/production',
           2018:'/data/users/minerva1993/ntuple/V10_3/200101/production'}
outDir = '../output/' + str(year)

list_to_process = dataset(year)

syst1 = ['','jecup','jecdown','jerup','jerdown']
syst2 = ['TuneCP5up','TuneCP5down','hdampup','hdampdown'] #external sample

#Create list of tuple (folder_to_process, syst_ext)
list_args = []
for d_tmp in list_to_process:
  if d_tmp != "TT_powheg_ttbb": continue

  for s_tmp in syst1 + syst2:
    if s_tmp != "jecup": continue
    list_args.append((d_tmp, s_tmp, len(get_file_list(rootDir[year], d_tmp))))

def run_ana(tuple_args):
  print 'processing... ' + str(tuple_args)
  folder_to_process = tuple_args[0]
  folder_to_process = folder_to_process.replace('_','')
  syst_ext = tuple_args[1]

  isData = False
  if 'Run201' in folder_to_process: isData = True

  #Deal with JER/C, Hdamp, Tune systematics
  loc_str = os.path.join(rootDir[year], folder_to_process)
  if ('Run201' in loc_str) and syst_ext != '': return
  elif (syst_ext in syst2) and not (syst_ext in loc_str): return
  elif (syst_ext in syst1) and any(tmp in loc_str for tmp in syst2): return

  if syst_ext == "": postfix = ""
  else:              postfix = "__"

  #JER/C treatment
  jerc_str = ''; met_idx = '';
  if syst_ext == 'jecup':
    jerc_str = 'jet_JES_Up'
    met_idx  = 0
  elif syst_ext == 'jecdown':
    jerc_str = 'jet_JES_Down'
    met_idx  = 1
  elif syst_ext == 'jerup':
    jerc_str = 'jet_JER_Up'
    met_idx  = 2
  elif syst_ext == 'jerdown':
    jerc_str = 'jet_JER_Down'
    met_idx  = 3
  elif not isData:
    jerc_str = 'jet_JER_Nom'

  #d = uproot.lazyarrays([os.path.join(rootDir[year], tuple_args[0]) + '/*'], 'fcncLepJets/tree')
  d = uproot.lazyarrays([os.path.join(rootDir[year], tuple_args[0]) + '/*000*'], 'fcncLepJets/tree')

  #One should define additional column beforehand
  tmp_pv = np.empty(len(d)); tmp_pv.fill(wrongPVRate(folder_to_process, year))
  tmp_wg = np.empty(len(d)); tmp_wg.fill(1.0)
  d['wrongPVrate']  = tmp_pv
  d['EventWeight']  = tmp_wg

  if 'jec' in syst_ext:
    d['jet_pt_jerc'] = d['jet_pt'] * (d['jet_JER_Nom'] * d[jerc_str])
  else:
    d['jet_pt_jerc'] = d['jet_pt'] * d[jerc_str]

  jet_pt = d['jet_pt_jerc']
  jet_eta = abs(d['jet_eta'])
  d['njet']  = np.logical_and(d['jet_pt_jerc'] > 30, abs(d['jet_eta']) < 2.4).sum()
  d['nbjet'] = np.logical_and(np.logical_and(d['jet_pt_jerc'] > 30, abs(d['jet_eta']) < 2.4),\
                                             d['jet_deepCSV'] > float(b_tagging(year))).sum()

  if any(i in syst_ext for i in ['jec','jer']):
    d['met_pt_jerc']  = np.sqrt(d['MET_unc_x'][:,met_idx]**2 + d['MET_unc_y'][:,met_idx]**2)
    d['met_phi_jerc'] = np.arctan2(d['MET_unc_x'][:,met_idx], d['MET_unc_y'][:,met_idx])
  else: d['met_pt_jerc'] = d['MET'] 

  lepton = uproot_methods.TLorentzVectorArray.from_ptetaphie(d['lepton_pt'], d['lepton_eta'], d['lepton_phi'], d['lepton_e'])
  met = uproot_methods.TLorentzVectorArray.from_ptetaphim(d['met_pt_jerc'], 0, d['met_phi_jerc'], 0)
  d['lepDphi'] = lepton.delta_phi(met)


  #Define cut steps
  d = d[np.logical_or(\
        np.logical_and(np.logical_and(d['channel'] == 0, d['lepton_pt'] > 30), abs(d['lepton_eta']) < 2.4),\
        np.logical_and(np.logical_and(d['channel'] == 1, d['lepton_pt'] > 30), abs(d['lepton_eta']) < 2.4))]

  cuts = collections.OrderedDict()
  cuts['0'] = d
  cuts['1'] = d[d['njet'] == 3]
  cuts['2'] = d[np.logical_and(d['njet'] == 3, d['nbjet'] == 2)]
  cuts['3'] = d[np.logical_and(d['njet'] == 3, d['nbjet'] == 3)]
  cuts['4'] = d[np.logical_and(d['njet'] >= 3, d['nbjet'] >= 2)]
  cuts['5'] = d[d['njet'] >= 4]
  cuts['6'] = d[np.logical_and(d['njet'] >= 4, d['nbjet'] == 2)]
  cuts['7'] = d[np.logical_and(d['njet'] >= 4, d['nbjet'] == 3)]
  cuts['8'] = d[np.logical_and(d['njet'] >= 4, d['nbjet'] == 4)]

  for step, cut_d in cuts.items():
    print step, len(cut_d)



if __name__ == '__main__':
  pool = multiprocessing.Pool(1)
  pool.map(run_ana, list_args)
  pool.close()
  pool.join()

print(process.memory_info()[0]/(1024.0*1024)) #rss only
print(process.cpu_times())
