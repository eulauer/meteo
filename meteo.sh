#!/bin/sh

cd $HOME/sueringwarte/meteo/


for d in 15

do

date=$(date -d "${d}"" day ago" '+%Y-%m-%d')

rm ./csv/nied_${date}.csv
rm ./csv/tmax_${date}.csv

done

x=13.4
y=52.5

date=$(date '+%Y-%m-%d')

para='precipitation_sum'
#para='temperature_2m_max'

echo ${date}

curl -H "Accept: application/json" -o ./csv/nied_${date}.csv -X GET "https://api.open-meteo.com/v1/forecast?latitude="${y}"&longitude="${x}"&daily=${para}&forecast_days=14&models=gfs_global&format=csv"

para='temperature_2m_max'

curl -H "Accept: application/json" -o ./csv/tmax_${date}.csv -X GET "https://api.open-meteo.com/v1/forecast?latitude="${y}"&longitude="${x}"&daily=${para}&forecast_days=14&models=gfs_global&format=csv"

python meteo.py

git add -A
git commit -m 'Added my project'
git push -u -f origin main

scp meteo_nied.html peterh@se06:/home/peterh/www/sueringwarte/
scp meteo_tmax.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_day.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_gwl.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_dis.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_dia.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_doy.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_box.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_ind.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_aus.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_tcum.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_rcum.html peterh@se06:/home/peterh/www/sueringwarte/
scp potsdam_pcum.html peterh@se06:/home/peterh/www/sueringwarte/

scp ./rcms/potsdam_rcum.html peterh@se06:/home/peterh/www/sueringwarte/rcms/
scp ./rcms/potsdam_tcum.html peterh@se06:/home/peterh/www/sueringwarte/rcms/

scp readme.md peterh@se06:/home/peterh/www/sueringwarte/

python potsdam_day.py
python potsdam_year.py