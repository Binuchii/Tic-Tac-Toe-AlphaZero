# Monte Carlo Tree Search for Tic-Tac-Toe

## Overview

This project implements a Monte Carlo Tree Search (MCTS) algorithm to play the game of Tic-Tac-Toe. The AI can play against a human player, using MCTS to determine optimal moves based on the current state of the game board.

## Features

- Interactive command-line interface for players to enter their moves.
- MCTS algorithm for the AI to determine its moves.
- Basic win detection and game state management.
- Supports two players: human and AI.

## Requirements

- Python 3.x
- NumPy library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-mcts.git
## Navigate to the Project Directory

cd tic-tac-toe-mcts

## Install the Required Dependencies
pip install numpy

##Usage
To start the game, run the neural.py script:

python neural.py


## Input
Players take turns entering their moves by specifying the row and column (0-indexed).
Example input: 1 1 for placing a mark in the center of the board.

## Board Representation
The board is represented as a 3x3 NumPy array.

0 indicates an empty space
1 indicates a player's mark
-1 indicates the AI's mark

## Game Rules
The first player to align three marks in a row (horizontally, vertically, or diagonally) wins the game.
If the board is full and no player has three marks in a row, the game is a draw.
How MCTS Works
Selection: Starting from the root node, the algorithm selects child nodes based on a balance of exploration and exploitation (using UCT).
Expansion: Once it reaches a leaf node, the algorithm expands the node by adding a new child for a random available move.
Simulation: The algorithm simulates a random play from the new node to a terminal state (win/loss/draw).
Backpropagation: The results of the simulation are propagated back up the tree, updating visit counts and win scores.
Future Improvements
Enhance win detection logic for various game states.
Add support for other games beyond Tic-Tac-Toe.
Implement a more sophisticated AI using neural networks.
