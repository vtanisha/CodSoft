import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'  # Human is 'X', AI is 'O'

    def print_board(self):
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def is_valid_move(self, move):
        return self.board[move] == ' '

    def make_move(self, move):
        if self.is_valid_move(move):
            self.board[move] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for cond in win_conditions:
            if self.board[cond[0]] != ' ' and self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]]:
                return True
        return False

    def alphabeta(self, depth, is_maximizing, alpha, beta):
        if self.check_win():
            return -1 if is_maximizing else 1  # Fixed win scoring
        if ' ' not in self.board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if self.is_valid_move(i):
                    self.board[i] = 'X'  # Simulate 'X' move
                    score = self.alphabeta(depth + 1, False, alpha, beta)
                    self.board[i] = ' '  # Undo
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.is_valid_move(i):
                    self.board[i] = 'O'  # Simulate 'O' move
                    score = self.alphabeta(depth + 1, True, alpha, beta)
                    self.board[i] = ' '  # Undo
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return best_score

    def get_ai_move(self):
        best_score = float('inf')
        best_move = None
        for i in range(9):
            if self.is_valid_move(i):
                self.board[i] = 'O'  # Test 'O' move
                score = self.alphabeta(0, True, -float('inf'), float('inf'))
                self.board[i] = ' '  # Undo
                if score < best_score:  # AI minimizes score
                    best_score = score
                    best_move = i
        return best_move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':
                move = input("Your move (1-9): ")
                try:
                    move = int(move) - 1
                    if not self.make_move(move):
                        print("Invalid move! Try again.")
                        continue
                except ValueError:
                    print("Enter a number 1-9!")
                    continue
            else:
                print("AI thinking...")
                move = self.get_ai_move()
                self.make_move(move)
                print(f"AI plays {move + 1}")

            if self.check_win():
                self.print_board()
                winner = 'X' if self.current_player == 'O' else 'O'
                print(f"{'You' if winner == 'X' else 'AI'} wins!")
                break
            if ' ' not in self.board:
                self.print_board()
                print("It's a tie!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
