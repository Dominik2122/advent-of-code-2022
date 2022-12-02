with open("./data.txt") as f:
    lines = f.readlines()


class Game:
    Rock = 0
    Scissors = 1
    Paper = 2

    @staticmethod
    def winning_pairs():
        return [(Game.Rock, Game.Paper), (Game.Paper, Game.Scissors), (Game.Scissors, Game.Rock)]

    @staticmethod
    def get_player_choice_points(choice):
        if choice == Game.Rock:
            return 1
        elif choice == Game.Paper:
            return 2
        else:
            return 3

    @staticmethod
    def get_battle_score(elf_choice, player_choice):
        if elf_choice == player_choice:
            return 3

        for pair in Game.winning_pairs():
            if elf_choice == pair[0] and player_choice == pair[1]:
                return 6
        return 0


elf_possible_choices = {
    'A': Game.Rock,
    'B': Game.Paper,
    'C': Game.Scissors
}

first_score = 0
for battle in lines:
    player_possible_choices = {
        'X': Game.Rock,
        'Y': Game.Paper,
        'Z': Game.Scissors,
    }
    elf_choice = elf_possible_choices[battle.split()[0]]
    player_choice = player_possible_choices[battle.split()[1]]
    first_score += Game.get_player_choice_points(player_choice)
    first_score += Game.get_battle_score(elf_choice, player_choice)
print(first_score)


def resolve_player_choice(elf_choice, required_result):
    if required_result == 'X':
        for pair in Game.winning_pairs():
            if elf_choice == pair[1]:
                return pair[0]

    if required_result == 'Y':
        return elf_choice

    if required_result == 'Z':
        for pair in Game.winning_pairs():
            if elf_choice == pair[0]:
                return pair[1]


second_score = 0
for battle in lines:
    elf_choice = elf_possible_choices[battle.split()[0]]
    result = battle.split()[1]
    player_choice = resolve_player_choice(elf_choice, result)
    second_score += Game.get_player_choice_points(player_choice)
    second_score += Game.get_battle_score(elf_choice, player_choice)
print(second_score)
