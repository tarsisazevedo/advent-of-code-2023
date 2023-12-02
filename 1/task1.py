numbers_as_texts = {
    "one": "on1e",
    "two": "tw2o",
    "three": "th3ree",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "se7ven",
    "eight": "ei8ght",
    "nine": "ni9ne",
    "zero": "ze0ro",
}

def replace_numbers_as_texts(line, numbers_as_texts):
    for char in line:
        for k in numbers_as_texts.keys():
            if k.startswith(char) and k in line:
                line = line.replace(k, str(numbers_as_texts[k]))
                return replace_numbers_as_texts(line, numbers_as_texts)
    return line

def extract_numbers(line):
    line_numbers  = ""
    line = replace_numbers_as_texts(line, numbers_as_texts)
    for char in line:
        if char.isdigit():
            line_numbers += char
    return line_numbers
    
def find_numbers(input):
    numbers = []
    for line in input.splitlines():
        line_numbers = extract_numbers(line)
        if line_numbers:
            number = int(line_numbers[0]+line_numbers[-1]) 
            numbers.append(number)
    return sum(numbers)

if __name__ == "__main__":
    with open("input") as f:
        input = f.read()
        print(find_numbers(input))