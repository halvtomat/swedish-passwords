#!/bin/bash

# LEGACY

for password in $(cat $1); do
	grep -na $password $2
done

