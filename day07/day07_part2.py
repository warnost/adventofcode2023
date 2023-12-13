from collections import Counter

def score_data(data):

    # seperate hands and bids
    hands = parse_data(data)

    # Check for Jokers, Improve the hand,
    # then encode numerically for sorting
    for i, hand in enumerate(hands):
        if ("J" in hand[0]):
            new_hand = improve_hand(hand[0])
        else:
            new_hand = hand[0]

        hand.append([hand_type(new_hand)] + encode_hand(hand[0]))
        hand.append(new_hand)

    # Numeric encoding makes sorting and breaking ties ez
    hands = sorted(hands, key= lambda x: x[2], reverse=True)

    # Append ranks to hands
    ranks = list(range(1, len(hands)+1))
    ranks = sorted(ranks, reverse=True)

    for i, hand in enumerate(hands):
        hand.append(ranks[i])

    # multiply bid times rank, then sum them up for final score
    print(sum([hand[1] * hand[4] for hand in hands]))

def parse_data(data):
    """
    the hand and the bid come as a single string on each line.
    parse that string into a list [hand, bid]
    then convert the bid to an int so we can do math on it later
    """
    hands = []
    for row in data:
        hand = row.split()
        hand[1] = int(hand[1])
        hands.append(hand)

    return hands

def improve_hand(hand):
    """
    Takes a hand string and replaces jokers
    with cards to improve the hand
    """

    no_joker_hand = hand.replace('J','')

    joker_count = 5 - len(no_joker_hand)
    if (joker_count == 5):
        new_hand = 'AAAAA'
    else:
        # Find highest count cards in the no joker hand
        hand_counter = Counter(no_joker_hand)
        ordered_cards = hand_counter.most_common()
        highest_count = ordered_cards[0][1]
        highest_count_cards = [x[0] for x in ordered_cards if x[1] == highest_count]

        # find the best card among the highest count cards
        best_card = rank_cards(highest_count_cards)

        # replace the jokers with the best high count card
        new_hand = hand.replace('J',str(best_card))
    
    return new_hand

def rank_cards(card_list):
    """
    Takes a list of cards, returns the highest ranked
    """
    face_cards = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    new_card_list = []
    for card in card_list:
        if (not card.isdigit()):
            new_card_list.append(face_cards[card])
        else:
            new_card_list.append(int(card))

    # have to check if it is a face card and convert it back
    best_card = int(max(new_card_list))
    if (best_card > 9):
        best_card = list(face_cards.keys())[list(face_cards.values()).index(best_card)]
    return best_card

def hand_type(hand):
    """
    Takes a string representing the hand
    returns an int representing the hand type
    """

    # Since we don't have suits or straights a counter gives
    # an interpretation of the hand that is easy to classify
    hand_counter = Counter(hand)
    card_counts = sorted(hand_counter.values(), reverse=True)
    match card_counts:
        case [5]:
            hand_type = 7 #'Five of a kind'
        case [4,1]:
            hand_type = 6 #'Four of a kind'
        case [3,2]:
            hand_type = 5 #'Full house'
        case [3,1,1]:
            hand_type = 4 #'Three of a kind'
        case [2,2,1]:
            hand_type = 3 #'Two pair'
        case [2,1,1,1]:
            hand_type = 2 #'One pair'
        case [1,1,1,1,1]:
            hand_type = 1 #'High card'
        case _:
            print(card_counts)
            print(hand_counter)

    return hand_type

def encode_hand(hand):
    """
    Takes a string representing the hand
    returns a list of ints corresponding to the cards
    in the hand
    """
    encoded_card = []
    
    # J is now 1
    face_cards = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    for card in hand:
        if (card.isdigit()):
            encoded_card.append(int(card))
        else:
            encoded_card.append(face_cards[card])

    return encoded_card

file = open("day07_input1.txt","r")
data = file.read().splitlines()
score_data(data)