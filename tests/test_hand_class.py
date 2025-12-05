import unittest
from src.cards.hand_class import Hand
from src.cards.deck_class import Deck
from src.cards.card_class import Card


class TestDeckClass(unittest.TestCase):
    def test_init(self):
        hand_1: Hand = Hand()
        self.assertFalse(hasattr(hand_1, 'capacity'))

        hand_2: Hand = Hand(5)
        self.assertTrue(hasattr(hand_2, 'capacity'))

    def test_len(self):
        deck: Deck = Deck()

        hand: Hand = Hand(5)
        self.assertFalse(hand)

        for i in range(hand.capacity):
            hand.add(deck.draw())

        self.assertEqual(len(hand), 5)

    def test_str(self):
        deck: Deck = Deck()

        hand: Hand = Hand(5)
        self.assertFalse(hand)

        for i in range(hand.capacity):
            hand.add(deck.draw())

        self.assertEqual(
            str(hand),
            'King of Clubs, Queen of Clubs, Jack of Clubs, Ten of Clubs, Nine of Clubs.'
        )

    def test_sort(self):
        deck: Deck = Deck()
        deck.shuffle()
        hand: Hand = Hand(5)

        for i in range(hand.capacity):
            hand.add(deck.draw())

        hand.sort()

        # woops, maybe I should implement some more dunders...
        self.assertLess(hand.cards[0], hand.cards[4])

    def test_draw(self):
        deck: Deck = Deck()
        hand: Hand = Hand(5)

        for i in range(hand.capacity):
            hand.add(deck.draw())

        cards: list[Card] = []
        hand_copy: list[Card] = hand.cards.copy()

        for j in range(hand.capacity):
            cards.append(hand.draw(0))

        self.assertListEqual(cards, hand_copy)

    def test_add(self):
        deck: Deck = Deck()
        deck.shuffle()
        hand: Hand = Hand(5)

        for i in range(hand.capacity):
            hand.add(deck.draw())
