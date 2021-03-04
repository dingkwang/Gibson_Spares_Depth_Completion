#!/bin/bash
#SBATCH --job-name=SparseDepth_dk      # Job name
#SBATCH --mail-user=noplaxochia@ufl.edu
#SBATCH --mail-type=ALL         # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                  # Number of MPI tasks (i.e. processes)
#SBATCH --nodes=1                    # Maximum number of nodes to be allocated
#SBATCH --output=log_%j.log     # Path to the standard output and error files relative to the working directory
#SBATCH --qos=eel6935
#SBATCH --account=eel6935
#SBATCH --gpus=1
#SBATCH --mem=22gb
#SBATCH --time=0:02:00			# Time: hr:min:sec
#SBATCH --partition=gpu

echo "Date              = $(date)"
echo "Hostname          = $(hostname -s)"
echo "Working Directory = $(pwd)"
echo ""
echo "Number of Nodes Allocated      = $SLURM_JOB_NUM_NODES"
echo "Number of Tasks Allocated      = $SLURM_NTASKS"
echo "Number of Cores/Task Allocated = $SLURM_CPUS_PER_TASK"

ml pytorch/1.5.0
python3 creatVideo.py

