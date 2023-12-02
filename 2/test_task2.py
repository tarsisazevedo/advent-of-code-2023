from task2 import (get_max_number_of_each_cube, get_power_from_cubes,
                   get_sum_of_all_game_powers, get_valid_lines, is_valid_game)


def test_valid_line():
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    expected = [1, 2, 5]
    valid_lines = get_valid_lines(input)
    assert valid_lines == expected

def test_valid_game():
    game = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert is_valid_game(game) == True

def test_get_max_number_of_each_cube():
    input = """3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"""
    expected = {"red": 4, "green": 2, "blue": 6}
    assert get_max_number_of_each_cube(input) == expected

def test_get_power_from_cubes():
    input = {"red": 4, "green": 2, "blue": 6}
    assert get_power_from_cubes(input) == 48

def test_get_sum_of_all_game_powers():
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    expected = 2286
    assert get_sum_of_all_game_powers(input) == expected