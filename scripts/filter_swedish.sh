#!/bin/bash

# Input --> Credential list with emails and passwords
# Output --> Credential list with emails and passwords of Swedish users

grep -aE ".*@.*\.(se|nu):.*" $1
