import unittest
from src.cards.card_class import Card


class TestCardClass(unittest.TestCase):
    def test_str(self):
        card: Card = Card('ace', 'spades')
        self.assertEqual(str(card), 'Ace of Spades')

        joker: Card = Card('joker')
        self.assertEqual(str(joker), 'Joker')

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

        card: Card = Card('joker')
        self.assertFalse(hasattr(card, 'value'))

    def test_comparison(self):
        cards: list[Card] = [
            Card('ace', 'spades'), Card('ten', 'clubs'),
            Card('king', 'hearts'), Card('king', 'diamonds'),
            Card('joker')
            ]

        self.assertLess(cards[0], cards[2])
        self.assertGreater(cards[2], cards[1])
        self.assertNotEqual(cards[3], cards[2])
        self.assertLessEqual(cards[1], cards[3])

        with self.assertRaises(TypeError): # I'm not sure what's going on here, but whatever
            jk: bool = cards[0] < cards[4]
