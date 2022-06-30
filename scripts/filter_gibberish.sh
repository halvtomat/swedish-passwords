#!/bin/bash

# Input --> 1. Pattern list with gibberish patterns to remove. 2. Word list which to filter. 
# Output --> Filtered word list.

cp $2 ___TEMP
for pattern in $(cat $1); do
	grep -avxE $pattern ___TEMP > ___TEMP2
	mv ___TEMP2 ___TEMP
done
cat ___TEMP
rm ___TEMP
