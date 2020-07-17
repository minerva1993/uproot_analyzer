import os, sys

def dataset(year):
  list_to_process = []

  if year == 2016:
    list_to_process.extend([
    ])

  elif year == 2017:
    list_to_process.extend([
      "SingleElectron_Run2017B",
      "SingleElectron_Run2017C",
      "SingleElectron_Run2017D",
      "SingleElectron_Run2017E",
      "SingleElectron_Run2017F",
      "SingleMuon_Run2017B",
      "SingleMuon_Run2017C",
      "SingleMuon_Run2017D",
      "SingleMuon_Run2017E",
      "SingleMuon_Run2017F",
      "WJetsToLNu_part2",
    ])

  elif year == 2018:
    list_to_process.extend([
    ])

  #Signals
  list_to_process.extend([
    "ST_TH_1L3B_Hct",
    "ST_TH_1L3B_Hut",
    "TT_TH_1L3B_aTLep_Hct",
    "TT_TH_1L3B_aTLep_Hut",
    "TT_TH_1L3B_TLep_Hct",
    "TT_TH_1L3B_TLep_Hut",
  ])


  list_to_process.extend([
    "TT_powheg_ttbb",
    "TT_powheg_ttbb_hdampdown",
    "TT_powheg_ttbb_hdampup",
    "TT_powheg_ttbb_TuneCP5down",
    "TT_powheg_ttbb_TuneCP5up",
    "TT_powheg_ttcc",
    "TT_powheg_ttcc_hdampdown",
    "TT_powheg_ttcc_hdampup",
    "TT_powheg_ttcc_TuneCP5down",
    "TT_powheg_ttcc_TuneCP5up",
    "TT_powheg_ttlf",
    "TT_powheg_ttlf_hdampdown",
    "TT_powheg_ttlf_hdampup",
    "TT_powheg_ttlf_TuneCP5down",
    "TT_powheg_ttlf_TuneCP5up",
    "TTLL_powheg_ttbb",
    "TTLL_powheg_ttbb_hdampdown",
    "TTLL_powheg_ttbb_hdampup",
    "TTLL_powheg_ttbb_TuneCP5down",
    "TTLL_powheg_ttbb_TuneCP5up",
    "TTLL_powheg_ttcc",
    "TTLL_powheg_ttcc_hdampdown",
    "TTLL_powheg_ttcc_hdampup",
    "TTLL_powheg_ttcc_TuneCP5down",
    "TTLL_powheg_ttcc_TuneCP5up",
    "TTLL_powheg_ttlf",
    "TTLL_powheg_ttlf_hdampdown",
    "TTLL_powheg_ttlf_hdampup",
    "TTLL_powheg_ttlf_TuneCP5down",
    "TTLL_powheg_ttlf_TuneCP5up",
    "TTHad_powheg_ttbb",
    "TTHad_powheg_ttbb_hdampdown",
    "TTHad_powheg_ttbb_hdampup",
    "TTHad_powheg_ttbb_TuneCP5down",
    "TTHad_powheg_ttbb_TuneCP5up",
    "TTHad_powheg_ttcc",
    "TTHad_powheg_ttcc_hdampdown",
    "TTHad_powheg_ttcc_hdampup",
    "TTHad_powheg_ttcc_TuneCP5down",
    "TTHad_powheg_ttcc_TuneCP5up",
    "TTHad_powheg_ttlf",
    "TTHad_powheg_ttlf_hdampdown",
    "TTHad_powheg_ttlf_hdampup",
    "TTHad_powheg_ttlf_TuneCP5down",
    "TTHad_powheg_ttlf_TuneCP5up",
    "DYJets",
    "DYJets_10to50",
    "SingleTbar_t",
    "SingleTbar_tW",
    "SingleTop_s",
    "SingleTop_t",
    "SingleTop_tW",
    "TTWJetsToLNu",
    "TTWJetsToQQ",
    "TTZToLLNuNu",
    "TTZToQQ",
    "ttHTobb",
    "ttHToNonbb",
    "W1JetsToLNu",
    "W2JetsToLNu",
    "W3JetsToLNu",
    "W4JetsToLNu",
    "WJetsToLNu",
    "WW",
    "WZ",
    "ZZ",
    "QCD_EM120to170",
    "QCD_EM15to20",
    "QCD_EM170to300",
    "QCD_EM20to30",
    "QCD_EM300toInf",
    "QCD_EM30to50",
    "QCD_EM50to80",
    "QCD_EM80to120",
    "QCD_Mu1000toInf",
    "QCD_Mu120to170",
    "QCD_Mu15to20",
    "QCD_Mu170to300",
    "QCD_Mu20to30",
    "QCD_Mu300to470",
    "QCD_Mu30to50",
    "QCD_Mu470to600",
    "QCD_Mu50to80",
    "QCD_Mu600to800",
    "QCD_Mu800to1000",
    "QCD_Mu80to120",
  ])

  return list_to_process
