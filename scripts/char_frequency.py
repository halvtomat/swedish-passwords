#!/usr/bin/python3

# Input --> Character occurance list, one character per line followed by the number of occurances of that character.
# Output --> The frequency of lowercase letters in a sorted list.

import sys

def main():
	total_chars = 0
	chars = {}
	whitelist = list(range(97,123))
	for line in sys.stdin:
		char = line[0]
		if not ord(char) in whitelist:
			continue
		occurances = int(line[2:])
		total_chars += occurances
		chars[char] = occurances
	sorted_chars = sorted(chars.items(), key=lambda x:x[1], reverse=True)
	for char in sorted_chars:
		print(char[0], char[1], str(round((char[1] / total_chars) * 100, 2)) + '%')
	return 0

if __name__ == "__main__":
	main()
