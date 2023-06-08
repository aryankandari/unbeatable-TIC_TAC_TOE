import math
import random

class Player:
    def __init__(self,letter):
        self.letter = letter    #O or X

    #get all players get next move given a game
    def get_move(self,game):
        pass

class RandomPCPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class UserPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #check that this is the correct value by trying to cast it to integer and if not 
            #then we say invalid and if that spot is not available on the board then also invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
    
class GeniusPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) ==9:
            square = random.choice(game.available_moves())
            #random selection
        else:
            #using the mimimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter    #the user
        other_player = 'O' if player == 'X' else 'X'

        #
        if state.current_winner == other_player:
            #keep track of position and score for minimax to work
            return {'position': None,
                    'score': 1*(state.num_empty_squares()+1) if other_player == max_player else -1*(state.num_empty_squares()+1)
                    }

        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position':None, 'score': -math.inf}    #each score should maximize
        else:
            best = {'position':None, 'score': math.inf} #each score should minimize

        for possible_move in state.available_moves():
            #step1: make a move and try that spot
            state.make_move(possible_move, player)

            #step2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            #step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move    #otherwise this will get messed up 

            #step4: update the dictionaries if necessary
            if player == max_player:    #we are trying to maximise the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score    #replace best
            else:   #but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score    #replace best
        return best