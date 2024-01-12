class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # Mapping numeric ranks to their respective characters for face cards
        rank_str = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(self.rank, str(self.rank))
        return f"{rank_str}{self.suit}"

# Testing the updated Card class
card1 = Card(11, 'H')  # Jack of Hearts
card2 = Card(7, 'D')   # Seven of Diamonds
print(card1, card2)

