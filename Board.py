# Tic Tac Toe Board class
class Board:
    """ a data type for a Tic Tac Toe board"""

    def __init__(self):
        """ Initialize the board to be 3x3"""
        self.height = 3
        self.width=3
        self.slots= [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """returns string representation of the board"""
        s=''
        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
            
        for col in range(self.width):
            s += '--'
        s += '\n'
        return s 
        
        
    
    def isValid (self,move):
        row = move[1]
        col = move[2]
        if self.slots[row][col] == ' ':
            return True
        else:
            return False
    
    def add_move(self,move):
        """ adds the player's move (X or O) to the specified place"""
        row = move[1]
        col = move[2]
        checker = move[0]
        assert (checker =='X' or checker =='O')
        assert(col>=0 and col<=3 and row>=0 and row<=3)
        self.slots[row][col]= checker

        
    def clean_board(self):
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
                
    def is_diagonal_win(self,checker):
        if self.slots[0][0] ==checker\
        and self.slots[1][1] == checker \
        and self.slots[2][2] == checker:
            return True
        if self.slots[0][2] ==checker\
        and self.slots[1][1] == checker \
        and self.slots[2][0] == checker:
            return True
        return False
    
    def is_horizontal_win(self,checker):
        for row in range(self.height):
            if self.slots[row][0]==checker:
                if self.slots[row][1] == checker and self.slots[row][2]==checker:
                    return True
        return False
    
    def is_vertical_win(self,checker):
        for col in range(self.width):
            if self.slots[0][col]==checker:
                if self.slots[1][col] == checker and self.slots[2][col]==checker:
                    return True
        return False
    
    def is_win(self,checker):
        if self.is_diagonal_win(checker) or self.is_horizontal_win(checker) or self.is_vertical_win(checker):
            return True
        return False
    
    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col]==' ':
                    return False
        return True
        
    
                


        
        

                
        

