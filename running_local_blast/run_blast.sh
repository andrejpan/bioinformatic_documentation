#!/bin/bash

# $1 - first argument: full database path
# $2 - second argument: full path to separate fasta files

if [ "$#" -ne 2 ]; then
   echo "Illegal number of parameters"
   echo "Please call: $0 full_path_to_blast_database full_path_to_separate_fasta_files_directory"
   exit 1
fi

FILES=$2/*
for f in $FILES
do
  blastp -db $1 -query $f -out "$f.out"
  echo "Done with $f"
done
