from player import UserPlayer, RandomPCPlayer, GeniusPlayer
import time 

class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    #single list to represent 3x3 board
        self.current_winner = None #track of current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     #['x','x','o'] --> [(0,'x'), (1,'x'), (2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #if valid move then make the move else return false
        if self.board[square] ==' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #if 3 in a row anywhere then player is a winner
        #first check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind +1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonal
        #only if the square in even number as only two moves are possible
        if square %2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]    #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]    #right to left diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

        #if all of these fail 
        return False
            

def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game or none for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #starting letter

    while game.empty_squares():
        #get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('') #empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            #after the move has been made we need to alternate the letter

            letter = 'O' if letter == 'X' else 'X' #switches player 

        time.sleep(1)

    if print_game:
        print("It\'s a TIE!")

if __name__ == '__main__':
    x_player = UserPlayer('X')
    # o_player = RandomPCPlayer('O')
    o_player = GeniusPlayer('O')
    t = tictactoe()
    play(t, x_player, o_player, print_game=True)