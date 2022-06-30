#!/bin/bash

# Input --> Two word lists with one word per line.
# Output --> List of words from word list 1 which exist in word list 2.

for password in $(cat $1); do
	if grep -qax $password $2; then
		echo $password
	fi
done

