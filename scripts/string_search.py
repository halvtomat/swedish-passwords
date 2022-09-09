#!/usr/bin/python3

# INPUT: file1 = wordlist of words to search for, file2 = passwords
# OUTPUT: passwords with the words found in them 

import sys
import ahocorasick

def print_words(key, words):
	print(key, end=' : ')
	for word in words:
		print(word[1], end=', ')	
	print()

def print_word(key, found):
	print(key, ':', found)

def main():
	total_passwords = 0
	found_word = 0

	automaton = ahocorasick.Automaton()

	# Build automaton
	with open(sys.argv[1], encoding='utf-8', errors='ignore') as file1:
		for key in file1.read().splitlines():
			automaton.add_word(key.lower(), key.lower())
	automaton.make_automaton()

	# Search passwords
	with open(sys.argv[2], encoding='utf-8', errors='ignore') as file2:
		if '-match' in sys.argv:
			for key in file2.read().splitlines():
				total_passwords += 1
				found = automaton.match(key.lower())
				if found:
					found_word += 1
				if '-v' in sys.argv:
					print_word(key, found)
				if '-not_found' in sys.argv and not found:
					print_word(key, False)
			print(found_word, "/", total_passwords, " includes words", sep='')
			print(found_word/total_passwords*100, "%", sep='')
		elif '-count' in sys.argv:
			counts = {}
			for key in file2.read().splitlines():
				key = key.lower()
				words = list(automaton.iter_long(key))
				for word in words:
					word = word[1]
					counts[word] = counts.get(word, 0) + 1
			for word in counts:
				print(counts.get(word), "\t", word)
		else:
			for key in file2.read().splitlines():
				words = list(automaton.iter_long(key.lower()))
				total_passwords += 1
				if len(words) != 0:
					found_word += 1
				if '-v' in sys.argv:
					print_words(key, words)
				if '-not_found' in sys.argv and len(words) == 0:
					print_words(key, words)
				if '-found' in sys.argv and len(words) > 0:
					print_words(key, words)
			print(found_word, "/", total_passwords, " includes words", sep='')
			print(found_word/total_passwords*100, "%", sep='')


if __name__ == "__main__":
	main()