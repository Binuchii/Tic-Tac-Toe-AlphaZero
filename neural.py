import numpy as np
import math
import random

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))  # Initialize an empty board
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

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.available_actions())

    def best_child(self, exploration_weight=1.4):
        # Avoid ZeroDivisionError by filtering out nodes with zero visits
        choices_weights = [
            (child.wins / child.visits) + exploration_weight * math.sqrt(math.log(self.visits) / (child.visits + 1e-6))
            if child.visits > 0 else float('-inf')  # Assign a very low value to unvisited nodes
            for child in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def expand(self):
        legal_actions = self.state.available_actions()
        for action in legal_actions:
            new_state = TicTacToe()
            new_state.board = self.state.board.copy()
            new_state.current_player = self.state.current_player
            new_state.take_action(action)
            child_node = Node(new_state, parent=self)
            self.children.append(child_node)

    def backpropagate(self, result):
        self.visits += 1
        if result is not None:
            self.wins += result
        if self.parent is not None:
            self.parent.backpropagate(-result)  # Invert result for the parent

def mcts_search(root, simulations):
    for _ in range(simulations):
        node = root

        # Selection
        while node.is_fully_expanded() and not node.state.check_winner():
            node = node.best_child()

        # Expansion
        if not node.state.check_winner():
            node.expand()
            node = random.choice(node.children)  # Select a random child for simulation

        # Simulation
        result = simulate_random_game(node.state)

        # Backpropagation
        node.backpropagate(result)

    return root.best_child(exploration_weight=0)  # Return the best action based on value

def simulate_random_game(state):
    while state.check_winner() is None:
        legal_actions = state.available_actions()
        action = random.choice(legal_actions)
        state.take_action(action)
    return state.check_winner()  # Return the game result

# Game Simulation
if __name__ == "__main__":
    game = TicTacToe()

    while game.check_winner() is None:
        game.render()  # Display current board state

        # Player 1's (Human) Move: Random move for simulation purposes
        legal_moves = game.available_actions()
        if legal_moves:  # Check if there are any legal moves left
            move = random.choice(legal_moves)  # Simulate a random move for Player 1
            print(f"Player 1 (Human) chooses move: {move}")
            game.take_action(move)

        if game.check_winner() is not None:
            break  # Exit if the game has been won after Player 1's move

        # Player 2's (AI) Move using MCTS
        root_node = Node(game)
        best_action_node = mcts_search(root_node, simulations=100)
        game = best_action_node.state  # Update the game state

    # Final board state and winner announcement
    game.render()
    winner = game.check_winner()
    if winner == 1:
        print("Player 1 wins!")
    elif winner == -1:
        print("Player 2 (AI) wins!")
    else:
        print("It's a draw!")
