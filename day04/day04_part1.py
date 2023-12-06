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


scores = []
for card in data:
    winning_numbers, your_numbers = process_card(card)
    matches = count_matches(winning_numbers, your_numbers)
    score = 0 if (matches == 0) else 2**(matches-1)
    scores.append(score)

print(scores)
print("Total points: " + str(sum(scores)))