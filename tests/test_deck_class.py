import unittest
from src.cards.deck_class import Deck


class TestDeckClass(unittest.TestCase):
    def test_init(self):
        deck: Deck = Deck()
        self.assertEqual(52, deck.size())
