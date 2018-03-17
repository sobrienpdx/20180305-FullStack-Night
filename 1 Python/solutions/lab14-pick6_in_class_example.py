"""
In class solution to lab14-pick6
"""
import random 

payout = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

def pick6():
	"""
	returns a list of 6 random numbers
	"""
	return [random.randint(1,99) for i in range(6)]
	#### this is equivalent to the following: ####
	ticket = []
	for i in range(6):
		ticket.append(random.randint(1,99))
	return ticket


def num_matches(winning, ticket):
	"""
	returns the number of matches between the winning numbers and the ticket
	"""
	matches = 0
	for i in range(len(ticket)):
		if winning[i] == ticket[i]:
			matches += 1
	return matches


def return_on_investment(earnings):
	"""
	returns return on investment for 100000 x $2 tickets
	"""
	return (earnings - (2*100000))/earnings


def play_100000():
	winning_ticket = pick6()
	balance = 0
	winnings = 0

	for i in range(100000):
		ticket = pick6()
		balance -= 2
		matches = num_matches(winning_ticket, ticket)
		balance += payout[matches]
		winnings += payout[matches]

	if balance > 0:
		print(f"Your final balance is: {balance}")
		print(f"Your return on investment (ROI) is: {return_on_investment(winnings)}")


if __name__ == '__main__':
	for i in range(100):
		play_100000()