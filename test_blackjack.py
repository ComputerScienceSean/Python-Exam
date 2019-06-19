import unittest
import Cards
import Blackjack


class BlackjackTest(unittest.TestCase):
    
    def test_checkAce(self):
        deck = Cards.deck
        playerHand = []
        playerHand.append(deck[0])
        playerHand.append(deck[1])
        self.assertEqual(12, Cards.checkAce(playerHand))

    def test_getCard(self):
        deck = Cards.deck
        Cards.get_card(deck)
        Cards.get_card(deck)
        Cards.get_card(deck)
        Cards.get_card(deck)
        self.assertEqual(len(deck), 48)

if __name__ == "__main__":
        unittest.main()


        
        