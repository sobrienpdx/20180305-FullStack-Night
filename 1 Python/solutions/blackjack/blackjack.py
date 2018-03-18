# lab 19 - blackjack with using custom deck and card classes

from Deck import Card, Deck
from functools import reduce

valid_inputs = ['yes', 'no', 'y', 'n', 'hit', 'stay']

def get_card_value(card):
    """
    returns rank of card object
    """
    try:
        return(int(card.rank))
    except ValueError:
        if card.rank in 'JQK':
            return 10
        elif card.rank == 'A':
            return 1
    except AttributeError:
        if type(card) is int:
            return card


def get_points(user_hand):
    """
    user_hand is a list of card objects
    returns total point value of user_hand
    """
    if len(user_hand) == 1:
        return get_card_value(user_hand[0])
    else:
        return reduce(lambda left,right: get_card_value(left) + get_card_value(right), user_hand)


def advice(points):
    """
    Returns blackjack advice based on points in user_hand
    """
    if points < 17:
        return 'Hit'
    elif 17 <= points < 21:
        return 'Stay'
    elif points == 21:
        return 'Blackjack!'
    else:
        return 'Already Busted'
    return ''


if __name__ == '__main__':
    while True:              # loop game
        deck = Deck()        # initialize deck object
        deck.shuffle()       # shuffle deck

        user_hand = [deck.deal(), deck.deal()]   # initialize user hand as list with two cards drawn from the deck
        user_points = get_points(user_hand)           # get point value of cards in user's hand
        dealer_hand = [deck.deal(), deck.deal()]
        dealer_points = get_points(dealer_hand)

        while True: # loop while user chooses to hit
            print('-'*48)
            print("\nThe dealer's hand is: ")
            print("Card(rank='unknown', suit='unknown')")
            for card in range(1,len(dealer_hand)):
                print(dealer_hand[card])
            print(f"The dealer has at least {1 + get_points(dealer_hand[1:])}")

            print("\nYour hand is: ")
            for card in user_hand:
                print(card)
            print(user_points, advice(user_points))

            if user_points >= 21 or dealer_points >= 21: # game over
                break

            while True: # input validation
                hit = input("\nDo you want to hit? ").strip().lower()
                if hit in valid_inputs:
                    break

            if hit in ['yes', 'y', 'hit']:  # if user decides to hit
                user_hand.append(deck.deal())           # deal new card from deck into the user's hand
                user_points = get_points(user_hand)
                dealer_hand.append(deck.deal())         # deal new card to dealer's hand
                dealer_points = get_points(dealer_hand)
            elif hit in ['no', 'n', 'stay']:
                break

        # show dealer's full hand and print result
        print('-'*48)
        print("\nThe dealer's hand is: ")
        for card in dealer_hand:
            print(card)
        if user_points <= 21 and dealer_points < 21:
            if user_points > dealer_points:
                print("\nYou win!")
            elif user_points < dealer_points:
                print("\nYou lose!")
            else:
                print("\nTie!")
        elif dealer_points > 21 and user_points <= 21:
            print("\nYou win!")            
        else:
            print("\nYou lose")

        while True: # input validation
            play_ag = input("\nDo you want to play again? ").strip().lower()
            if play_ag in valid_inputs:
                break

        if play_ag in ['no', 'n']:
            break
            
