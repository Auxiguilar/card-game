from cards.card_class import Card


class Hand():
    '''A hand that takes a `capacity`, defaulting to 7.'''


    def __init__(self, capacity: int = 7):
        self.cards: list[Card] = []
        self.capacity: int = capacity
