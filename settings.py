from random import randint

class Board:
    '''
    This class creates a instance of the board with random values withing the range 100 - 550, calculates the rent for each one as 25%
    of the face value, sets the owner name to None and then builds the board as a dict object
    '''
    def __init__(self):
        self.board = self.create_board()
    
    def create_board(self):
        board = {}
        values = [randint(200, 550) for x in range(0, 20)]
        rent = [value*0.25 for value in values]
        zip_list = zip(values, rent)
        count = 1
        for item in zip_list:
            board[count] = {
                'value': item[0],
                'rent': item[1],
                'owner': None
            }
            count += 1
        return board


class Player:
    '''
    This class creates a instance of a player object with name, personality, initial cash, sets the 
    initial position as 1 and status to active
    '''
    def __init__(self, name, personality, start_cash):
        self.name = name
        self.personality = personality
        self.cash = start_cash
        self.position = 1
        self.spaces_owned = []
        self.status = 'active'

    def __str__(self):
        return self.name

