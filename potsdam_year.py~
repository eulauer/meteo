import numpy as N

file = '/home/peterh/daily/03987.dat'
dat = N.genfromtxt(file,names=True,dtype=None)

jo = N.array(list(set(dat['jahr'])))

je = N.max(jo)-1

id = N.where((dat['jahr']>=1961)&(dat['jahr']<=je))[0]

ta = dat['ta'][id]
mo = dat['mo'][id]
ja = dat['jahr'][id]
tn = dat['tmin'][id]
tg = dat['tmit'][id]
tx = dat['tmax'][id]
pr = dat['nied'][id]
rf = dat['relf'][id]
so = dat['sonn'][id]
ld = dat['ludr'][id]

jo = N.arange(1961,je+1,1)

f = open('03987_year.csv','w')
f.write('date,tx00,tx01,tx25,tx30,tx99,pr30,pr99\n')

for j in jo:

    id = N.where(ja==j)[0]
    
    tx00 = N.where((ja==j)&(tx<=0))[0]
    tx01 = N.percentile(tx[id],1)
    tx25 = N.where((ja==j)&(tx>=25))[0]
    tx30 = N.where((ja==j)&(tx>=30))[0]
    tx99 = N.percentile(tx[id],99)  
    pr30 = N.where((ja==j)&(pr>=30))[0]
    pr99 = N.percentile(pr[id],99) 

    f.write('%i-01-01,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f\n'%(j,len(tx00),tx01,len(tx25),len(tx30),tx99,len(pr30),pr99))

f.close()