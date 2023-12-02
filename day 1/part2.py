"""
--- Part Two ---

"""
# Read the input text file
with open('input.txt','r') as f:
    calibration_doc = f.read().split('\n')

# Removing an extra line made by the last newline character
calibration_doc = calibration_doc[:-1]
f.close()

# test case from the problem
test_doc = ['two1nine', 'eightwothree', 'abcone2threexyz','xtwone3four',
            '4nineeightseven2','zoneight234','7pqrstsixteen']

def read_digits(string_with_digits):
    # Checks a string for digits and returns the
    # first and the last as an int
    first_digit_index = len(string_with_digits)
    first_digit = None
    last_digit_index = -1
    last_digit = None

    number_words = ["one","two","three","four","five","six","seven","eight","nine"]
    for i, word in enumerate(number_words):

        # Looking for the words first
        first_idx = string_with_digits.find(word)
        last_idx = string_with_digits.rfind(word)
        if (first_idx < first_digit_index and first_idx >= 0):
          first_digit_index = first_idx
          first_digit = str(i+1)
        if (last_idx > last_digit_index and last_idx >= 0):
          last_digit_index = last_idx
          last_digit = str(i+1)

        # Then the numbers
        first_idx = string_with_digits.find(str(i+1))
        last_idx = string_with_digits.rfind(str(i+1))
        if (first_idx < first_digit_index and first_idx >= 0):
          first_digit_index = first_idx
          first_digit = str(i+1)
        if (last_idx > last_digit_index and last_idx >= 0):
          last_digit_index = last_idx
          last_digit = str(i+1)

    return int(first_digit + last_digit)

def score_doc(doc):
    """
    Calculate the score for a document
    """
    calibration_values = [read_digits(line) for line in doc]
    return sum(calibration_values)

print(score_doc(test_doc))
print(score_doc(calibration_doc))