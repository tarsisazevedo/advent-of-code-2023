import re
from collections import defaultdict


def has_adjacent_symbol(index, last_index, indexes_of_symbols, line_index):
    """Return True if there is a symbol adjacent to the number."""

    index_inline = (index - 1 in indexes_of_symbols.get(line_index, []) 
        or last_index + 1 in indexes_of_symbols.get(line_index, []))
    index_previous_line = [True if i in indexes_of_symbols.get(line_index - 1, []) else False for i in range(index - 1 , last_index + 2)]
    index_next_line = [True if i in indexes_of_symbols.get(line_index + 1, []) else False for i in range(index - 1 , last_index + 2)]
    # index_next_line = (
    #     (index - 1 in indexes_of_symbols.get(line_index + 1, []) 
    #     or last_index + 1 in indexes_of_symbols.get(line_index + 1, []))
    #     or (index in indexes_of_symbols.get(line_index + 1 , [])
    #     or last_index in indexes_of_symbols.get(line_index + 1, []))
    # )
    return index_inline or bool(sum(index_previous_line)) or bool(sum(index_next_line))

def sum_numbers_adjacent_to_symbol(input):
    """Return the sum of all numbers adjacent to the symbol $ in the input string."""
    indexes_of_symbols = find_all_index_of_symbols(input)
    summup = [] 
    for i, line in enumerate(input.splitlines()):
        numbers = re.finditer(r'\d+', line)
        for match in numbers:
            index = match.start()
            last_index = match.end() - 1
            if has_adjacent_symbol(index, last_index, indexes_of_symbols, i):
                summup.append(int(match.group(0)))
    return sum(summup)

def find_all_index_of_symbols(input):
    """Return a dictionary of all indexes of symbols in the input string."""
    indexes_of_symbols = defaultdict(list)
    symbols = []
    for i, line in enumerate(input.splitlines()):
        for j, symbol in enumerate(line):
            if not symbol.isdigit() and symbol != '.':
                symbols.append(symbol)
                indexes_of_symbols[i].append(j)
    return indexes_of_symbols

if __name__ == '__main__':
    with open('input') as f:
        input = f.read()
        print(sum_numbers_adjacent_to_symbol(input))