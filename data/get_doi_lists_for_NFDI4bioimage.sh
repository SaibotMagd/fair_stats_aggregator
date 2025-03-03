#!/bin/bash

# Array of arguments
declare -a arguments=(
    "i96578850 lin.txt"
    "i44260953 hhu.txt"
    "i4387155373 gerbi.txt"
    "i170658231 u-osnabrueck.txt"
    "i189712700 u-konstanz.txt"
    "i17937529 dkfz.txt"
    "i4210138560 embl.txt"
    "i4210162077 leibniz-hki.txt"
    "i78650965 tud.txt"
    "i22465464 u-muenster.txt"
    "i161046081 alu-fr.txt"
)

# Loop through the array and execute the command
for args in "${arguments[@]}"; do
    python get_dois_from_openalex_id.py $args
done

