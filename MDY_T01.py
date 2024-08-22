import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return board[combination[0]]
    if " " not in board:
        return "Tie"
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_win(board)
    if result:
        if result == "X":
            return -10 + depth
        elif result == "O":
            return 10 - depth
        else:
            return 0
    if is_maximizing:
        best_score = -1000
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 1000
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def ai_move(board):
    best_score = -1000
    best_move = 0
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -1000, 1000)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

def play_game():
    board = [" "] * 9
    while True:
        print_board(board)
        move = input("Enter your move (1-9): ")
        board[int(move) - 1] = "X"
        result = check_win(board)
        if result:
            print_board(board)
            if result == "X":
                print("Human wins!")
            elif result == "O":
                print("AI wins!")
            else:
                print("Tie!")
            break
        ai_move(board)
        result = check_win(board)
        if result:
            print_board(board)
            if result == "X":
                print("Human wins!")
            elif result == "O":
                print("AI wins!")
            else:
                print("Tie!")
            break

play_game()