import glob
import numpy as N
import datetime

today = datetime.date.today()
print(today)

files = glob.glob("./csv/nied_*.csv")

f = open('meteo_nied.csv','w')
f.write('init,date,rain\n')

f.write('%s,%s,%.1f\n'%('today',today,0))
f.write('%s,%s,%.1f\n'%('today',today,30))

for file in files:

    print (file)
    
    date = N.genfromtxt(file,usecols=(0),delimiter=',',skip_header=4,dtype=str)
    rain = N.genfromtxt(file,usecols=(1),delimiter=',',skip_header=4,dtype=float)

    rain = N.cumsum(rain)

    nd = len(date)
    
    for d in range(nd):
    
        f.write('%s,%s,%.1f\n'%(file[6:16],date[d],rain[d]))

f.close()

    
     