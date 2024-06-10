import unittest
from CheckersGame import Checkers, InvalidPlayer, OutOfTurn, InvalidSquare

class TestCheckersGame(unittest.TestCase):
    def setUp(self):
        self.game = Checkers()
        self.player1 = self.game.create_player("Adam", "White")
        self.player2 = self.game.create_player("Lucy", "Black")

    def test_create_player(self):
        self.assertEqual(self.player1.player_name, "Adam")
        self.assertEqual(self.player1.checker_color, "White")
        self.assertEqual(self.player2.player_name, "Lucy")
        self.assertEqual(self.player2.checker_color, "Black")

    def test_play_game_invalid_player(self):
        with self.assertRaises(InvalidPlayer):
            self.game.play_game("Invalid", (5, 6), (4, 7))

    def test_play_game_out_of_turn(self):
        with self.assertRaises(OutOfTurn):
            self.game.play_game("Adam", (2, 1), (3, 0))

    def test_play_game_invalid_square(self):
        # First, let Lucy (black) make a valid move to ensure it's Adam's (white) turn
        self.game.play_game("Lucy", (5, 0), (4, 1))
        
        # Now it's Adam's turn, so we test the invalid square move
        with self.assertRaises(InvalidSquare):
            self.game.play_game("Adam", (8, 8), (9, 9))

    def test_get_checker_details(self):
        self.assertEqual(self.game.get_checker_details((0, 1)), "White")
        with self.assertRaises(InvalidSquare):
            self.game.get_checker_details((8, 8))

    def test_print_board(self):
        self.game.print_board()

if __name__ == "__main__":
    unittest.main()

