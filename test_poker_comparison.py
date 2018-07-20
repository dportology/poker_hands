from poker_comparison import FiveCardHand, compare_hands


def test_royal_flush():
    royal_flush1 = FiveCardHand(['AS', 'KS', 'TS', 'JS', 'QS'])
    assert royal_flush1.get_hand_value() == 9
    not_royal_flush = FiveCardHand(['AS', 'KC', 'TS', 'JS', 'QS'])
    assert not_royal_flush.get_hand_value() != 9
    royal_flush2 = FiveCardHand(['KD', 'AD', 'JD', 'QD', 'TD'])
    assert royal_flush2.get_hand_value() == 9


def test_straight_flush():
    not_straight_flush = FiveCardHand(['5S', '6S', '7S', '8S', '9D'])
    assert not_straight_flush.get_hand_value() != 8

    straight_flush1 = FiveCardHand(['6S', '2S', '5S', '4S', '3S'])
    assert straight_flush1.get_hand_value() == 8
    straight_flush2 = FiveCardHand(['6S', '7S', '8S', '9S', 'TS'])
    assert straight_flush2.get_hand_value() == 8

    assert compare_hands(straight_flush1, straight_flush2) is False


def test_four_kind():
    not_four_kind = FiveCardHand(['5C', '2S', '4S', '5S', '5D'])
    assert not_four_kind.get_hand_value() != 7

    four_kind1 = FiveCardHand(['TS', 'QS', 'TD', 'TC', 'TH'])
    assert four_kind1.get_hand_value() == 7
    four_kind2 = FiveCardHand(['2C', '2D', '2H', '2S', '9S'])
    assert four_kind2.get_hand_value() == 7

    assert compare_hands(four_kind1, four_kind2) is True


def test_full_house():
    not_full_house = FiveCardHand(['AS', 'AD', 'TS', 'TD', 'QS'])
    assert not_full_house.get_hand_value() != 6

    full_house1 = FiveCardHand(['AS', 'AD', 'TS', 'TD', 'TC'])
    assert full_house1.get_hand_value() == 6
    full_house2 = FiveCardHand(['TS', 'TD', 'TC', '7D', '7S'])
    assert full_house2.get_hand_value() == 6

    assert compare_hands(full_house1, full_house1) is True


def test_flush():
    not_flush = FiveCardHand(['5S', '6S', 'TS', '2D', '3S'])
    assert not_flush.get_hand_value() != 5

    flush1 = FiveCardHand(['5S', '6S', 'QS', '2S', '3S'])
    assert flush1.get_hand_value() == 5
    flush2 = FiveCardHand(['JS', '6S', '8S', '3S', '4S'])
    assert flush2.get_hand_value() == 5

    assert compare_hands(flush1, flush2) is True


def test_straight():
    not_straight = FiveCardHand(['3S', '4S', '5D', '6S', 'QS'])
    assert not_straight.get_hand_value() != 4

    straight1 = FiveCardHand(['7S', '8S', '9D', 'TS', 'JS'])
    assert straight1.get_hand_value() == 4
    straight2 = FiveCardHand(['3S', '4S', '7S', '5C', '6D'])
    assert straight2.get_hand_value() == 4

    assert compare_hands(straight1, straight2) is True


def test_three_kind():
    not_three_kind = FiveCardHand(['QS', 'KS', 'QS', '2S', '5D'])
    assert not_three_kind.get_hand_value() != 3

    three_kind1 = FiveCardHand(['QS', 'QS', 'QS', '2S', '5D'])
    assert three_kind1.get_hand_value() == 3
    three_kind2 = FiveCardHand(['QS', '2S', '3S', '3C', '3D'])
    assert three_kind2.get_hand_value() == 3

    assert compare_hands(three_kind1, three_kind2) is True


def test_two_pair():
    not_two_pair = FiveCardHand(['QS', 'KS', 'QS', '2S', '5D'])
    assert not_two_pair.get_hand_value() != 2

    two_pair1 = FiveCardHand(['QS', 'QS', '5S', '2S', '5D'])
    assert two_pair1.get_hand_value() == 2
    two_pair2 = FiveCardHand(['JS', '2S', '2S', '3C', 'JD'])
    assert two_pair2.get_hand_value() == 2

    assert compare_hands(two_pair1, two_pair2) is True


def test_one_pair():
    not_one_pair = FiveCardHand(['AS', 'KS', '5S', '6S', '2D'])
    assert not_one_pair.get_hand_value() != 1

    one_pair1 = FiveCardHand(['AS', 'AD', '4S', '2S', '6H'])
    assert one_pair1.get_hand_value() == 1
    one_pair2 = FiveCardHand(['AH', 'KS', 'TS', 'TD', 'QC'])
    assert one_pair2.get_hand_value() == 1

    assert compare_hands(one_pair1, one_pair2) is True


def test_high_card():
    high_card1 = FiveCardHand(['5S', '2D', 'AC', 'JS', 'QS'])
    assert high_card1.get_hand_value() == 0
    high_card2 = FiveCardHand(['5S', '2D', '7C', 'JS', 'QS'])
    assert high_card2.get_hand_value() == 0

    assert compare_hands(high_card1, high_card2) is True
