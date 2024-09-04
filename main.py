# creating board
class Board:
    def __init__(self):
        self.board =    [" ", " ", " ",
                        " ", " ", " ",
                        " ", " ", " "]

    def print_board(self):
        print('\n')
        print(" " + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print("-----------")
        print(" " + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print("-----------")
        print(" " + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        print('')
        
    def update_board(self, position, symbol):

            if self.board[position - 1] == " ":
                self.board[position -1] = symbol
                return True
        
            else:
                print("Position already taken. Select another position.")
                return False
        
    def check_winner(self, symbol):
        if  (self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol) or \
            (self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol) or \
            (self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol) or \
            (self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol) or \
            (self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol) or \
            (self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol) or \
            (self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol) or \
            (self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol):
            return True
        else:
            return False
        
    def check_draw(self):
        if " " not in self.board:
            return True
        else:
            return False
        
# player class to get symbol and name
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = self.get_name()
        
    def get_name(self):
        if self.symbol == "X" :
            name = input("Enter name for player 'X': ")
        else:
            name = input("Enter name for player 'O': ")
        return name

# game objects for board and players
class Game:
    def __init__(self):
        
        self.board = Board()
        
        self.player1 = Player("X")
        self.player2 = Player("O")
        
        self.current_player = self.player1

    def play(self):
        while True:
            try:
                message = f"{self.current_player.name}, enter position (1 - 9): "
                position = int(input(message))

                if self.board.update_board(position, self.current_player.symbol):
                        self.board.print_board()
                        
                        if self.board.check_winner(self.current_player.symbol):
                            print(f"\n{self.current_player.name}, wins the round!\n")
                            break
                        
                        elif self.board.check_draw():
                            print(f"This round is a draw.")
                            break
                        
                        else:
                            if self.current_player == self.player1:
                                self.current_player = self.player2
                            else:
                                self.current_player = self.player1
            except:
                print(f"\nInvalid input. Enter a number between 1 and 9.")

# initialize game loop
while True:
    game = Game()
    game.play()
    
    replay = input(f"Do you want to play another round? (Enter 'y' for yes or any key to quit): ")
    
    if replay != "y":
        print(f"\nThanks for playing! See you again.\n")
        break