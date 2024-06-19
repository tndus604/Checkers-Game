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
    """
    The Checkers class represents a game of checkers
    """
    def __init__(self):
        self.board = self._initialize_board()
        self.players = {}
        self.turn = "Black"

    def _initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
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
        """
        Creates a player object with the specified name and piece color.

        Parameters:
        player_name (str): The name of the player.
        piece_color (str): The color of the player's pieces. Must be either "Black" or "White".

        Returns:
        Player: The created player object.

        Raises:
        ValueError: If piece_color is not "Black" or "White".
        """
        if piece_color not in ["Black", "White"]:
            raise ValueError("Invalid piece color")
        
        player = Player(player_name, piece_color)
        self.players[piece_color] = player
        return player

    def print_board(self):
        for row in self.board:
            print(" ".join(["." if cell is None else cell[0] for cell in row]))
        print()

    def play_game(self, player_name, start_pos, end_pos):
        """
        Moves a piece on the board according to the game's rules.

        Parameters:
        player_name (str): The name of the player making the move.
        start_pos (tuple): The starting square location of the piece in the format (x, y).
                        For example, (1, 2) represents the third square in the second row.
        end_pos (tuple): The destination square location of the piece in the format (x, y).
                        For example, (4, 3) represents the fourth square in the fifth row.

        Returns:
        list: A list of captured pieces during the move.

        Raises:
        InvalidPlayer: If the player_name is not valid.
        OutOfTurn: If the player is trying to move out of turn.
        InvalidSquare: If the move is invalid, such as moving from an empty square or to a wrong color piece.
        """
        if player_name not in [self.players["White"].player_name, self.players["Black"].player_name]:
            raise InvalidPlayer("Invalid player name")
        
        if (self.turn == "White" and self.players["White"].player_name != player_name) or \
           (self.turn == "Black" and self.players["Black"].player_name != player_name):
            raise OutOfTurn("It's not your turn")
        
        start_x, start_y = start_pos
        dest_x, dest_y = end_pos
        piece = self.board[start_x][start_y]

        if piece is None or (self.turn == "White" and piece != "White") or (self.turn == "Black" and piece != "Black"):
            raise InvalidSquare("No checker to move or wrong checker color")
        
        captures = self._move_piece(start_x, start_y, dest_x, dest_y, piece)
        self.turn = "White" if self.turn == "Black" else "Black"
        return captures

    def _move_piece(self, start_x, start_y, dest_x, dest_y, piece):
        """
        Handles the movement of a piece on the board, including capturing opponent pieces 
        and promoting pieces to kings.
        
        """
        self.board[dest_x][dest_y] = piece
        self.board[start_x][start_y] = None
        captures = []
        if abs(dest_x - start_x) == 2:
            capture_x, capture_y = (start_x + dest_x) // 2, (start_y + dest_y) // 2
            captures.append(self.board[capture_x][capture_y])
            self.board[capture_x][capture_y] = None
            self.players[piece].captured_pieces_count += 1
        if dest_x == 0 or dest_x == 7:
            self.players[piece].king_count += 1
        return captures

    def game_winner(self):
        """
        Determines the winner of the game.
        
        Returns:
        str: "White" if there are no black pieces left on the board, "Black" if there are no white pieces left on the board,
            or "Game has not ended" if neither player has won yet.
        """
        black_pieces = sum(row.count("Black") for row in self.board)
        white_pieces = sum(row.count("White") for row in self.board)

        if black_pieces == 0:
            return "White"
        elif white_pieces == 0:
            return "Black"
        return "Game has not ended"
