import random

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if all(board[i + j] == player for j in range(3)) or \
           all(board[i // 3 + j * 3] == player for j in range(3)):
            return True
    if all(board[i] == player for i in [0, 4, 8]) or \
       all(board[i] == player for i in [2, 4, 6]):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def is_valid_move(move, board):
    return 1 <= move <= 9 and board[move - 1] == ' '

def get_available_moves(board):
    return [i + 1 for i, cell in enumerate(board) if cell == ' ']

def get_blocking_move(board, player):
    for win_set in WIN_SET:
        count_player = win_set.count(player)
        count_empty = win_set.count(' ')
        if count_player == 2 and count_empty == 1:
            blocking_move = [move for move in win_set if board[move - 1] == ' '][0]

            if is_valid_move(blocking_move, board):
                return blocking_move

    return None

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
            blocking_move = get_blocking_move(board, 'X')
            if blocking_move is not None:
                move = blocking_move
            else:
                available_moves = get_available_moves(board)
                move = random.choice(available_moves)

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

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    WIN_SET = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    )
    play_tic_tac_toe()
