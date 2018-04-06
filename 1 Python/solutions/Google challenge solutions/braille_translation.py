"""
braille_translation.py

 Braille Translation
 Part of the Google secret interview process
===================

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency at the same time - increase your chances of a promotion. 

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".

Write a function answer(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.
"""

def int_to_bin(x):
	"""
	Converts integer to 6-bit binary string
	"""
	return str(bin(x)).split('b')[1].zfill(6)


def encode_braille(string):
	"""
	Returns 6-bit binary representation of the string translated to braille 
	"""
	ret = ''
	for char in string:
		if char.isupper():
			ret += eng_to_braille['cap']
			char = char.lower()
		ret += eng_to_braille[char]
	return ret


def split_braille(braille):
	"""
	Returns list of braille string split to 6-bit letters 
	"""
	return [braille[i:i+6] for i in range(0, len(braille), 6)]


def decode_braille(braille):
	"""
	Returns braille string translated to english
	"""
	braille = split_braille(braille)
	ret = ''
	upper = False
	for char in braille:
		if char == eng_to_braille['cap']:
			upper = True
			continue
		else:
			if upper:
				ret += braille_to_eng[char].upper()
				upper = False
			else:
				ret += braille_to_eng[char]
	return ret


# Hardcoded dict of english to braille translations, where key = char and value = 6-bit binary representation of braille
eng_to_braille = {
	'a': int_to_bin(32),
	'b': int_to_bin(48),
	'c': int_to_bin(36),
	'd': int_to_bin(38),
	'e': int_to_bin(34),
	'f': int_to_bin(52),
	'g': int_to_bin(54),
	'h': int_to_bin(50),
	'i': int_to_bin(20),
	'j': int_to_bin(22),
	'k': int_to_bin(40),
	'l': int_to_bin(56),
	'm': int_to_bin(44),
	'n': int_to_bin(46),
	'o': int_to_bin(42),
	'p': int_to_bin(60),
	'q': int_to_bin(62),
	'r': int_to_bin(58),
	's': int_to_bin(28),
	't': int_to_bin(30),
	'u': int_to_bin(41),
	'v': int_to_bin(57),
	'w': int_to_bin(23),
	'x': int_to_bin(45),
	'y': int_to_bin(47),
	'z': int_to_bin(43),
	' ': int_to_bin(0),
	'cap': int_to_bin(1)
}

# Hardcoded dict of braille to english translations, where key = 6-bit binary representation of braille and value = char
braille_to_eng = {v:k for k,v in eng_to_braille.items()}

if __name__ == '__main__':
	plaintext = "The quick brown fox jumps over the lazy dog"
	# Test encoding
	print(encode_braille(plaintext) == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")
	# Test decoding
	print(plaintext == decode_braille(encode_braille(plaintext)))