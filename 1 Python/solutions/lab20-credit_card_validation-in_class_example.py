def credit_card_validation(card_number):
	card_number = card_number.split()
	print(card_number)
	for i in range(len(card_number)):
		card_number[i] = int(card_number[i])
	# card_number = [int(num) for num in card_number]
	check_digit = card_number.pop()
	print(card_number)
	card_number.reverse()
	print(card_number)
	for i in range(0,len(card_number),2):
		card_number[i] *= 2
	print(card_number)
	# card_number = [num*2 for num in card_number]
	for i in range(len(card_number)):
		if card_number[i] > 9:
			card_number[i] -= 9
	print(card_number)
	# card_number = [num-9 if num>9 else num for num in card_number ]
	sum_num = sum(card_number)
	print(sum_num)
	# second_digit = sum_num % 10
	second_digit = int(list(str(sum_num))[1])
	return second_digit == check_digit


if __name__ == '__main__':
	credit_card = input("Enter your credit card number: ")
	if (credit_card_validation(credit_card)):
		print("Valid number")
	else:
		print("Invalid number")

	# Test data
	print("Testing test case... Our validation function works: ")
	card_number = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
	print(credit_card_validation(card_number) == True)
	card_number = '1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2'
	print(credit_card_validation(card_number) == False)
