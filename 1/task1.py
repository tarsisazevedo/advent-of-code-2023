numbers_as_texts = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

def replace_numbers_as_texts(line, numbers_as_texts):
    for char in line:
        for k in numbers_as_texts.keys():
            if k.startswith(char) and k in line:
                line = line.replace(k, str(numbers_as_texts[k]))
                return replace_numbers_as_texts(line, numbers_as_texts)
    return line

def find_numbers(input):
    numbers = []
    for line in input.splitlines():
        line_numbers  = ""
        line = replace_numbers_as_texts(line, numbers_as_texts)
        for char in line:
            if char.isdigit():
                line_numbers += char
        if line_numbers:
            number = int(line_numbers[0]+line_numbers[-1]) 
            numbers.append(number)
    return sum(numbers)

if __name__ == "__main__":
    with open("input") as f:
        input = f.read()
        print(find_numbers(input))