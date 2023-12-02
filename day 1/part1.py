"""
The newly-improved calibration document consists of lines of text; each line 
originally contained a specific calibration value that the Elves now need to 
recover. On each line, the calibration value can be found by combining the first
digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, 
and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the 
calibration values?
"""
# Read the input text file
with open('input.txt','r') as f:
    calibration_doc = f.read().split('\n')

# Removing an extra line made by the last newline character
calibration_doc = calibration_doc[:-1]
f.close()


def read_digits(string_with_digits):
    # Checks a string for digits and returns the
    # first and the last as an int
    digits = [char for char in string_with_digits if char.isdigit()]
    return int(digits[0] + digits[-1])

calibration_values = [read_digits(line) for line in calibration_doc]

sum(calibration_values)