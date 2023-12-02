from task1 import find_numbers, replace_numbers_as_texts


def test_find_numbers():
    input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
    numbers_summed = find_numbers(input)
    assert numbers_summed == 142

def test_find_numbers_as_text():
    input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    numbers_summed = find_numbers(input)
    assert numbers_summed == 281

def test_replace_numbers_as_texts():
    line = "two1nine"
    numbers_as_texts = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    line = replace_numbers_as_texts(line, numbers_as_texts)
    assert line == "219"

def test_replace_numbers_as_texts_with_lower_wrong_number():
    line = "eightwothree"
    numbers_as_texts = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    line = replace_numbers_as_texts(line, numbers_as_texts)
    assert line == "8wo3"