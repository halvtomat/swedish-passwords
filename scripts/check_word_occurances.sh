#!/bin/bash

# LEGACY

for word in $(cat $1); do
		occurances=$(grep -F $word $2 | awk '{sum+=$1} END{printf "%d",sum}')
		if [ "$occurances" -ne "0" ]; then
			echo -e $occurances"\t\t"$word
		fi
done

