from sympy.solvers import solve
from sympy import Symbol, N
import math

file = open("day06_input1.txt","r")
data = file.read().splitlines()

def parse_data(data):
    """
    returns a list for times and distances
    """
    times = "".join(data[0].split(":")[1].strip().split())
    distances = "".join(data[1].split(":")[1].strip().split())

    times = int(times)
    distances = int(distances)
    return times, distances


def possible_wins(time, record_distance):
    """
    Calculate the race distance for all
    possible combos, returns the number of
    possible wins. More efficient
    """

    x = Symbol('x')
    sols = solve(x * (time - x) - record_distance, x)
    possible_wins = math.floor(N(sols[1])) - math.ceil(N(sols[0])) + 1
    return possible_wins

times, distances = parse_data(data)
possible_wins_per_game = possible_wins(times, distances)
print(possible_wins_per_game)