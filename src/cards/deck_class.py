import random
from src.cards.card_class import Card


class Deck():
    '''A basic 52-card deck. Is initialized unshuffled; must be shuffled with `.shuffle()` for a randomized deck. Cards are represented as class `Card` with a `rank`, `suit`, and `value`. Has a length.
    
    Takes an optional `jokers` argument, which is the number of jokers to add to the top of the deck.'''

    RANKS: list[str] = [
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

    SUITS: list[str] = [
        'spades',
        'hearts',
        'diamonds',
        'clubs'
    ]

    def __init__(self, jokers: int | None = None):
        self.cards: list[Card] = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        
        if jokers:
            joker_cards: list[Card] = [Card('joker') for i in range(jokers)]
            self.cards.extend(joker_cards)

    def __len__(self) -> int:
        return len(self.cards)
    
    def __repr__(self) -> str:
        return f'Deck(size={len(self)})'
    
    def __str__(self) -> str:
        return f'A deck with {len(self)} cards.'
    
    def shuffle(self):
        '''Shuffles the deck.'''

        random.shuffle(self.cards)

    def draw(self) -> Card:
        '''Returns the card at the top of the deck, removing it from the deck.'''

        if not self:
            raise IndexError('Drawing from an empty deck.')

        return self.cards.pop()
    
    def peek(self) -> Card:
        '''Returns the card at the top of the deck, preserving the deck.'''

        if not self.cards:
            raise IndexError('Peeking at an empty deck.')
        
        return self.cards[-1]
        
    def add(self, card: Card, rand: bool = False):
        '''Adds a card to the top of the deck. If `rand == True`, inserts it at a random index in the deck.'''

        if rand == True:
            self.cards.insert(random.randint(0, len(self) - 1), card)
        else:
            self.cards.append(card)
