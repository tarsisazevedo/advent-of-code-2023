import re

rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_valid_game(game):
    """Return True if the game is valid, False otherwise."""
    subsets = game.split(";")
    for subset in subsets:
        cubes = subset.split(",")
        for cube in cubes:
            quantity, color = cube.strip().split(" ")
            if int(quantity) > rules[color]:
                return False
    return True

def get_valid_lines(input):
    """Return a list of line numbers that contain valid games."""
    valid_lines = []
    lines = input.splitlines()
    for i, line in enumerate(lines):
        game_id, game = line.split(":")
        game_id = re.search(r'\d+', game_id).group()
        if is_valid_game(game):
            valid_lines.append(int(game_id))
    return valid_lines

def get_max_number_of_each_cube(game):
    """Return a dictionary with the max number of each cube."""
    max_number_of_each_cube = {}
    subsets = game.split(";")
    for subset in subsets:
        cubes = subset.split(",")
        for cube in cubes:
            quantity, color = cube.strip().split(" ")
            max_number_of_each_cube[color] = max(max_number_of_each_cube.get(color, 0), int(quantity))
    return max_number_of_each_cube

def get_power_from_cubes(cubes):
    """Return the power from the cubes."""
    power = 1
    for _, quantity in cubes.items():
        power *= quantity
    return power

def get_sum_of_all_game_powers(input):
    powers = []
    lines = input.splitlines()
    for i, line in enumerate(lines):
        _, game = line.split(":")
        max_number_of_each_cube = get_max_number_of_each_cube(game)
        power = get_power_from_cubes(max_number_of_each_cube)
        powers.append(power)
    return sum(powers)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        valid_lines = get_valid_lines(input)
        print(sum(valid_lines))
        print(get_sum_of_all_game_powers(input))