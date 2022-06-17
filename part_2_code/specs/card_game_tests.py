import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.Testcase):

    def setUp(self):
        value_of_card = Card(1, 2)
        ace_card = Card(2, 1)
        game = CardGame()


    def test_check_ace_equals_ace(self):
        game = CardGame(self.value_of_card)
        card_is_ace = game.check_for_ace(self.value_of_card)

        self.AssertEqual(True, card_is_ace)


