max_values = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def interperet_line(s):
    parts = s.split(": ")
    game_number = int(parts[0].split(" ")[-1])
    rounds = parts[1].split("; ")
    rounds_list = []
    for round in rounds:
        colours = round.split(", ")
        round_map = {}
        for color in colours:
            l = color.split(" ")
            round_map[l[1]] = int(l[0])
        rounds_list.append(round_map)
    return game_number, rounds_list

def validate_game(game):
    for round in game:
        for color in round.keys():
            if round[color] > max_values[color]:
                return False
    return True

with open("./02.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in [line.strip() for line in lines]:
        game = interperet_line(line)
        if validate_game(game[1]):
            sum += game[0]
    print(sum)