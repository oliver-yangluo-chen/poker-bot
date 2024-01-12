from card import *

def evaluate(cards):
    if len(cards) != 7:
        raise ValueError("Must have exactly 7 cards")

    # Sorting cards by rank for easier evaluation
    cards.sort(key=lambda x: x.rank, reverse=True)

    # Helper functions
    def get_flush():
        suit_counts = {suit: [] for suit in ['H', 'D', 'C', 'S']}
        for card in cards:
            suit_counts[card.suit].append(card)
        for suit, suited_cards in suit_counts.items():
            if len(suited_cards) >= 5:
                return suited_cards[:5]
        return None

    def get_straight(flush_cards=None):
        selected_cards = flush_cards if flush_cards else cards
        unique_cards = sorted(set(selected_cards), key=lambda x: x.rank, reverse=True)
        unique_ranks = [card.rank for card in unique_cards]

        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i] - unique_ranks[i + 4] == 4:
                return unique_cards[i:i + 5]
        # Special case for Ace-low straight
        if set(unique_ranks[:4] + [unique_ranks[-1]]) == {2, 3, 4, 5, 14}:
            return unique_cards[:4] + [unique_cards[-1]]
        return None

    def get_straight_flush():
        flush_cards = get_flush()
        if flush_cards:
            straight_flush = get_straight(flush_cards)
            if straight_flush:
                return straight_flush
        return None

    def get_quads():
        rank_counts = {}
        for card in cards:
            rank_counts.setdefault(card.rank, []).append(card)
        for rank, grouped_cards in rank_counts.items():
            if len(grouped_cards) == 4:
                return grouped_cards
        return None

    def get_full_house():
        rank_counts = {}
        for card in cards:
            rank_counts.setdefault(card.rank, []).append(card)
        three_of_kind = None
        pair = None
        for rank, grouped_cards in rank_counts.items():
            if len(grouped_cards) == 3:
                if not three_of_kind or rank > three_of_kind[0].rank:
                    three_of_kind = grouped_cards
            elif len(grouped_cards) == 2:
                if not pair or rank > pair[0].rank:
                    pair = grouped_cards
        if three_of_kind and pair:
            return three_of_kind + pair
        return None

    def get_three_of_a_kind():
        rank_counts = {}
        for card in cards:
            rank_counts.setdefault(card.rank, []).append(card)
        for rank, grouped_cards in rank_counts.items():
            if len(grouped_cards) == 3:
                return grouped_cards
        return None

    def get_two_pair():
        rank_counts = {}
        pairs = []
        for card in cards:
            rank_counts.setdefault(card.rank, []).append(card)
        for grouped_cards in rank_counts.values():
            if len(grouped_cards) == 2:
                pairs.append(grouped_cards)
                if len(pairs) == 2:
                    return pairs[0] + pairs[1]
        return None

    def get_pair():
        rank_counts = {}
        for card in cards:
            rank_counts.setdefault(card.rank, []).append(card)
        for grouped_cards in rank_counts.values():
            if len(grouped_cards) == 2:
                return grouped_cards
        return None

    # Checking for hand types in order of strength
    straight_flush = get_straight_flush()
    if straight_flush:
        return "Straight Flush", straight_flush

    quads = get_quads()
    if quads:
        return "Four of a Kind", quads

    full_house = get_full_house()
    if full_house:
        return "Full House", full_house

    flush = get_flush()
    if flush:
        return "Flush", flush

    straight = get_straight()
    if straight:
        return "Straight", straight

    three_of_a_kind = get_three_of_a_kind()
    if three_of_a_kind:
        return "Three of a Kind", three_of_a_kind

    two_pair = get_two_pair()
    if two_pair:
        return "Two Pair", two_pair

    pair = get_pair()
    if pair:
        return "One Pair", pair

    return "High Card", sorted(cards, key=lambda x: x.rank, reverse=True)[:5]

# Completing the test case for a Straight Flush hand
straight_flush_hand = [
    Card(14, 'H'),  # Ace of Hearts
    Card(13, 'H'),  # King of Hearts
    Card(12, 'H'),  # Queen of Hearts
    Card(11, 'H'),  # Jack of Hearts
    Card(10, 'H'),  # Ten of Hearts
    Card(3, 'D'),   # Three of Diamonds (irrelevant for this hand)
    Card(2, 'S')    # Two of Spades (irrelevant for this hand)
]

# Testing the function
hand_type, winning_cards = evaluate(straight_flush_hand)
print(hand_type, [(card.rank, card.suit) for card in winning_cards])  # Displaying card details





def compare_hands(hand1_type, hand1_cards, hand2_type, hand2_cards):
    hand_strengths = {
        "Straight Flush": 8, "Four of a Kind": 7, "Full House": 6,
        "Flush": 5, "Straight": 4, "Three of a Kind": 3,
        "Two Pair": 2, "One Pair": 1, "High Card": 0
    }

    # Compare hand types first
    if hand_strengths[hand1_type] > hand_strengths[hand2_type]:
        return "First hand wins"
    elif hand_strengths[hand1_type] < hand_strengths[hand2_type]:
        return "Second hand wins"

    # If hand types are the same, compare the ranks
    hand1_cards_sorted = sorted(hand1_cards, key=lambda x: x.rank, reverse=True)
    hand2_cards_sorted = sorted(hand2_cards, key=lambda x: x.rank, reverse=True)

    for card1, card2 in zip(hand1_cards_sorted, hand2_cards_sorted):
        if card1.rank > card2.rank:
            return "First hand wins"
        elif card1.rank < card2.rank:
            return "Second hand wins"

    # If all ranks are the same, it's a tie
    return "Tie"

# Example usage
hand1_type = "Flush"
hand1_cards = [Card(14, 'H'), Card(13, 'H'), Card(12, 'H'), Card(11, 'H'), Card(10, 'H')]  # Flush with Ace high

hand2_type = "Flush"
hand2_cards = [Card(13, 'H'), Card(12, 'H'), Card(11, 'H'), Card(10, 'H'), Card(9, 'H')]  # Flush with King high

print(compare_hands(hand1_type, hand1_cards, hand2_type, hand2_cards))