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
        deck_1: Deck = Deck()

        with self.assertRaises(ValueError):
            draw_invalid: list = deck_1.draw(-3)

        with self.assertWarns(UserWarning):
            draw_too_much: list = deck_1.draw(54)

        deck_2: Deck = Deck()
        
        draw_one: list = deck_2.draw()
        self.assertEqual(1, len(draw_one))

        draw_more: list = deck_2.draw(3)
        self.assertEqual(3, len(draw_more))

        draw_all: list = deck_2.draw(48)
        self.assertEqual(48, len(draw_all))

        with self.assertRaises(IndexError):
            draw_empty: list = deck_2.draw()
    
    def test_add(self):
        deck_1: Deck = Deck()
        deck_2: Deck = Deck()

        card = deck_1.draw()[0] # <-- returns a list
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

        cards: list = deck.draw(52)
        self.assertFalse(deck)

    def test_str(self):
        deck: Deck = Deck()
        self.assertEqual(str(deck), 'A deck with 52 cards.')

    # Unfortunately I'm not sure how to test the shuffle method, since it'll just introduce the possibility
    # the whole test fails every once in a while, which defeats the purpose. Method .size() is just len();
    # not worth testing...
