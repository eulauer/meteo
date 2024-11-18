#!/bin/bash

for par in tas pr

do

his="/p/projects/optagramm/data/climate/RCM/germany/bias_adjusted/isimip3basd/EUR-11/netCDF/CLMcom/MOHC-HadGEM2-ES/historical/r1i1p1/CLMcom-CCLM4-8-17/v1/day/"${par}"/*.nc"
rcp="/p/projects/optagramm/data/climate/RCM/germany/bias_adjusted/isimip3basd/EUR-11/netCDF/CLMcom/MOHC-HadGEM2-ES/rcp85/r1i1p1/CLMcom-CCLM4-8-17/v1/day/"${par}"/*.nc"

cdo -O -mergetime ${his} ${rcp} rcms.nc

if [ ${par} == "tas" ]
then

cdo -O -outputtab,date,value -expr,"tas=tas-273.14" -remapnn,lon=13.06_lat=52.39 rcms.nc > rcms_tas.csv

else

cdo -O -outputtab,date,value -expr,"pr=pr*86400." -remapnn,lon=13.06_lat=52.39 rcms.nc > rcms_pr.csv

fi

rm rcms.nc

done
