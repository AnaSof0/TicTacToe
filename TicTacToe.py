from Board import Board
from player import Player

def TicTacToe():
    print('Welcome to TicTacToe!'+'\n')
    choice = int(input("Do you want to play against a friend(1) or an AIPlayer?(2)"))
    while (choice !=1 or choice!=2):
        choice = int(input("Do you wnat to play against a friend(1) or an AIPlayer?(2)"))
    if (choice==1):
        friend_play()
        
    
def friend_play():    
    P1= (input('Please enter the name of the first player: '))
    P2 = (input('Please enter the name of the second player: '))
    print()
    print('Welcome! '+'\n'+ P1+', you\'ll be X '+ ' \n'+P2+ ',you\'ll be O')
    p1=Player('X',P1)
    p2=Player('O',P2)
    print()
    b=Board()
    print(b)
    while True:
        if play(p1,b)==True:
            return b
        if play(p2,b)==True:
            return b
    

def play(p,b):
    print(p.name+"'s turn")
    row = int(input('what row?'))
    while (row<0 or row >2):
        row = int(input('what row?'))
    col = int(input('what column?'))
    while (col<0 or col >2):
        col = int(input('what column?'))
        
        
    checker = p.checker
    
    
    move=[checker,row,col]
    while (not b.isValid(move)):
        print("It appears that cell is already in use... try again:")
        row = int(input('what row?'))
        while (row<0 or row >2):
            row = int(input('what row?'))
        while (col<0 or col >2):
            col = int(input('what column?'))
        move=[checker,row,col]
        
    
    b.add_move(move)
    p.num_moves+=1
    print()
    print(b)
    if b.is_win(p.checker)== True:
        print(str(p) + " wins in " + str(p.num_moves) + " moves.")
        print("Congratulations!")
        return True
    elif b.is_win(p.checker) == False and b.is_full() == True:
        print ("It's a tie!")
        return True
    else:
        return False
    
    

    
    
    
    

