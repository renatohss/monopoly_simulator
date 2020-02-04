from settings import Player, Board
from random import randint
from pprint import pprint
import operator

def roll_d6():
    return randint(1, 6)


def buy_space(board, player):
    index = player.position
    board[index]['owner'] = player
    player.spaces_owned.append(index)
    player.cash -= board[index]['value']


def pay_rent(board, player):
    index = player.position
    player.cash -= board[index]['rent']
    board[index]['owner'].cash += board[index]['rent']


def check_status(player):
    if player.cash >= 0:
        return True
    else:
        return False



def start_game(max_rounds):
    board = Board().board
    players = {
        1: Player('player1', 'impulsive', 300),
        2: Player('player2', 'demanding', 300),
        3: Player('player3', 'cautious', 300),
        4: Player('player4', 'random', 300)
    }

    _round = 1
    active_players = len(players)
        
    while _round <= max_rounds:
        for num, current_player in players.items():
            if current_player.status == 'active':
                dice = roll_d6()
                position = current_player.position + dice
                if position > 20:
                    current_player.cash += 100
                    current_player.position = 1
                else:
                    current_player.position = position
                board_space = board[current_player.position]

                if not board_space['owner']:
                    if current_player.personality == 'impulsive':
                        if current_player.cash > board_space['value']:
                            buy_space(board, current_player)

                    elif current_player.personality == 'demanding':
                        if board_space['rent'] > 50 and current_player.cash > board_space['value']:
                            buy_space(board, current_player)

                    elif current_player.personality == 'cautious':
                        if (current_player.cash - board_space['value']) > 80:
                            buy_space(board, current_player)

                    else:
                        if randint(1,2) == 1 and current_player.cash > board_space['value']:
                            buy_space(board, current_player)

                else:
                    pay_rent(board, current_player)

                status = check_status(current_player)
                if not status:
                    for num in current_player.spaces_owned:
                        board[num]['owner'] = None
                    current_player.spaces_owned = []
                    current_player.status = 'game_over'
                    active_players -= 1

        if active_players == 1:
            break

        _round += 1
        
    winner = [players[index] for index in players if players[index].status == 'active']
    return {
        'winner': winner,
        'total_rounds': _round,
        'timeout': True if _round >= max_rounds else False
    }
    
    
def main():
    win_count = {
        'player1': [0],
        'player2': [0],
        'player3': [0],
        'player4': [0]
    }

    total_rounds = 0
    total_sims = 300
    total_timeout = 0
    max_rounds = 1000

    count = 1

    print(f'Maximum number of rounds before timeout: {max_rounds}')
    print(f'Running {total_sims} simulations...')

    while count <= total_sims:
        payload = start_game(max_rounds)
        for player in payload['winner']:
            win_count[player.name][0] += 1
            win_count[player.name].append(player.personality)
        total_rounds += payload['total_rounds']
        if payload['timeout']:
            total_timeout += 1
        count += 1

    max_win = 0
    max_player = ''
    for player, win in win_count.items():
        if win[0] > max_win:
            max_win = win[0]
            max_player = player

    print(f'\nResults:')
    print(f'Avg. Rounds: {round(total_rounds/total_sims, 2)}')
    print(f'Total of matches ending with timeout: {total_timeout}')
    print(f'Percentage of victory:\n \
            {win_count["player1"][1]}: {round((win_count["player1"][0]/total_sims)*100, 2)}%\n \
            {win_count["player2"][1]}: {round((win_count["player2"][0]/total_sims)*100, 2)}%\n \
            {win_count["player3"][1]}: {round((win_count["player3"][0]/total_sims)*100, 2)}%\n \
            {win_count["player4"][1]}: {round((win_count["player4"][0]/total_sims)*100, 2)}%\n')
    print(f'{max_player} ({win_count[max_player][1]}) won most times, with {max_win} victories')
            

if __name__ == "__main__":
    main()
