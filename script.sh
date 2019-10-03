#!/usr/bin/env bash

DI=1

for i in {2..100}; do
    echo "$DI, $i" >> results.txt
    python grid.py 1 $i >> results.txt
done