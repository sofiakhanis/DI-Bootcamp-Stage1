def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print(" - " * 3)
    print("\n")

def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):  # строка
            return True
        if all(board[j][i] == player for j in range(3)):  # столбец
            return True

    # Диагонали
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def main():
    # Пустое поле
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to the tic tac toe game! Quick rules: each player choose if he wants to play as 'X' or 'O'. The one who get three symbols in a row is a winner. Good luck!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, please enter the row (0-2): "))
            col = int(input(f"Player {current_player}, please enter the column (0-2): "))

            if board[row][col] != " ":
                print("You can't put your symbol here. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"Congrats! The player {current_player} wins!")
                break

            if is_draw(board):
                print("A tie!")
                break

            # Смена игрока
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Wrong input. Choose numbers from 0 to 2.")

if __name__ == "__main__":
    main()
