x=13.4
y=52.5

#x=12.5
#y=42.5


date=$(date '+%Y-%m-%d')
#date=$(date -d "1 day ago" '+%Y-%m-%d')

para='rain_sum'
#para='temperature_2m_max'

echo ${date}

curl -H "Accept: application/json" -o ./csv/${date}.csv -X GET "https://api.open-meteo.com/v1/forecast?latitude="${y}"&longitude="${x}"&daily=${para}&forecast_days=14&models=gfs_global&format=csv"
#curl -H "Accept: application/json" -o ./json/${date}.json -X GET "https://api.open-meteo.com/v1/forecast?latitude="${y}"&longitude="${x}"&daily=rain_sum&forecast_days=14&models=gfs_global"
#https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&format=csv

python meteo.py

git add -A
git commit -m 'Added my project'
git push -u -f origin main

scp meteo.html peterh@se06:/home/peterh/www/sueringwarte/

#jq -s '.' ./json/*.json   > meteo.json

#https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=52.5&longitude=13.4&start_date=2024-10-14&end_date=2024-10-28&daily=rain_sum&models=gfs_global