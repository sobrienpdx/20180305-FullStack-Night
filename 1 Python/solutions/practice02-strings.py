# Solutions to practice02-strings

"""
Problem 1
Get a string from the user, print out another string, doubling every letter.
"""
def double_letters(x):
	y = ''
	for char in x:
		y += char + char
	return y

double_letters('hello') #  # → hheelloo

"""
Problem 2
Write a function that takes a string, and returns a list of strings, each missing a different character.
"""
def missing_char(string):
	pass

missing_char('kitten') # → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

"""
Problem 3
Return the letter that appears the latest in the english alphabet.
"""
def latest_letter(string):
	pass

latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') # → v

"""
Problem 4
Write a function that returns the number of occurances of 'hi' in a given string.
"""
def count_hi(string):
	pass

count_hi('hihi') # → 2

"""
Problem 5
Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
"""
def cat_dog(string):
	pass

cat_dog('catdog') # → True
cat_dog('catcat') # → False
cat_dog('catdogcatdog') # → True

"""
Problem 6
Return the number of letter occurances in a string.
"""
def count_letter(letter, word):
    pass

count_letter('i', 'antidisestablishmentterianism') # → 5
count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') # → 2

"""
Problem 7
Convert input strings to lowercase without any surrounding whitespace.
"""
def lower_case(string):
	pass

lower_case("SUPER!") # → 'super!'
lower_case("        NANNANANANA BATMAN        ") # → 'nannananana batman'