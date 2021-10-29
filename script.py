import os
import re
files = os.listdir('genproductions/bin/MadGraph5_aMCatNLO/')
#Zjj_cHbox_QU_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz
p = re.compile('Zjj_(\w+_[QULI]+)_.*.tar.xz')
gridpacks = list(map(lambda k: k[0], list(filter(lambda k: len(k)!=0 ,list(map(lambda k: re.findall(p, k), files))))))
print(gridpacks) 
