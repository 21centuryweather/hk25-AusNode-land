#!/bin/bash
#PBS -q normal
#PBS -l ncpus=8
#PBS -l mem=32GB
#PBS -l walltime=01:00:00
#PBS -l storage=gdata/hh5+gdata/qx55+scratch/nf33
#PBS -l wd
#PBS -l jobfs=10GB
#PBS -P nf33

set -eu
module use /g/data/hh5/public/modules
module load conda/analysis3
source /scratch/nf33/public/hackathon_env/bin/activate

# run your code here!
