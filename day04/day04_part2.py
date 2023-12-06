file = open("day04_input1.txt","r")
data = file.read().splitlines()


def process_card(card):
    num_lists = card.split(":")[1].split("|")
    winning_numbers = num_lists[0].strip().split()
    winning_numbers.sort()

    your_numbers = num_lists[1].strip().split()
    your_numbers.sort()
    return winning_numbers, your_numbers

def count_matches(winning_numbers, your_numbers):
    matches = 0
    for winning_num in winning_numbers:
        for your_num in your_numbers:
            if (winning_num == your_num):
                matches += 1
    return matches

from collections import Counter
total_cards = len(data)
card_counter = Counter(list(range(1,total_cards+1)))

for card_num, card in enumerate(data, start=1):
    winning_numbers, your_numbers = process_card(card)
    matches = count_matches(winning_numbers, your_numbers)

    if ((matches > 0) & (card_num < total_cards)):

        # making a list of copies I will add to each match. Must account
        # for going beyond the total number of cards
        copies = [card_counter[card_num]] * min(matches, total_cards - card_num)

        # List of cards to update. Need to account for not updating past the 
        # last card
        cards2update = list(range(card_num + 1, min(card_num + matches + 1, total_cards) + 1))
        card_counter.update(dict(zip(cards2update, copies)))

print("Total cards: " + str(sum(card_counter.values())))