import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.high_value_card = Card(1, 10)
        self.low_value_card = Card(1, 2)
        self.ace_card = Card(2, 1)
        self.game = CardGame()


    def test_check_ace_equals_ace(self):
        card_is_ace = self.game.check_for_ace(self.ace_card)
        self.assertEqual(True, card_is_ace)


    def test_check_ace_equals_no_ace(self):
        card_is_ace = self.game.check_for_ace(self.low_value_card)
        self.assertEqual(False, card_is_ace)

    def test_check_highest_card__True(self):
        returned_card = self.game.highest_card(self.high_value_card, self.low_value_card)
        self.assertEqual(10, returned_card.value)

    def test_check_highest_card__False(self):
        returned_card = self.game.highest_card(self.low_value_card, self.high_value_card)
        self.assertEqual(10, returned_card.value)

    def test_check_total_cards_pass(self):
        list_of_cards = [self.low_value_card, self.high_value_card]
        total_of_all_cards = self.game.cards_total(list_of_cards)
        self.assertEqual("You have a total of 12", total_of_all_cards)

    def test_check_total_cards_fails(self):
        list_of_cards = [self.low_value_card, self.high_value_card]
        total_of_all_cards = self.game.cards_total(list_of_cards)
        self.assertNotEqual("You have a total of 10", total_of_all_cards)




