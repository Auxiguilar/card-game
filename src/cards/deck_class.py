import random
import warnings
from src.cards.card_class import Card

class Deck():
    '''A basic 52-card deck. Is initialized unshuffled; must be shuffled with `.shuffle()` for a randomized deck. Cards are represented as class `Card` with a `rank`, `suit`, and `value`. Has a length.'''

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
        'knight',
        'queen',
        'king'
    ]

    SUITS: list[str] = [
        'spades',
        'hearts',
        'diamonds',
        'clubs'
    ]

    def __init__(self):
        self.cards: list[Card] = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]

    def __len__(self) -> int:
        return len(self.cards)
    
    def __repr__(self) -> str:
        return f'Deck(size={len(self)})' # most relevant state
    
    def __str__(self) -> str:
        return f'A deck with {len(self)} cards.'
    
    def shuffle(self):
        '''Shuffles the deck.'''

        random.shuffle(self.cards)

    def draw(self, n: int = 1) -> list[Card]:
        '''Draws a given number `n` of cards from the top of the deck, removing them from the deck and returning them.'''

        if not self:
            raise IndexError('Drawing from an empty deck.')

        if n > len(self):
            warnings.warn(f'Argument "n" ({n}) is larger than current deck size ({len(self)}). Entire deck returned.', UserWarning)
            n = len(self)
        elif n < 1:
            raise ValueError(f'Invalid number of cards: {n}')

        cards: list[Card] = []

        for i in range(n):
            cards.append(self.cards.pop())
        
        return cards
    
    def peek(self) -> Card:
        '''Returns the card at the top of the deck, preserving the deck.'''

        if not self.cards:
            raise IndexError('Peeking at an empty deck.')
        
        return self.cards[-1]
        
    def add(self, card: Card, pos: int = -1, rand: bool = False):
        '''Adds a card to the deck, defaulting to the top. If `rand == True`, adds it to a random index in the deck.'''

        if rand == True:
            self.cards.insert(random.randint(0, len(self) - 1), card)
        elif pos == -1 or pos == len(self) - 1:
            self.cards.append(card)
        else:
            self.cards.insert(pos, card)


