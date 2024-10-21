import math
import random

import numpy as np

from gameRules import TicTacToe


class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state  # Game state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

    def expand(self, game):
        # Expand all possible children for the current node
        for action in game.available_actions():
            new_game = TicTacToe()
            new_game.board = self.state.board.copy()
            new_game.current_player = self.state.current_player
            new_game.take_action(action)
            self.children.append(MCTSNode(new_game, parent=self))

    def best_child(self, exploration_weight=1.4):
        # Select the best child node based on UCB1 formula
        choices_weights = [(child.value / (child.visits + 1e-6)) + exploration_weight * math.sqrt(math.log(self.visits + 1) / (child.visits + 1e-6)) for child in self.children]
        return self.children[np.argmax(choices_weights)]

    def simulate(self, game):
        # Simulate random playout until the end of the game
        while game.check_winner() is None:
            available_actions = game.available_actions()
            action = random.choice(available_actions)
            game.take_action(action)
        return game.check_winner()  # Return the winner of the simulation

    def backpropagate(self, result):
        # Backpropagate the result of the simulation up the tree
        self.visits += 1
        self.value += result  # Positive for win, negative for loss
        if self.parent:
            self.parent.backpropagate(-result)

def mcts_search(game, simulations=100):
    root = MCTSNode(game)
    for _ in range(simulations):
        node = root
        while node.children:  # Select the best node
            node = node.best_child()
        if not node.visits:  # If not visited, simulate
            result = node.simulate(game)
            node.backpropagate(result)
        else:
            node.expand(game)  # If visited, expand the node
    return root.best_child(exploration_weight=0)  # Return the best action based on value
