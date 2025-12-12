from src.cards.hand_class import Hand


class Player():
    def __init__(self, name: str, id: int):
        self.name: str = name
        self.id: int = 0
        self.score: int = 0
        self.hand: Hand = Hand()

    def __repr__(self) -> str:
        return f'Player(name={self.name})'
    
    def __str__(self) -> str:
        return self.name
    