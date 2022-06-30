#!/bin/bash

# LEGACY

total_occurances=0
for password in $(cat $1); do
		temp=$(grep -E " $password\$" $2 | awk '{print $1}')
		echo $temp
		((total_occurances+=temp))
done
echo $total_occurances

