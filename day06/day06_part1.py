file = open("day06_input1.txt","r")
data = file.read().splitlines()

def parse_data(data):
    """
    returns a list for times and distances
    """
    times = data[0].split(":")[1].strip().split()
    distances = data[1].split(":")[1].strip().split()

    times = [int(x) for x in times]
    distances = [int(x) for x in distances]
    return times, distances

def possible_wins(time, record_distance):
    """
    Calculate the race distance for all
    possible combos, returns the number of
    possible wins. Not particularly
    efficient
    """
    possible_wins = 0
    for i in range(time):
        your_distance = i * (time - i)
        if (your_distance > record_distance):
            possible_wins += 1

    return possible_wins

times, distances = parse_data(data)
possible_wins_per_game = []
for i in range(len(times)):
    possible_wins_per_game.append(possible_wins(times[i], distances[i]))
print(possible_wins_per_game)

import math
print(math.prod(possible_wins_per_game))