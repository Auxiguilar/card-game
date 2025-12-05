import unittest
from src.cards.card_class import Card


class TestCardClass(unittest.TestCase):
    def test_str(self):
        card: Card = Card('ace', 'spades')
        self.assertEqual(str(card), 'Ace of Spades')

    def test_value(self):
        ranks: list[str] = [
            'ace',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
            'jack',
            'queen',
            'king'
            ]

        for i in range(len(ranks)):
            card: Card = Card(ranks[i], 'hearts')
            self.assertEqual(card.value, i+1)
