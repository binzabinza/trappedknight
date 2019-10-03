#!/usr/bin/env bash

MAX_DI=25
MAX_DJ=25

rm results.txt

printf "di\tdj\tstep\ttrap\tvalue\n" >> results.txt

for ((di=1; di<=$MAX_DI; di++)); do
    for ((dj=$di+1; dj<=$MAX_DJ; dj++)); do
	if [[ $1 == 'p' ]]; then
		printf "$di\t$dj\t" | tee -a results.txt
		python trappedknight.py $di $dj | tee -a results.txt
	else
		printf "$di\t$dj\t" >> results.txt
		python trappedknight.py $di $dj >> results.txt
	fi
    done
done