from collections import Counter

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
        self.cards = sorted(cards, key=lambda x: ranks[x[0]])
        self.ranks = [ranks[card[0]] for card in self.cards]
        self.suits = [card[1] for card in self.cards]

    def get_high_card(self, rank=0):
        """
        Returns the nth highest valued card in a hand, default being 0, but there are instances when we need to
        compare the nth highest card of two hands
        """
        try:
            return self.ranks[-rank - 1]  # Need to get nth highest value in an ascending sorted list, so start at -1
        except IndexError:
            print(f'Cannot get card of rank {rank} from hand, quitting')

    def get_hand_value(self):
        """
        Calculates the score of a given hand, with a royal flush being 0, straight flush a 1, four of a kind 2 etc...
        Start with hands which exclude the possibility of other hands (e.g. royal flush means the hand
        is not a 2 pair
        :return: Score of any given hand
        """

        # Check if all cards are of the same suit, as this is the only instance in which poker cares about suit
        all_same_suit = True if len(set(self.suits)) == 1 else False

        if all_same_suit and self.ranks == list(range(10, 15)):
            # print('royal flush')
            return 0

        straight = True if self.ranks == list(range(self.ranks[0], self.ranks[0] + 5)) else False

        if all_same_suit and straight:
            # print('Straight Flush')
            return 1

        occurances = Counter(self.ranks)
        occurances_length = len(occurances.keys())
        if occurances_length == 2:
            if sorted(occurances.values()) == [1, 4]:
                # print('Four of a Kind')
                return 2
            else:
                # print('Full House')
                return 3

        if all_same_suit:
            # print('Flush')
            return 4

        if straight:
            # print('Straight')
            return 5

        if occurances_length == 3:
            if sorted(occurances.values())[-1] == 3:
                # print('Three of a Kind')
                return 6
            else:
                # print('Two Pairs')
                return 7

        if occurances_length == 4:
            # print('One Pair')
            return 9

        # print('High Card')
        return 10


def compare_hands(hand_1, hand_2):
    """
    Given 2 lists, get scores for both
    :return: True, if hand_1 is better than hand_2, None if tie
    """
    value_1 = hand_1.get_hand_value()
    value_2 = hand_2.get_hand_value()

    if value_1 < value_2:
        return True

    if value_1 == value_2:
        first_won = None
        i = 0
        while first_won is None and i < HAND_SIZE:
            first_won = (hand_1.get_high_card(i) > hand_2.get_high_card(i))
            i += 1

        return first_won


    return False


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


calculate_victories('poker.txt')
