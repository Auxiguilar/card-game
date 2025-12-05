def main():
    print("Hello from card-game!")

    from src.cards.card_class import Card
    from src.cards.deck_class import Deck
    from src.cards.hand_class import Hand

    deck = Deck()
    deck.shuffle()

    hand: Hand = Hand(5)

    for i in range(hand.capacity):
            hand.add(deck.draw())

    print(str(hand))


if __name__ == "__main__":
    main()
