import unittest
from src.cards.deck_class import Deck
from src.cards.card_class import Card


class TestDeckClass(unittest.TestCase):
    def test_init(self):
        deck: Deck = Deck()
        self.assertEqual(52, len(deck))

        top_card = deck.peek() # also checks peek! :)
        self.assertEqual(str(top_card), 'King of Clubs')

    def test_draw(self):
        deck: Deck = Deck()
        card: Card = deck.draw()
        self.assertEqual(str(card), 'King of Clubs')
        self.assertEqual(len(deck), 51)

        deck.cards = []

        with self.assertRaises(IndexError):
            draw_empty: Card = deck.draw()
    
    def test_add(self):
        deck_1: Deck = Deck()
        deck_2: Deck = Deck()

        card = deck_1.draw()
        deck_2.add(card)

        self.assertEqual(51, len(deck_1))
        self.assertEqual(53, len(deck_2))

        deck_3: Deck = Deck()
        card_card: Card = Card('queen', 'hearts')
        deck_3.add(card=card_card)
        self.assertEqual(card_card, deck_3.peek())

    def test_len(self):
        deck: Deck = Deck()
        self.assertEqual(52, len(deck))

        deck.cards = []
        self.assertFalse(deck)

    def test_str(self):
        deck: Deck = Deck()
        self.assertEqual(str(deck), 'A deck with 52 cards.')

    # Unfortunately I'm not sure how to test the shuffle method, since it'll just introduce the possibility
    # the whole test fails every once in a while, which defeats the purpose.
