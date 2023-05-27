
class Player:
    
    def __init__(self,checker,name):
        assert(checker=='X' or checker == 'O')
        self.checker=checker
        self.name=name
        self.num_moves=0
    
    def __repr__(self):
        """
            returns a string representing a Player object.
        """
        s = "Player " + self.name+' '+ self.checker
        return s
    
    def opponent_checker(self):
        """
            returns a one-character string representing the checker of 
            the Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    

            
