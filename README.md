# Checkers-Game
This project implements a variation of the classic game of Checkers with modified rules. The game allows two players to compete by moving their pieces diagonally across a board, capturing opponent pieces, and promoting pieces to kings and triple kings.

## Installtion
1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Ensure you have Python installed.
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## How to Play
### Commnad-Line Version
1. Run the Checkers game:
    ```sh
    python3 PlayCheckers.py
    ```

2. Follow the prompts to make moves.

    #### Example Ouput
    ![Commnad-line ouput](./assets/output_1.png)

### GUI Version
1. Run the Checkers game with GUI:
    ```sh
    python3 CheckersGUI.py
    ```

2. Use the mouse to click on a piece to select it and then click on the destination square to move it. The current turn and scores are displayed on the top.

    ### Video Demo
    ![Checkers GUI Demo](./assets/gui_demo.gif)


## Game Rules
- Objective: Capture all opponent's pieces or block them so they can't make a move.
Moves: Pieces move diagonally on dark squares.
- Captures: Jump over an opponent's piece to capture it. Multiple captures are possible in a single turn.
- King Promotion: A piece that reaches the opponent's side is promoted to a king.
- Triple King: A king that returns to its original side is promoted to a triple king with additional abilities.

For detailed rules, refer to the [Game Rules document](./assets/Game_Rules.docx).

## Testing
To run the unit tests for the game, execute the following command:
```sh
python3 CheckersGameTester.py
```

## License
This project is licensed under the MIT License. 

Enjoy playing Checkers!