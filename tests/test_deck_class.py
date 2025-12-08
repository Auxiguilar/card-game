import unittest
from src.cards.deck_class import Deck
from src.cards.card_class import Card


class TestDeckClass(unittest.TestCase):
    def test_init(self):
        deck: Deck = Deck(1)
        self.assertEqual(53, len(deck))

        top_card = deck.peek()
        self.assertEqual(str(top_card), 'Joker')

    def test_draw(self):
        deck: Deck = Deck()
        card: Card = deck.draw_card()
        self.assertEqual(str(card), 'King of Clubs')
        self.assertEqual(len(deck), 51)

        deck.cards = []

        with self.assertRaises(IndexError):
            draw_empty: Card = deck.draw_card()
    
    def test_add(self):
        deck_1: Deck = Deck()
        deck_2: Deck = Deck()

        card = deck_1.draw_card()
        deck_2.add_card(card)

        self.assertEqual(51, len(deck_1))
        self.assertEqual(53, len(deck_2))

        deck_3: Deck = Deck()
        card_card: Card = Card('queen', 'hearts')
        deck_3.add_card(card=card_card)
        self.assertEqual(card_card, deck_3.peek())

    def test_len(self):
        deck: Deck = Deck()
        self.assertEqual(52, len(deck))

        deck.cards = []
        self.assertFalse(deck)

    def test_str(self):
        deck: Deck = Deck()
        self.assertEqual(str(deck), 'A deck with 52 cards.')

    def test_shuffle(self):
        shuffled_deck: Deck = Deck()
        comparison_deck: Deck = Deck()
        shuffled_deck.shuffle()

        # Since I can't find a listNotEqual, making some logic for it.
        try:
            self.assertListEqual(shuffled_deck, comparison_deck) # type: ignore

            # In the extremely unlikely event the above succeeds(fails):
            raise RuntimeError('shuffle() has somehow produced an identical list...')

            # Really, I think this is appropriate, since it really means
            # it works. Not that this will ever happen often, or at all...
            # If it did, that would be a problem, though at least then
            # you'd know.
        
        # Failure is expected! "Failure" is good!
        except self.failureException:
            pass
