#!/bin/bash

# Array of arguments
declare -a arguments=(
    "lin.txt"
    "gerbi.txt"
    "u-osnabrueck.txt"
    "u-konstanz.txt"
    "dkfz.txt"
    "embl.txt"
    "leibniz-hki.txt"
    "tud.txt"
    "u-muenster.txt"
    "alu-fr.txt"
    "hhu.txt"
)

# Loop through the array and execute the command
for args in "${arguments[@]}"; do
    python fair_stats_agg.py --renew 0 --doi-filelist ./data/$args
done



