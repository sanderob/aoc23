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


def find_min_cubes(game_input):
    maxs = {
        "green": 0,
        "red": 0,
        "blue": 0
    }
    for round in game_input:
        for color, number in round.items():
            maxs[color] = max(maxs[color], number)
    return maxs


if __name__ == '__main__':
    with open("../resources/02.txt", "r") as f:
        lines = f.readlines()
        sum = 0
        for line in [line.strip() for line in lines]:
            game = interperet_line(line)
            maxs = find_min_cubes(game[1])
            c = 1
            for color in maxs.values():
                c *= color
            sum += c
        print(sum)
