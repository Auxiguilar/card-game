import random

class Deck():
    '''A basic 52-card deck. Is initialized unshuffled; must be shuffled with `.shuffle()` for a randomized deck. Cards are represented as tuples of `(rank: int, suit: str)`.'''

    SUITS: list[str] = ['spades', 'hearts', 'diamonds', 'clubs']
    RANKS: list[int] = list(range(1,14))

    def __init__(self):
        self.cards: list[tuple[int, str]] = [(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, pos: str = 'top') -> tuple[int, str]:
        '''Draws a card at the given position `pos`. Position argument must be either "top", "bottom", or "random", and defaults to "top".'''

        if pos == 'top':
            return self.cards.pop()
        elif pos == 'bottom':
            return self.cards.pop(0)
        elif pos == 'random':
            return self.cards.pop(random.randint(0, len(self.cards) - 1))
        else:
            raise ValueError('Position argument must be either "top", "bottom", or "random".')
    
    def peek(self, pos: str = 'top') -> tuple[int, str]:
        '''Peeks at a card at the given position `pos`. Position argument must be either "top", "bottom", or "random", and defaults to "top".'''

        if pos == 'top':
            return self.cards[-1]
        elif pos == 'bottom':
            return self.cards[0]
        elif pos == 'random':
            return self.cards[random.randint(0, len(self.cards) - 1)]
        else:
            raise ValueError('Position argument must be either "top", "bottom", or "random".')
        
    def insert(self, card: tuple[int, str], pos: str = 'top'):
        '''Inserts a card at the given position `pos`. Position argument must be either "top", "bottom", or "random", and defaults to "top".'''

        if pos == 'top':
            self.cards.append(card)
        elif pos == 'bottom':
            return self.cards.insert(0, card)
        elif pos == 'random':
            return self.cards.insert(random.randint(0, len(self.cards) - 1), card)
        else:
            raise ValueError('Position argument must be either "top", "bottom", or "random".')
