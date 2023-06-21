from utils.fileio import readFile


def get_rounds(input_str: str) -> list:
    return [round.split(' ') for round in input_str.split()]


def get_round_result(round: list) -> int:
    moves = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'
    }

    move_score = {'rock': 1, 'paper': 2, 'scissors': 3}

    opponent_move = moves[round[0]]
    print(opponent_move)
    player_move = moves[round[1]]
    print(player_move)

    if (opponent_move == player_move):
        return move_score[player_move] + 3
    elif (opponent_move == 'rock' and player_move == 'scissors') or (opponent_move == 'scissors' and player_move == 'paper') or (opponent_move == 'paper' and player_move == 'rock'):
        return move_score[player_move]
    else:
        return move_score[player_move] + 6


# *slaps roof of method* This puppy can fit so many returns in it
def get_move_to_play(round: list) -> int:
    opponent_moves = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
    }
    move_scores = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    outcomes = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
    }

    if (round[1] == 'X'):
        if (round[0] == 'A'):
            return move_scores['scissors']
        elif (round[0] == 'B'):
            return move_scores['rock']
        else:
            return move_scores['paper']
    elif (round[1] == 'Y'):
        if (round[0] == 'A'):
            return move_scores['rock'] + 3
        elif (round[0] == 'B'):
            return move_scores['paper'] + 3
        else:
            return move_scores['scissors'] + 3
    else:
        if (round[0] == 'A'):
            return move_scores['paper'] + 6
        elif (round[0] == 'B'):
            return move_scores['scissors'] + 6
        else:
            return move_scores['rock'] + 6


def get_score(rounds: list) -> int:
    score = 0
    for round in rounds:
        score += get_round_result(round)
    return score


def get_score_on_move_to_play(rounds: list) -> int:
    score = 0
    for round in rounds:
        score += get_move_to_play(round)
    return score


def main():
    input_str = readFile('input.txt')
    rounds = get_rounds(input_str)
    # print(rounds)
    score = get_score(rounds)
    print(score)
    score_on_move_to_play = get_score_on_move_to_play(rounds)
    print(score_on_move_to_play)


if __name__ == '__main__':
    main()
