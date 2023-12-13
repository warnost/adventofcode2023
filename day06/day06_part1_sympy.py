from sympy.solvers import solve
from sympy import Symbol, N
import math

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
    possible wins. More Efficient
    """
    x = Symbol('x')
    sols = solve(x * (time - x) - record_distance, x)
    possible_wins = math.floor(N(sols[1])) - math.ceil(N(sols[0])) + 1
    return possible_wins

    return possible_wins

times, distances = parse_data(data)
possible_wins_per_game = []
for i in range(len(times)):
    possible_wins_per_game.append(possible_wins(times[i], distances[i]))
print(possible_wins_per_game)


print(math.prod(possible_wins_per_game))