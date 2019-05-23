import random

# Class that creates a single card
class Card:
    name = ''
    value = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return self.name


#A deck of 52 cards
deck = [Card('Ace of Hearts', 11), Card('Ace of Spades', 11), Card('Ace of Diamonds', 11), Card('Ace of Clubs', 11),
Card('2 of Hearts', 2), Card('3 of Hearts', 3), Card('4 of Hearts', 4), Card('5 of Hearts', 5), Card('6 of Hearts', 6), Card('7 of Hearts', 7), Card('8 of Hearts', 8), 
Card('9 of Hearts', 9), Card('10 of Hearts', 10), Card('Jack of Hearts', 10), Card('Queen of Hearts', 10), Card('King of Hearts', 10), Card('2 of Spades', 2),
Card('3 of Spades', 3), Card('4 of Spades', 4), Card('5 of Spades', 5), Card('6 of Spades', 6), Card('7 of Spades', 7), Card('8 of Spades', 8), 
Card('9 of Spades', 9), Card('10 of Spades', 10), Card('Jack of Spades', 10), Card('Queen of Spades', 10), Card('King of Spades', 10), Card('2 of Diamonds', 2),
Card('3 of Diamonds', 3), Card('4 of Diamonds', 4), Card('5 of Diamonds', 5), Card('6 of Diamonds', 6), Card('7 of Diamonds', 7), Card('8 of Diamonds', 8), 
Card('9 of Diamonds', 9), Card('10 of Diamonds', 10), Card('Jack of Diamonds', 10), Card('Queen of Diamonds', 10), Card('King of Diamonds', 10), Card('2 of Clubs', 2),
Card('3 of Clubs', 3), Card('4 of Clubs', 4), Card('5 of Clubs', 5), Card('6 of Clubs', 6), Card('7 of Clubs', 7), Card('8 of Clubs', 8), 
Card('9 of Clubs', 9), Card('10 of Clubs', 10), Card('Jack of Clubs', 10), Card('Queen of Clubs', 10), Card('King of Clubs', 10)]


#Draw a random card from the deck and remove it from the deck
def get_card(deck):
    myCard = random.choice(deck)
    deck.remove(myCard)
    return myCard

def scoreOfHand(hand):
    total = checkAce(hand)
    return total

def checkAce(hand):
    total = 0
    for card in hand:
        total += card.value
        if (total > 21 and ('Ace of Hearts' == str(hand[-1]) or 'Ace of Spades' == str(hand[-1]) or 'Ace of Clubs' == str(hand[-1]) or 'Ace of Diamonds' == str(hand[-1]))):
                total -= 10
    return total