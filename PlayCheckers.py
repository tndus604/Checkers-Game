from CheckersGame import Checkers, OutOfTurn, InvalidSquare, InvalidPlayer

def main():
    game = Checkers()
    player1 = game.create_player("Adam", "White")
    player2 = game.create_player("Lucy", "Black")

    print("Welcome to Checkers!")
    game.print_board()

    while True:
        try:
            # Display the current player's turn
            current_player = player1 if game.turn == "White" else player2
            print(f"\n{current_player.player_name}'s ({current_player.checker_color}) turn.")

            # Get the move from the player
            start_x = int(input("Enter the starting square row: "))
            start_y = int(input("Enter the starting square column: "))
            dest_x = int(input("Enter the destination square row: "))
            dest_y = int(input("Enter the destination square column: "))

            # Attempt the move
            captures = game.play_game(current_player.player_name, (start_x, start_y), (dest_x, dest_y))
            print(f"Move successful! Captured pieces: {captures}")

            # Print the updated board
            game.print_board()

            # Check for a winner
            winner = game.game_winner()
            if winner != "Game has not ended":
                print(f"Congratulations! {winner} has won the game!")
                break

        except OutOfTurn:
            print("It's not your turn! Please wait for your turn.")
        except InvalidSquare:
            print("Invalid square. Please try again.")
        except InvalidPlayer:
            print("Invalid player. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid integers for the board positions.")

if __name__ == "__main__":
    main()