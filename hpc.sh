#!/bin/bash

#SBATCH -A dem-mate
#SBATCH --job-name=internal_friction
#SBATCH --time=04:00:00
#SBATCH --no-requeue
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 24
#SBATCH -o %j.out-%N
#SBATCH --mail-type=ALL
#SBATCH --mail-user=toth.janos@uni-mate.hu

module load singularity

echo "Job               = $SLURM_JOB_ID"
echo "Date              = $(date)"
echo "Hostname          = $(hostname -s)"
echo "Working Directory = $(pwd)"
echo ""
echo "Number of Nodes Allocated      = $SLURM_JOB_NUM_NODES"
echo "Number of Tasks Allocated      = $SLURM_NTASKS"
echo "Number of Cores/Task Allocated = $SLURM_CPUS_PER_TASK"

set -xe

singularity exec ../yadedaily.sif /usr/bin/yadedaily -j $SLURM_CPUS_PER_TASK -x -n batch.py

