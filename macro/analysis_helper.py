import os, sys, collections

def get_file_list(rootDir, dataset):

  out = []
  tmp = os.listdir(os.path.join(rootDir, dataset))
  for i in tmp:
    if not i.endswith('.root'): continue
    out.append(os.path.join(rootDir,dataset,i))

  return out


def cut_flow():

  d = collections.OrderedDict()
  d['1'] = ' && njet_jerc == 3'
  d['2'] = ' && njet_jerc == 3 && nbjet_jerc == 2'
  d['3'] = ' && njet_jerc == 3 && nbjet_jerc == 3'
  d['4'] = ' && njet_jerc >= 3 && nbjet_jerc >= 2'
  d['5'] = ' && njet_jerc >= 4'
  d['6'] = ' && njet_jerc >= 4 && nbjet_jerc == 2'
  d['7'] = ' && njet_jerc >= 4 && nbjet_jerc == 3'
  d['8'] = ' && njet_jerc >= 4 && nbjet_jerc == 4'

  return d


def b_tagging(year):

  if year == 2017:
    bWP_M = 0.4941
    bWP_T = 0.8001
    cvsbWP_M = 0.28
    cvslWP_M = 0.15

  elif year == 2018:
    bWP_M = 0.4184
    bWP_T = 0.7527
    cvsbWP_M = 0.29
    cvslWP_M = 0.137

  else:
    bWP_M = 0.0
    bWP_T = 0.0
    cvsbWP_M = 0.0
    cvslWP_M = 0.0

  return str(bWP_M)    


def wrongPVRate(fileName, year):

  if int(year) == 2017:
    if   "DYJets10to50"            in fileName: wrongPVrate = 1.02921
    elif "QCDEM15to20"             in fileName: wrongPVrate = 1.01333
    elif "QCDEM20to30"             in fileName: wrongPVrate = 1.01227
    elif "QCDEM300toInf"           in fileName: wrongPVrate = 1.01194
    elif "QCDEM50to80"             in fileName: wrongPVrate = 1.02226
    elif "QCDMu120to170"           in fileName: wrongPVrate = 1.01289
    elif "QCDMu170to300"           in fileName: wrongPVrate = 1.01181
    elif "QCDMu20to30"             in fileName: wrongPVrate = 1.0253
    elif "QCDMu30to50"             in fileName: wrongPVrate = 1.02105
    elif "QCDMu470to600"           in fileName: wrongPVrate = 1.0141
    elif "QCDMu50to80"             in fileName: wrongPVrate = 1.01149
    elif "QCDMu80to120"            in fileName: wrongPVrate = 1.01278
    elif "TTLLpowhegttbbhdampup"   in fileName: wrongPVrate = 1.01807
    elif "TTLLpowhegttcchdampup"   in fileName: wrongPVrate = 1.01978
    elif "TTLLpowhegttlfhdampup"   in fileName: wrongPVrate = 1.01938
    elif "TTZToLLNuNu"             in fileName: wrongPVrate = 1.02425
    elif "TTpowhegttbbTuneCP5down" in fileName: wrongPVrate = 1.02715
    elif "TTpowhegttbbhdampdown"   in fileName: wrongPVrate = 1.02717
    elif "TTpowhegttccTuneCP5down" in fileName: wrongPVrate = 1.0273
    elif "TTpowhegttcchdampdown"   in fileName: wrongPVrate = 1.02746
    elif "TTpowhegttlfTuneCP5down" in fileName: wrongPVrate = 1.02742
    elif "TTpowhegttlfhdampdown"   in fileName: wrongPVrate = 1.02774
    elif "W3JetsToLNu"             in fileName: wrongPVrate = 1.02348
    elif "WW"                      in fileName: wrongPVrate = 1.0295
    elif "WZ"                      in fileName: wrongPVrate = 1.02298
    elif "ZZ"                      in fileName: wrongPVrate = 1.01508
    else: wrongPVrate = 1.0

  else: wrongPVrate = 1.0

  return float(wrongPVrate)
