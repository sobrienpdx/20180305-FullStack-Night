# lab 17 - palindrome_anagram.py in class example

def check_anagram(first, second):
	""" Returns boolean if first and second are anagrams
	Set implementation doesn't work :(

	>>> check_anagram('racecar', 'aaccerr')
	True

	>>> check_anagram('aaab', 'baaa')
	True

	>>> check_anagram('bees', 'bee')
	False

	>>> check_anagram('bad', 'goo')
	False

	>>> check_anagram('bba', 'aab')
	False
	"""
	return clean_sort_string(first) == clean_sort_string(second)


def clean_sort_string(string):
	return sorted(list(string.lower().replace(' ', '')))


def check_palindrome(string):
	""" Returns boolean if string is a palindrome
	Stack implementation

	>>> check_palindrome('racecar')
	True

	>>> check_palindrome(112211)
	True

	>>> check_palindrome('bees')
	False
	"""
	if not type(string) is str:
		string = str(string)
	half_point = len(string)//2
	stack = [char for char in string[:half_point]]	
	if len(string)%2:  # if string is odd
		string = list(string[half_point+1:])
	else:  # string is even
		string = list(string[half_point:])
	while len(stack):
		if stack.pop() != string.pop(0):
			return False
	return True




if __name__ == '__main__':
	while True:
		while True:
			operation = input("Enter '(a)nagram' or '(p)alindrome' to check if your input is an anagram or palindrome, or 'e(x)it' to exit: ").strip().lower() 
			if operation in ['anagram', 'a', 'palindrome', 'p', 'exit', 'x']:
				break

		if operation in ['exit', 'x']:
			break
		else: 
			if operation in ['anagram', 'a']:
				first_phrase = input("Enter your first phrase: ")
				second_phrase = input("Enter your second phrase: ")
				if check_anagram(first_phrase, second_phrase):
					print(f'"{first_phrase}" is an anagram of "{second_phrase}"')
				else:
					print(f'"{first_phrase}" is not an anagram of "{second_phrase}"')
			elif operation in ['palindrome', 'p']:
				user_input = input("Enter the text you want to check: ")
				if check_anagram(user_input):
					print(f'"{user_input}" is a palindrome')
				else:
					print(f'"{user_input}" is not a palindrome')			


