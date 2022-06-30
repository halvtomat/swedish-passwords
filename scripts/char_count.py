#!/usr/bin/python3

# Input --> Word list, one word per line
# Output --> Character occurance list, each line is a character followed by the number of occurances of that character.

# If it complains about character encodings, run with "LC_ALL=C".

import sys

def main():
	blacklist = list(range(0,32)) + list(range(127,161))
	chars = [0] * 256
	for line in sys.stdin:
		for char in line:
			if(ord(char) < 256):
				chars[ord(char)] += 1
	for char, occurance in enumerate(chars):
		if char not in blacklist:
			print(chr(char), occurance)
	return 0

if __name__ == "__main__":
	main()
