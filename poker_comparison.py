from collections import Counter
from time import time

HAND_SIZE = 5

ranks = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class FiveCardHand:
    """Represents a full poker hand in a 5 card game"""

    def __init__(self, cards):
        self.cards = sorted(cards, key=lambda x: ranks[x[0]], reverse=True)
        self.ranks = [ranks[card[0]] for card in self.cards]
        self.suits = [card[1] for card in self.cards]

    def get_hand_value(self):
        """
        Calculates the score of a given hand, with a royal flush being 9, straight flush a 8, four of a kind 7 etc...
        Start with hands which exclude the possibility of other hands (e.g. royal flush means the hand
        is not a regular flush, which it would quality for)
        :return: Score of any given hand
        """

        # Check if all cards are of the same suit, as this is the only instance in which poker cares about suit
        all_same_suit = True if len(set(self.suits)) == 1 else False

        if all_same_suit and self.ranks == list(range(14, 9, -1)):
            # royal flush
            return 9

        # Test if hand is a straight, meaning it matches a list of 5 consecutive values
        straight = True if self.ranks == list(range(self.ranks[0], self.ranks[0] - 5, -1)) else False

        if all_same_suit and straight:
            # Straight Flush
            return 8

        # Calculate duplicate of cards in the hand. Length of this object will tell us what kind of hand we may have
        occurrences = Counter(self.ranks)
        occurrences_length = len(occurrences.keys())
        if occurrences_length == 2:
            if sorted(occurrences.values()) == [1, 4]:
                # Four of a Kind
                return 7
            else:
                # Full House
                return 6

        if all_same_suit:
            # Flush
            return 5

        if straight:
            # Straight
            return 4

        if occurrences_length == 3:
            if sorted(occurrences.values())[-1] == 3:
                # Three of a Kind
                return 3
            else:
                # Two Pairs
                return 2

        if occurrences_length == 4:
            # One Pair
            return 1

        # High Card
        return 0

    def get_trump_card(self):
        """
        For tie breaking purposes. This sorts the list of card ranks with respect to the number of occurrences
        (most occurrences go the front of the list). e.g. a hand with a pair of fours could look like [4, 4, T, 9, 3]
        If we are comparing two hands with one pair, this would allow us to first examine the 4s to break the tie.
        For high card comparisons, this sort will do nothing, and we'll compare the high cards
        :return:
        """
        if len(set(self.ranks)) == HAND_SIZE:
            return self.ranks
        return [item for items, c in Counter(self.ranks).most_common() for item in [items] * c]


def compare_hands(hand_1, hand_2):
    """
    Given 2 lists, get scores for both and
    :return: True, if hand_1 is better than hand_2, None if tie
    """
    value_1 = hand_1.get_hand_value()
    value_2 = hand_2.get_hand_value()

    if value_1 != value_2:
        return value_1 > value_2

    else:

        trump_1 = hand_1.get_trump_card()
        trump_2 = hand_2.get_trump_card()

        i = 0
        while i < HAND_SIZE:
            if trump_1[i] != trump_2[i]:
                return trump_1[i] > trump_2[i]
            i += 1

    print('TIE')
    return True


def calculate_victories(filename):
    """
    Given a text file name, calculate the number of times the first player wins, and return
    :return: Int representing the number of times player 1 (the first player) won based on the hands given
    """

    first_hand_victories = 0
    with open(filename) as f:
        for line in f:
            hands = [i for i in line.split()]
            if compare_hands(FiveCardHand(hands[:5]), FiveCardHand(hands[5:])):
                first_hand_victories += 1

    print(first_hand_victories)
