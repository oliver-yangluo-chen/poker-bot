from card import *

class Agent:
    def __init__(self, hand, stack):
        self.hand = hand  # Expects a list of 2 Card objects
        self.stack = stack  # An integer representing the player's money

    def __str__(self):
        hand_str = ", ".join([f"{card.rank}{card.suit}" for card in self.hand])
        return f"Player with hand: {hand_str} and stack: ${self.stack}"

# Example usage
# Creating a poker player with a pair of cards and a specific stack amount
player = Agent([Card(10, 'H'), Card(10, 'D')], 1000)  # Player with a pair of Tens and a stack of $1000
print(player)

