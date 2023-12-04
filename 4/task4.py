def calc_cards_points(input):
    sum = 0
    for line in input.splitlines():
        sum += calc_card_points(line)
    return sum

def calc_card_points(card):
    card = card.split(":")[1]
    card = card.split("|")
    winning_numbers = card[0].split()
    current_numbers = card[1].split()
    winning_numbers = [int(i) for i in winning_numbers]
    current_numbers = [int(i) for i in current_numbers]
    sum = 0
    for i in current_numbers:
        if i in winning_numbers:
            if sum == 0:
                sum += 1
            else:
                sum *= 2
    return sum

if __name__ == "__main__":
    with open("input") as f:
        print(calc_cards_points(f.read()))