import os
import re
from shutil import copyfile
files = os.listdir('restrict_cards/v3_0')



p = re.compile('restrict_[a-zA-Z0-9]+_massless.dat')

#list(filt

a = list(filter(lambda k: len(k)!=0, list(map(lambda k: re.findall(p, k),files))))
for file in a:
	copyfile('restrict_cards/v3_0/'+file[0], 'restrict/'+file[0])
	print('copiato il file ', file[0])
#print(a)
