#!/bin/bash

sbatch --qos=short --account=cordex --nodes=1 --ntasks=1 ./rcms.sh
#sbatch --qos=short --account=cordex --nodes=1 --ntasks=1 --mem=10GB ./rcms.sh

