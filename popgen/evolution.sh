echo -e $2'\t'generation $1
cat data.mutant | ./evolution.py $1 >> data.evolution.$2
