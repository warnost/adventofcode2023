from collections import Counter

file = open("day07_input1.txt","r")
data = file.read().splitlines()

data

def parse_data(data):
    hands = []
    for row in data:
        hand = row.split()
        hand[1] = int(hand[1])
        hands.append(hand)
    return hands

def hand_type(hand):
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

    encoded_card = [hand_type]
    face_cards = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    for card in hand:
        if (card.isdigit()):
            encoded_card.append(int(card))
        else:
            encoded_card.append(face_cards[card])

    return encoded_card

def score_hands(hands):
    return sum([hand[1] * hand[3] for hand in hands])

def score_data(data):
    hands = parse_data(data)
    for hand in hands:
        hand.append(hand_type(hand[0]))


    hands = sorted(hands, key= lambda x: x[2], reverse=True)
    ranks = list(range(1, len(hands)+1))
    ranks = sorted(ranks, reverse=True)

    for i, hand in enumerate(hands):
        hand.append(ranks[i])

    print(sum([hand[1] * hand[3] for hand in hands]))

score_data(data)