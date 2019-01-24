# Write a Sodoku valid move checker (https://en.wikipedia.org/wiki/Sudoku)

# This checker should be able to be given the current board state 
#    and a potential move and return a boolean of whether the move is valid
#    
# 9X9 
# number unique for a row, column and 3x3 region 


# Assuming rows (y) is 1-9
# Assuming cols (x) is 1-9

current_board_state = []

class SudokuBox:
    def __init__(self):
        
        self.box=[
            [10,10,10],
            [10,10,10],
            [10,10,10],
        ]
    
    def is_blank(self,x,y):
        if self.box[y][x]==10:
            return True
        else:
            return False
        
    def has_number(self,num):
        for line in self.box:
            if num in line:
                return True
        return False
    def return_box(self):
        #this is returning
        return self.box
    
    def make_play(self, number, x, y):
        #not allowed to have an x or y >3
        self.box[y-1][x-1]=number
        
    def check_row(self,number,y):
        if number in self.box[y-1]:
            return True
        return False
    
    def check_col(self,number,x):
        for i in self.box:
            if i[x-1]==number:
                return True
        return False
        

class SudokuBoard:
    def __init__(self):
        self.board=[[],
                    [],
                    []]
        
        for y in range(3):
            for x in range (3):
                self.board[y].append(SudokuBox())
            
    def return_board(self):
        
        for i in self.board:
            for j in i:
                #this is printing
                print(j.return_box())
    
    def make_play(self,number, x, y):
        x=x-1
        y=y-1
        
        if y in range(0,3):
            if x in range(0,3):
                
                self.board[0][0].make_play(number,x,y)
            if x in range(3,6):
                self.board[0][1].make_play(number,x-3,y)
            if x in range(6,9):
                self.board[0][2].make_play(number, x-6,y)
                
        if y in range(3,6):
            if x in range(0,3):
                self.board[1][0].make_play(number,x,y-3)
            if x in range(3,6):
                self.board[1][1].make_play(number,x-3,y-3)
            if x in range(6,9):
                self.board[1][2].make_play(number, x-6,y-3)
                
        if y in range(6,9):
            if x in range(0,3):
                self.board[2][0].make_play(number,x,y-6)
            if x in range(3,6):
                self.board[2][1].make_play(number,x-3,y-6)
            if x in range(6,9):
                self.board[2][2].make_play(number, x-6,y-6)
                
    def check_row(self,number,y):
        y=y-1
        if y in range(0,3):
            for box in self.board[0]:
                if box.check_row(number,y):
                    return True
        if y in range(3,6):
            for box in self.board[1]:
                if box.check_row(number,y-3):
        
        if y in range(6,9):
            for box in self.board[2]:
                if box.check_row(number,y-6):
        
        return False
    
    def check_col(self,number,x):
        x=x-1
        for line in self.board:
            
