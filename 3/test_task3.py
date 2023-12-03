from task3 import (find_all_index_of_symbols, has_adjacent_symbol,
                   sum_numbers_adjacent_to_symbol)


def test_sum_numbers_adjacent_to_symbol():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert sum_numbers_adjacent_to_symbol(input) == 4361

def test_find_all_index_of_symbols():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    expected = {1: [3], 3: [6], 4: [3], 5: [5], 8: [3, 5]}
    assert find_all_index_of_symbols(input) == expected

def test_has_adjacent_symbols():
    indexes_of_symbols = {1: [3], 3: [6], 4: [3], 5: [5], 8: [3, 5]}
    assert has_adjacent_symbol(0, 2, indexes_of_symbols, 0) == True
    assert has_adjacent_symbol(5, 7, indexes_of_symbols, 0) == False
    assert has_adjacent_symbol(2, 3, indexes_of_symbols, 2) == True
    assert has_adjacent_symbol(6, 8, indexes_of_symbols, 2) == True
    assert has_adjacent_symbol(0, 2, indexes_of_symbols, 4) == True
    assert has_adjacent_symbol(7, 8, indexes_of_symbols, 5) == False
    assert has_adjacent_symbol(2, 4, indexes_of_symbols, 6) == True
    assert has_adjacent_symbol(6, 8, indexes_of_symbols, 7) == True
    assert has_adjacent_symbol(1, 3, indexes_of_symbols, 9) == True
    assert has_adjacent_symbol(5, 7, indexes_of_symbols, 9) == True

def test_has_adjacent_symbol_in_the_middle():
    input = """.............554.........740...
........556...*....196........."""
    indexes_of_symbols = find_all_index_of_symbols(input)
    assert has_adjacent_symbol(13, 15, indexes_of_symbols, 0) == True

def test_numbers_at_end_of_line():
    input = """..10.40
......*"""
    assert sum_numbers_adjacent_to_symbol(input) == 40