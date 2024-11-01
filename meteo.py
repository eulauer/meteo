import glob
import numpy as N

files = glob.glob("./csv/*.csv")

f = open('meteo.csv','w')
f.write('init,date,rain\n')

for file in files:

    print (file)
    
    date = N.genfromtxt(file,usecols=(0),delimiter=',',skip_header=4,dtype=str)
    rain = N.genfromtxt(file,usecols=(1),delimiter=',',skip_header=4,dtype=float)

    rain = N.cumsum(rain)

    nd = len(date)
    
    for d in range(nd):
    
        f.write('%s,%s,%.1f\n'%(file[6:16],date[d],rain[d]))

f.close()

    
     