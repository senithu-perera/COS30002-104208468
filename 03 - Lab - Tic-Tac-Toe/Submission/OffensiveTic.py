import random

WIN_SET = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

def check_winner(board, player):
    return any(all(board[pos] == player for pos in win_set) for win_set in WIN_SET)

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def is_valid_move(move, board):
    return 1 <= move <= 9 and board[move - 1] == ' '

def get_available_moves(board):
    return [i + 1 for i, cell in enumerate(board) if cell == ' ']

def get_winning_move(board, player):
    for win_set in WIN_SET:
        count_player = win_set.count(player)
        count_empty = win_set.count(' ')
        if count_player == 2 and count_empty == 1:
            winning_move = next(move + 1 for move, cell in enumerate(win_set) if cell == ' ')
            return winning_move

    return None

def get_strategic_move(board):
    # Prefer center, corners, and then edges
    preferred_moves = [5, 1, 3, 7, 9, 2, 4, 6, 8]

    for move in preferred_moves:
        if move in get_available_moves(board):
            return move

def play_tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if not is_valid_move(move, board):
                print("Invalid move. Please try again.")
                continue
        else:
            print("AI is making a move...")
            winning_move = get_winning_move(board, 'O')
            blocking_move = get_winning_move(board, 'X')

            move = winning_move or blocking_move or get_strategic_move(board)

        board[move - 1] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == 'X':
                print("Player X wins!")
            else:
                print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
