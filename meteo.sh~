#!/bin/sh

cd $HOME/sueringwarte/meteo/


for d in 15 16 17

do

date=$(date -d "${d}"" day ago" '+%Y-%m-%d')

rm ./csv/${date}.csv

done

x=13.4
y=52.5

date=$(date '+%Y-%m-%d')

para='rain_sum'
#para='temperature_2m_max'

echo ${date}

curl -H "Accept: application/json" -o ./csv/${date}.csv -X GET "https://api.open-meteo.com/v1/forecast?latitude="${y}"&longitude="${x}"&daily=${para}&forecast_days=14&models=gfs_global&format=csv"

python meteo.py

git add -A
git commit -m 'Added my project'
git push -u -f origin main

scp meteo.html peterh@se06:/home/peterh/www/sueringwarte/

python potsdam_day.py