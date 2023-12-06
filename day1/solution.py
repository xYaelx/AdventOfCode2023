import re

DIGITS_MAP = {
    "oneight": '18',
    "twone": '21',
    "threeight": '38',
    "fiveight": '58',
    "sevenine": '79',
    "eightwo": '82',
    "nineight": '98',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}


def extract_first_and_last_digits(line):
    line = replace_words_with_digits(line)
    # Extract the first and last digits from a line and return as a string
    digits = re.findall(r'\d', line)
    return digits[0] + digits[-1] if digits else None


def replace_words_with_digits(line):
    for digit in DIGITS_MAP:
        line = line.replace(digit, DIGITS_MAP[digit])
    return line


def main():
    input_file = "input.txt"

    with open(input_file, 'r') as my_file:
        total_sum = sum(int(extract_first_and_last_digits(line.strip())) for line in my_file)

    print("Total sum:", total_sum)


if __name__ == "__main__":
    main()
