import unittest
from src.card import Card
from src.card_game import CardGame

CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1= Card("Hearts",1)
        self.card2= Card("Diamonds", 6)
        
        self.cards=[self.card1, self.card2]
        
    
    def test_check_for_ace(self):
        self.assertTrue(CardGame.check_for_ace(self, self.card1))
        
    
    def test_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2)) 
        
    def test_cards_total(self):
        self.assertEqual("You have a total of 7", CardGame.cards_total(self, self.cards))      

        