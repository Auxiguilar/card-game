from src.cards.hand_class import Hand


class Player():
    def __init__(self, name: str):
        self.name: str = name
        self.hand: Hand = Hand()

    def __repr__(self) -> str:
        return f'Player(name={self.name})'
    
    def __str__(self) -> str:
        return self.name
