#!/bin/bash

# Input --> Word list, one word per line.
# Output --> Average length of words. (Number)

total_length=0
num_passwords=$(wc -l < $1)
for password in $(cat $1); do
		let "total_length+=${#password}"
done
bc -l <<< "$total_length/$num_passwords"

