import numpy as N
import pylab as P
#import Image,ImageFont,ImageDraw,ImageOps

file = '/home/peterh/daily/03987.dat'

jj=N.genfromtxt(file,usecols=(2),skip_header=1,dtype='i')
mm=N.genfromtxt(file,usecols=(1),skip_header=1,dtype='i')
dd=N.genfromtxt(file,usecols=(0),skip_header=1,dtype='i')
tn=N.genfromtxt(file,usecols=(3),skip_header=1,dtype='f')	
tg=N.genfromtxt(file,usecols=(4),skip_header=1,dtype='f')
tx=N.genfromtxt(file,usecols=(5),skip_header=1,dtype='f')
sd=N.genfromtxt(file,usecols=(8),skip_header=1,dtype='f')
ld=N.genfromtxt(file,usecols=(11),skip_header=1,dtype='f')
rf=N.genfromtxt(file,usecols=(12),skip_header=1,dtype='f')
rr=N.genfromtxt(file,usecols=(13),skip_header=1,dtype='i')

nd = len(jj)

f = open('03987_day.csv','w')
f.write('date,tmin,tmit,tmax,relf,sonn,ludr,nied\n')

for d in range(nd):

    if((jj[d]>=1961)&(tg[d]>-900)):

       f.write('%04i-%02i-%02i,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f\n'%(jj[d],mm[d],dd[d],tn[d],tg[d],tx[d],rf[d],sd[d],ld[d],rr[d]))

f.close()


'''
f=open('potsdam_day.html','w')

f.write('<!doctype html>\n')
f.write('<html>\n')
f.write('<head>\n')

f.write('<meta charset="utf-8">\n')   
f.write('<title>Tourismus</title>\n')
f.write('<link href="http://mottie.github.io/tablesorter/css/theme.default.css" rel="stylesheet">\n')

f.write('<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n') 
f.write('<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.9.1/jquery.tablesorter.min.js"></script>\n')

f.write('<script>\n')
#f.write('$(function(){$("#myDummyTable").tablesorter({widgets: ["zebra"]});});\n')
f.write('$(function(){\n')
f.write('$("#myDummyTable").tablesorter({widgets: ["zebra"]});\n')
f.write('});\n')

f.write('</script>\n')

f.write('<table id="myDummyTable" class="tablesorter" border="0" cellpadding="0" cellspacing="1">\n')
#f.write('<table align="left" border="1">\n')
f.write('<thead>\n')
f.write('<tr>\n')
f.write('<th>Jahr</th>\n')
f.write('<th>Monat</th>\n')
f.write('<th>Tag</th>\n')
f.write('<th>tmit [&ordm;C]</th>\n')
f.write('<th>tmax [&ordm;C]</th>\n')
f.write('<th>nied [mm]</th>\n')
f.write('</tr>\n')
f.write('</thead>\n')

f.write('<tbody>\n')

for d in range(nd):

    if(tg[d]>-100.):


        if((mm[d]==1)|(mm[d]==2)|(mm[d]==12)):       

            f.write('<tr>')
            f.write('<td align="right"><font color="blue"> %i</td>'%(jj[d]))
            f.write('<td align="right"><font color="blue"> %i</td>'%(mm[d]))
            f.write('<td align="right"><font color="blue"> %i</td>'%(dd[d]))
            f.write('<td align="right"><font color="blue"> %6.1f</td>'%(tg[d]))
            f.write('<td align="right"><font color="blue"> %6.1f</td>'%(tx[d]))
            f.write('<td align="right"><font color="blue"> %6i</td>'%(rr[d]))
            f.write('</tr>\n')
            
        if((mm[d]==3)|(mm[d]==4)|(mm[d]==5)):

            f.write('<tr>')
            f.write('<td align="right"><font color="green"> %i</td>'%(jj[d]))
            f.write('<td align="right"><font color="green"> %i</td>'%(mm[d]))
            f.write('<td align="right"><font color="green"> %i</td>'%(dd[d]))
            f.write('<td align="right"><font color="green"> %6.1f</td>'%(tg[d]))
            f.write('<td align="right"><font color="green"> %6.1f</td>'%(tx[d]))
            f.write('<td align="right"><font color="green"> %6i</td>'%(rr[d]))
            f.write('</tr>\n')
            
        if((mm[d]==6)|(mm[d]==7)|(mm[d]==8)):

            f.write('<tr>')
            f.write('<td align="right"><font color="red"> %i</td>'%(jj[d]))
            f.write('<td align="right"><font color="red"> %i</td>'%(mm[d]))
            f.write('<td align="right"><font color="red"> %i</td>'%(dd[d]))
            f.write('<td align="right"><font color="red"> %6.1f</td>'%(tg[d]))
            f.write('<td align="right"><font color="red"> %6.1f</td>'%(tx[d]))
            f.write('<td align="right"><font color="red"> %6i</td>'%(rr[d]))
            f.write('</tr>\n')            

        if((mm[d]==9)|(mm[d]==10)|(mm[d]==11)):

            f.write('<tr>')
            f.write('<td align="right"><font color="orange"> %i</td>'%(jj[d]))
            f.write('<td align="right"><font color="orange"> %i</td>'%(mm[d]))
            f.write('<td align="right"><font color="orange"> %i</td>'%(dd[d]))
            f.write('<td align="right"><font color="orange"> %6.1f</td>'%(tg[d]))
            f.write('<td align="right"><font color="orange"> %6.1f</td>'%(tx[d]))
            f.write('<td align="right"><font color="orange"> %6i</td>'%(rr[d]))
            f.write('</tr>\n')

f.write('</tbody>\n')              
f.write('</table>\n')

f.write('</html>\n')

f.close()
'''