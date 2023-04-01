class TicTacToe:
    def __init__(self):
        self.board = [" "]*9
        self.players = {}
        self.current_player = "X"
    
    def update_player_info(self, first_player, second_player):
        if first_player:
            self.players[first_player] = 0
        else:
            self.players["X"] = 0

        if second_player:
            self.players[second_player] = 0
        else:
            self.players["0"] = 0

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
    
    def display_scores(self):
        print("Score:")
        for player, score in self.players.items():
            print(f"{player}: {score}")
    
    def get_move(self):
        while True:
            move = input(f"{self.current_player}'s turn. Enter a number (1-9) to place your mark: ")
            if move.isdigit() and int(move) in range(1, 10) and self.board[int(move)-1] == " ":
                return int(move)-1
    
    def make_move(self, move):
        self.board[move] = self.current_player
    
    def check_win(self):
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != " ":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False
    
    def check_tie(self):
        return " " not in self.board
    
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
    
    def update_scores(self):
        if self.check_win():
            self.players[self.current_player] += 1
    
    def play(self):
        print("Welcome to Tic Tac Toe!")

        # Collect info
        print("Collecting players information...")
        first_player = input(f"Provide first player name: ")
        second_player = input(f"Provide second player name: ")
        self.update_player_info(first_player, second_player)

        # Start the game
        while True:
            self.display_scores()
            self.display_board()
            move = self.get_move()
            self.make_move(move)
            if self.check_win():
                self.display_board()
                print(f"{self.current_player} wins!")
                self.update_scores()
                break
            elif self.check_tie():
                self.display_board()
                print("It's a tie!")
                break
            else:
                self.switch_player()

def main():
    game = TicTacToe()
    game.play()

if __name__ == "__main__":
    main()
