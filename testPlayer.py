import unittest
from snake_ladder import SnakeGame, Dice, Player


class TestPlayer(unittest.TestCase):
    def test_initialization(self):
        player_obj = Player()
        self.assertEqual(player_obj.current_position, 0)
        self.assertEqual(player_obj.turn, 0)
        self.assertEqual(player_obj.old_position, 0)

    def test_incrementation(self):
        player_obj = Player()
        old_value = player_obj.turn
        player_obj.increment_turn()
        self.assertEqual(player_obj.turn, old_value + 1)

    def test_updateposition(self):
        player_obj = Player()
        old_position = player_obj.current_position
        player_obj.update_position(2)
        self.assertEqual(player_obj.current_position, old_position + 2)


if __name__ == "__main__":
    unittest.main()