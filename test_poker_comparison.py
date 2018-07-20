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

#
# def test_straight():
#     royal_flush = FiveCardHand(['AS', 'KS', 'TS', 'JS', 'QS'])
#     assert royal_flush.get_hand_value() == 4
#
#
# def test_three_kind():
#     royal_flush = FiveCardHand(['AS', 'KS', 'TS', 'JS', 'QS'])
#     assert royal_flush.get_hand_value() == 3
#
#
# def test_two_pair():
#     royal_flush = FiveCardHand(['AS', 'KS', 'TS', 'JS', 'QS'])
#     assert royal_flush.get_hand_value() == 2
#
#
# def test_one_pair():
#     royal_flush = FiveCardHand(['AS', 'KS', 'TS', 'JS', 'QS'])
#     assert royal_flush.get_hand_value() == 1
#
#
# def test_high_card():
#     royal_flush = FiveCardHand(['AS', 'KS', 'TS', 'JS', 'QS'])
#     assert royal_flush.get_hand_value() == 0