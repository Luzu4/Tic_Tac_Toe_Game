# Clear Map For New Game
def clean_map():
    empty_map = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
    return empty_map


# Show map with players moves
def show_map_with_xo(game_map):
    print(f'   C1  C2  C3\n'
          f'R1 {game_map[0][0]} | {game_map[0][1]} | {game_map[0][2]} \n'
          f'  ---|---|---\n'      
          f'R2 {game_map[1][0]} | {game_map[1][1]} | {game_map[1][2]} \n'
          f'  ---|---|---\n'
          f'R3 {game_map[2][0]} | {game_map[2][1]} | {game_map[2][2]} ')


# Win conditions
def check_for_winner(game_map, player):
    if ((game_map[0][0] == game_map[1][0] == game_map[2][0] != ' ') or
        (game_map[0][1] == game_map[1][1] == game_map[2][1] != ' ') or
        (game_map[0][2] == game_map[1][2] == game_map[2][2] != ' ') or
        (game_map[0][0] == game_map[0][1] == game_map[0][2] != ' ') or
        (game_map[1][0] == game_map[1][1] == game_map[1][2] != ' ') or
        (game_map[2][0] == game_map[2][1] == game_map[2][2] != ' ') or
        (game_map[0][0] == game_map[1][1] == game_map[2][2] != ' ') or
        (game_map[2][0] == game_map[1][1] == game_map[0][2] != ' ')):
        print(f'Congratulations {player} WIN!!')
        win = True
        return win


# Ask player to move and check if the input is correct.
def player_move(map_before_move, player):
    correct = False
    while not correct:
        cell = input(f'{player} - Where do you want to put a sign?("R1C1"): ')
        try:
            if 0 < int(cell[1]) < 4 and 0 < int(cell[3]) < 4:
                if map_before_move[int(cell[1]) - 1][int(cell[3]) - 1] == ' ':
                    if player == 'Player One':
                        map_before_move[int(cell[1]) - 1][int(cell[3]) - 1] = 'X'
                        return map_before_move
                    elif player == 'Player Two':
                        map_before_move[int(cell[1]) - 1][int(cell[3]) - 1] = '0'
                        return map_before_move
                    correct = True
                else:
                    print('You need to pick EMPTY cell, Try one more time. ')
            else:
                print('Wrong cell index, Try one more time.')
        except ValueError:
            print('Wrong cell index, Try one more time.')


def main():
    user_want_to_play = input(print('Hey, You want to play Tic Tac Toe Game?(Y/N): '))
    while user_want_to_play.upper() == 'Y':
        tic_tac_toe_map = clean_map()
        show_map_with_xo(tic_tac_toe_map)
        while True:
            tic_tac_toe_map = player_move(tic_tac_toe_map, 'Player One')
            show_map_with_xo(tic_tac_toe_map)
            winner = check_for_winner(tic_tac_toe_map, 'Player One')
            if winner:
                break
            tic_tac_toe_map = player_move(tic_tac_toe_map, 'Player Two')
            show_map_with_xo(tic_tac_toe_map)
            winner = check_for_winner(tic_tac_toe_map, 'Player Two')
            if winner:
                break

        user_want_to_play = input('You one to play one more time?(Y/N): ')


if __name__ == '__main__':
    main()
