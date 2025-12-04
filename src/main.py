def main():
    print("Hello from card-game!")

    from src.cards.card_class import Card
    from src.cards.deck_class import Deck

    card = Card('ace', 'spades')
    deck = Deck()
    deck.add(card=card)

    print(deck.peek())


if __name__ == "__main__":
    main()
