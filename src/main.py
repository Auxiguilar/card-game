from deck.deck import Deck

def main():
    print("Hello from card-game!")
    
    deck: Deck = Deck()
    print(deck.cards)
    deck.insert((1, 'spades'), 'bottom')
    print(deck.cards)


if __name__ == "__main__":
    main()
