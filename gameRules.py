import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))  # 3x3 board, 0 = empty, 1 = player1, -1 = player2
        self.current_player = 1  # Player 1 starts

    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        return self.board

    def available_actions(self):
        # Returns a list of available moves (empty cells)
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def take_action(self, action):
        # Apply the move to the board
        if self.board[action] == 0:
            self.board[action] = self.current_player
            self.current_player = -self.current_player  # Switch player
        else:
            raise ValueError("Invalid action!")

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3 or abs(sum(self.board[:, i])) == 3:
                return np.sign(sum(self.board[i, :]))  # Return the winning player
        if abs(self.board.trace()) == 3 or abs(np.fliplr(self.board).trace()) == 3:
            return np.sign(self.board.trace())
        if len(self.available_actions()) == 0:  # No moves left = draw
            return 0
        return None  # No winner yet

    def render(self):
        # Print the board for visualization
        print(self.board)
