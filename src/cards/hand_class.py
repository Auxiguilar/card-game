from src.cards.card_class import Card


class Hand():
    '''A hand that takes an optional argument `capacity`. Starts empty. Has a length.'''


    def __init__(self, capacity: int | None = None):
        self.cards: list[Card] = []
        if capacity:
            self.capacity = capacity

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self) -> str:
        cards: list[str] = [str(card) for card in self.cards]
        return f'{', '.join(cards)}.'

    def __repr__(self) -> str:
        return f'Hand(capacity={self.capacity if hasattr(self, 'capacity') else None})'

    def sort(self) -> None:
        '''Sorts the deck according to card value.'''

        self.cards.sort()

    def add_card(self, card: Card) -> None:
        '''Adds a card to the hand. Does not call sort.'''

        if hasattr(self, 'capacity'):
            if len(self) >= self.capacity:
                raise IndexError(f'Hand is full. Capacity: {self.capacity}')

        self.cards.append(card)

    def draw_card(self, pos: int) -> Card:
        '''Draws a card from the hand at the given index, removing it from the hand.'''

        if not self.cards:
            raise IndexError('Drawing from and empty hand.')
        
        return self.cards.pop(pos)
