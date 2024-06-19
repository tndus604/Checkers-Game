import tkinter as tk
from tkinter import messagebox
from CheckersGame import Checkers, OutOfTurn, InvalidSquare, InvalidPlayer

class CheckersGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Checkers Game")
        
        self.game = Checkers()
        self.player1 = self.game.create_player("Adam", "White")
        self.player2 = self.game.create_player("Lucy", "Black")
        
        self.turn_label = tk.Label(root, text="Turn: White", font=("Helvetica", 16))
        self.turn_label.pack()
        
        self.score_frame = tk.Frame(root)
        self.score_frame.pack()
        
        self.white_score_label = tk.Label(self.score_frame, text="White Score: 0", font=("Helvetica", 14))
        self.white_score_label.pack(side=tk.LEFT, padx=20)
        
        self.black_score_label = tk.Label(self.score_frame, text="Black Score: 0", font=("Helvetica", 14))
        self.black_score_label.pack(side=tk.RIGHT, padx=20)
        
        self.canvas = tk.Canvas(root, width=800, height=800)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        
        self.selected_piece = None
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["white", "black"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1, y1 = col * 100, row * 100
                x2, y2 = x1 + 100, y1 + 100
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                
                piece = self.game.board[row][col]
                if piece:
                    self.draw_piece(row, col, piece)
        
        self.update_turn_label()
        self.update_scores()

    def draw_piece(self, row, col, piece):
        x1, y1 = col * 100 + 10, row * 100 + 10
        x2, y2 = x1 + 80, y1 + 80
        color = "red" if piece == "Black" else "white"
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def on_click(self, event):
        row, col = event.y // 100, event.x // 100
        if not self.selected_piece:
            if self.valid_piece_selection(row, col):
                self.selected_piece = (row, col)
            else:
                messagebox.showerror("Error", "No checker to move or wrong checker color")
        else:
            try:
                current_player = self.player1 if self.game.turn == "White" else self.player2
                self.game.play_game(current_player.player_name, self.selected_piece, (row, col))
                self.selected_piece = None
                self.draw_board()
                winner = self.game.game_winner()
                if winner != "Game has not ended":
                    self.show_winner(winner)
            except (OutOfTurn, InvalidSquare, InvalidPlayer) as e:
                messagebox.showerror("Error", str(e))
                self.selected_piece = None

    def valid_piece_selection(self, row, col):
        piece = self.game.board[row][col]
        current_color = "White" if self.game.turn == "White" else "Black"
        return piece == current_color

    def update_turn_label(self):
        current_turn = "White" if self.game.turn == "White" else "Black"
        self.turn_label.config(text=f"Turn: {current_turn}")

    def update_scores(self):
        white_score = self.player1.get_captured_pieces_count()
        black_score = self.player2.get_captured_pieces_count()
        self.white_score_label.config(text=f"White Score: {white_score}")
        self.black_score_label.config(text=f"Black Score: {black_score}")

    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"Congratulations! {winner} has won the game!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckersGUI(root)
    root.mainloop()

