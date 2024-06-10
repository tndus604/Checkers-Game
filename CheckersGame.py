# Author: Su Youn Jeon
# GitHub username: tndus604
# Date: March 19, 2023
# Description: The program allows two people to play the game called Checkers. To win a game of checkers,
#           your goal is to capture or block your opponent's pieces so that they can no longer make a move.
#           You can move faster by jumping your opponent's pieces and removing them from the board.


class OutOfTurn(Exception):
    pass

class InvalidSquare(Exception):
    pass

class InvalidPlayer(Exception):
    pass

class Player:
    def __init__(self, player_name, checker_color):
        self.player_name = player_name
        self.checker_color = checker_color
        self.king_count = 0
        self.triple_king_count = 0
        self.captured_pieces_count = 0

    def get_king_count(self):
        return self.king_count

    def get_triple_king_count(self):
        return self.triple_king_count

    def get_captured_pieces_count(self):
        return self.captured_pieces_count


class Checkers:
    def __init__(self):
        self.board = self._initialize_board()
        self.players = {}
        self.turn = "Black"

    def _initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        # Initialize the board with pieces
        for i in range(8):
            if i % 2 == 0:
                for j in range(1, 8, 2):
                    if i < 3:
                        board[i][j] = "White"
                    elif i > 4:
                        board[i][j] = "Black"
            else:
                for j in range(0, 8, 2):
                    if i < 3:
                        board[i][j] = "White"
                    elif i > 4:
                        board[i][j] = "Black"
        return board

    def create_player(self, player_name, piece_color):
        if piece_color not in ["Black", "White"]:
            raise ValueError("Invalid piece color")
        player = Player(player_name, piece_color)
        self.players[player_name] = player
        return player

    def play_game(self, player_name, starting_square_location, destination_square_location):
        if player_name not in self.players:
            raise InvalidPlayer("Invalid player name")
        if self.players[player_name].checker_color.lower() != self.turn.lower():
            raise OutOfTurn("It is not your turn")
        
        start_x, start_y = starting_square_location
        dest_x, dest_y = destination_square_location
        
        if not self._is_valid_square(start_x, start_y) or not self._is_valid_square(dest_x, dest_y):
            raise InvalidSquare("Invalid square location")

        piece = self.board[start_x][start_y]
        if not piece or self.players[player_name].checker_color.lower() not in piece.lower():
            raise InvalidSquare("No checker to move or wrong checker color")

        # Placeholder for actual move logic
        captures = self._move_piece(start_x, start_y, dest_x, dest_y, piece)
        self.turn = "White" if self.turn == "Black" else "Black"
        return captures

    def _is_valid_square(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def _move_piece(self, start_x, start_y, dest_x, dest_y, piece):
        # Logic for moving pieces, capturing, and promoting to king/triple king
        # Update the board
        self.board[start_x][start_y] = None
        self.board[dest_x][dest_y] = piece
        
        # Placeholder for capturing logic
        captures = 0

        # Placeholder for king/triple king promotion
        if piece.lower() == "white" and dest_x == 7:
            self.board[dest_x][dest_y] = "White_King"
            self.players[piece.split('_')[0]].king_count += 1
        elif piece.lower() == "black" and dest_x == 0:
            self.board[dest_x][dest_y] = "Black_King"
            self.players[piece.split('_')[0]].king_count += 1

        return captures

    def get_checker_details(self, square_location):
        x, y = square_location
        if not self._is_valid_square(x, y):
            raise InvalidSquare("Invalid square location")
        return self.board[x][y]

    def print_board(self):
        for row in self.board:
            print(row)

    def game_winner(self):
        # Placeholder for actual game winner logic
        return "Game has not ended"

