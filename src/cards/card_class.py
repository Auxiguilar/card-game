
class Card():
    '''A basic card printed as "Rank of Suit".'''

    VALUES: dict[str, int] = {
        'ace': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'knight': 11,
        'queen': 12,
        'king': 13
    }

    def __init__(self, rank: str, suit: str):
        self.rank: str = rank
        self.suit: str = suit
        self.value: int = Card.VALUES[rank]

    def __str__(self) -> str:
        return f'{self.rank.capitalize()} of {self.suit.capitalize()}'
    
    def __repr__(self) -> str:
        return f'Card("{self.rank}", "{self.suit}")'
