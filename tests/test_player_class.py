import unittest
from src.player.player_class import Player
from src.cards.hand_class import Hand

class TestPlayerClass(unittest.TestCase):
    def test_init(self):
        player: Player = Player('Player')

        self.assertTrue(hasattr(player, 'name'))
        self.assertTrue(hasattr(player, 'hand'))
        self.assertTrue(hasattr(player, 'score'))
        self.assertTrue(player.name == 'Player')

    def test_str(self):
        player: Player = Player('Player')

        self.assertTrue(str(player) == 'Player')
