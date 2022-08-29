#!/usr/bin/python3

# INPUT: file1 = wordlist of words to search for, file2 = passwords
# OUTPUT: passwords with the words found in them 

import ahocorasick
import sys

def print_words(key, words):
	print(key, end=' : ')
	for word in words:
		print(word[1], end=', ')	
	print()

def main():
	total_passwords = 0
	found_word = 0

	automaton = ahocorasick.Automaton()

	# Build automaton
	with open(sys.argv[1]) as file1:
		for key in file1.read().splitlines():
			automaton.add_word(key.lower(), key.lower())
	automaton.make_automaton()

	# Search passwords
	with open(sys.argv[2]) as file2:
		for key in file2.read().splitlines():
			words = list(automaton.iter(key.lower()))
			total_passwords += 1
			if len(words) != 0:
				found_word += 1
			if '-v' in sys.argv:
				print_words(key, words)
			if '-not_found' in sys.argv and len(words) == 0:
				print_words(key, words)


	print(found_word, "/", total_passwords, " includes words", sep='')
	print(found_word/total_passwords*100, "%", sep='')


if __name__ == "__main__":
	main()