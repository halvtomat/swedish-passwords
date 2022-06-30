#!/usr/bin/python3.10

# Input --> Word list, one word per line
# Output --> Pattern list, one pattern per line

import sys
import string

def convert_char(c):
	if c in list(string.ascii_lowercase): return 'l'
	if c in list(string.ascii_uppercase): return 'u'
	if c in list(string.digits): return 'd'
	if c in list(string.punctuation): return 's'
	if c in ['å', 'ä', 'ö']: return 'ö'
	if c == '\n': return ''
	return '?'

def convert_password(pw):
	converted = []
	for c in pw:
		converted.append(convert_char(c))
	return ''.join(converted)

def main():
	for pw in sys.stdin:
		print(convert_password(pw))


if __name__ == "__main__":
	main()
