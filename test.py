# Test the game environment
from gameRules import TicTacToe

game = TicTacToe()

# Reset the game and display the board
game.reset()
game.render()

# Test some actions
game.take_action((0, 0))  # Player 1 places a mark at (0, 0)
game.render()
print("Winner:", game.check_winner())
game.take_action((1, 1))  # Player 2 places a mark at (1, 1)
game.render()
print("Winner:", game.check_winner())
game.take_action((1, 0))  # Player 1 places a mark at (0, 0)
game.render()
print("Winner:", game.check_winner())
game.take_action((0, 2))  # Player 2 places a mark at (1, 1)
game.render()
print("Winner:", game.check_winner())
game.take_action((2, 0))  # Player 1 places a mark at (0, 0)
game.render()
print("Winner:", game.check_winner())

try:
    game.take_action((0, 0))  # Player 2 tries to place at (0, 0) which is already occupied
except ValueError as e:
    print(e)