#!/bin/bash

# Array of arguments
declare -a arguments=(
    "i96578850 ../data/lin.txt"
    "i4387155373 ../data/gerbi.txt"
    "i170658231 ../data/u-osnabrueck.txt"
    "i189712700 ../data/u-konstanz.txt"
    "i17937529 ../data/dkfz.txt"
    "i4210138560 ../data/embl.txt"
    "i4210162077 ../data/leibniz-hki.txt"
    "i78650965 ../data/tud.txt"
    "i22465464 ../data/u-muenster.txt"
    "i161046081 ../data/alu-fr.txt"
    "i44260953 ../data/hhu.txt"
)

# Loop through the array and execute the command
for args in "${arguments[@]}"; do
    python create_institute_doi_list.py $args
done



