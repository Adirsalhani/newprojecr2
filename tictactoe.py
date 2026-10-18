import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # בדיקת שורות
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # בדיקת עמודות
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # בדיקת אלכסונים
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def get_user_move(board):
    while True:
        try:
            move = input("הכנס שורה ועמודה (לדוג' 1 2): ")
            row, col = map(int, move.strip().split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == ' ':
                return row-1, col-1
            else:
                print("מיקום לא חוקי, נסה שוב.")
        except Exception:
            print("קלט לא חוקי, נסה שוב.")

def get_computer_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty)

def main():
    print("ברוך הבא למשחק איקס עיגול!")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = "X"

    mode = input("הכנס 1 לשחק נגד מחשב, 2 לשני שחקנים: ").strip()
    against_computer = (mode == "1")

    while True:
        print_board(board)
        if current_player == "X" or not against_computer:
            print(f"תור השחקן {current_player}:")
            row, col = get_user_move(board)
        else:
            print("תור המחשב:")
            row, col = get_computer_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X" or not against_computer:
                print(f"כל הכבוד! השחקן {current_player} ניצח!")
            else:
                print("המחשב ניצח!")
            break

        if is_full(board):
            print_board(board)
            print("תיקו!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()