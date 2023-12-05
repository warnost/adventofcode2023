"""
This problem reminds me of a convolutional network.
A filter sliding over the data should capture which
parts have symbols nearby. I am thinking flatten
the schematic and then use a regex match.

pad + flatten
search for digits
slice surrounding
search slices for symbols
if found add to part list.
"""
import re

file = open("day03_input1.txt","r")
data = file.read().splitlines()

def flatten_data(data):
    """
    This function is going to take
    our 2D schematic and make it 1D
    to make searching less complicated.

    We also need to pad it so we don't 
    get index out of bounds or transition
    to a new line by accident.
    """

    w = len(data[0]) + 2

    padded_data = [" " + line + " " for line in data]
    padded_data.insert(0, " " * w)
    padded_data.append(" " * w)

    flat_data = ''.join(padded_data)

    return flat_data, w

def find_valid_nums(data, w, part_num_length):
    """
    This function slices the flattened data 
    looking for consecutive digits of part_num_length.

    If it finds digits of that length it then looks
    in the surrounding space for a symbol. w, the 
    width of the original data plus two, helps locate
    the surrounding characters in the flattened data.
    """
    valid_part_nums = []
    invalid_nums = []
    for index in range(len(data) - 2*(w+1)):
        # Slice out a piece that is part_num_length long
        # This is a sliding window
        start = w+index+1
        end = w+index+1+(part_num_length)
        txt = data[start:end]
        

        # If that is a number, check the surrounding
        # Text for symbols. Using math to slice
        # out the appropriate characters from the
        # flattened data
        if (txt.isdigit()):
            part1 = data[(start - 1 - w): (end + 1 - w)]
            part2 = data[start - 1: start]
            part3 = data[end: end+1]
            part4 = data[start - 1 + w: end + 1 + w]
            search_txt = part1 + part2 + part3 + part4

            # Tracking the full indicies will make locating the gear easier
            part1_idx = [i for i in range((start - 1 - w), (end + 1 - w))]
            part2_idx = [i for i in range(start - 1, start)]
            part3_idx = [i for i in range(end, end+1)]
            part4_idx = [i for i in range(start - 1 + w, end + 1 + w)]
            search_idx = part1_idx + part2_idx + part3_idx + part4_idx

            # First regex is looking for anything not a letter,
            # number, period, or space. Second is also checking 
            # that there is no digit. Added search for * in part 2
            # to look for possible gears
            if (bool(re.search("[^a-zA-Z0-9.\\s]", search_txt)) & 
               (not bool(re.search("\\d", search_txt)))):
                part_num = int(txt)
                
                # Looking for "*" and noting its location
                gear_search = re.search("[\\*]", search_txt)
                if bool(gear_search):
                    loc = gear_search.span()
                    gear_loc = search_idx[loc[0]:loc[1]][0]
                else:
                    gear_loc = -1
                  
                valid_part_nums.append([part_num, gear_loc])

                #For Debugging
                #print(part1 + part2 + "|" + txt + "|" + part3 + part4)
            else:
                # Mostly for debugging
                invalid_nums.append(int(txt))
    # For Debugging
    # print(invalid_nums)
    return valid_part_nums

"""
Start by flattening the data and creating a placeholder
"""

flat_data, w = flatten_data(data)
all_part_nums = []

"""
The search function I built depends on the length of the digits
We search for. Part numbers are up to 3 digits in length, so
I need to run the search 3 times.

This is not efficient, I am searching the same area of the schematic
multiple times.
"""
for part_num_length in [3,2,1]:
    good_parts = find_valid_nums(flat_data, w, part_num_length)
    all_part_nums += good_parts

"""
Now we have all the part numbers and gear locations. I can
reverse that to make a dictonary of gear locations and the
adjacent parts. Then check if each gear has exactly 2
adjacent parts then compute the gear ratio.
"""
from collections import defaultdict 
possible_gears = [pair for pair in all_part_nums if pair[1] > -1]
gear_dict = defaultdict(list)
for gear in possible_gears:
    gear_dict[gear[1]].append(gear[0])

sum_of_gear_ratios = 0
for key in gear_dict:
    if (len(gear_dict[key]) == 2):
       gear_ratio = gear_dict[key][0] * gear_dict[key][1] 
       sum_of_gear_ratios += gear_ratio
    
# Final Answer
sum_of_gear_ratios