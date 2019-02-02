# Write a Sudoku valid move checker (https://en.wikipedia.org/wiki/Sudoku)

# This checker should be able to be given the current board state 
#    and a potential move and return a boolean of whether the move is valid
#    
# 9X9 
# number unique for a row, column and 3x3 region 


# Assuming rows (y) is 1-9, from top to bottom
# Assuming cols (x) is 1-9, from left to right
# this is a test to see if i can push commits.

current_board_state = []


class SudokuBox:
    #the class for one 3x3 box in a sudoku grid.
    #note: all methods assume the (x,y) coordinates go from 1 to 3
    #That is, the methods will convert to list indices for you.
    
    def __init__(self):
        #the data structure for one sudoku box is a list of lists
        #'_' is a blank box
        self.box=[
            ['_','_','_'],
            ['_','_','_'],
            ['_','_','_'],
        ]
    
    def is_blank(self,x:int,y:int)->bool:
        #Check if a space in the box has an entry yet.
        return self.box[y-1][x-1]=='_'
        
    def check_box(self,num:int)->bool:
        #check if the current box contains given number
        #True means it does
        for line in self.box:
            if num in line:
                return True
        return False
    
    def return_box(self)->list:
        #returns the box as a list
        return self.box
    
    def make_play(self, number:int, x:int, y:int)->None:
        #enters the number given into coordinates x,y
        if number not in range(1,10):
            print('Only numbers from 1-9 allowed in this box!')
        elif self.check_box(number):
            print('That number is already in that box')
        elif x in range(1,4) and y in range(1,4):
            self.box[y-1][x-1] = number
        else:
            print('Your coordinates are not allowed in this box.')
            #not allowed to have an x or y >3
            
    def erase_play(self, x, y)->None:
        #erases the number given into coordinates x,y
        #note: the check for whether a number is allowed to be erased is in SudokuBoard
        #this method could be used to bypass that! Not for player use!

        if x in range(1,4) and y in range(1,4):
            self.box[y-1][x-1]='_'
        else:
            print('Your coordinates are not allowed in this box.')
            #not allowed to have an x or y >3
        
    def check_row(self,number,y)->bool:
        #check if a number is in given row of this box
        return number in self.box[y-1]
    
    def check_col(self,number,x):
        #check if a number is in a given column of this box
        for i in self.box:
            if i[x-1] == number:
                return True
        return False
        

class SudokuBoard:
    #the class for one sudoku grid
    #note: all methods assume the (x,y) coordinates go from 1 to 9.
    #That is, the methods will convert to list indices for you.
    #Keep in mind any box methods also assume the same coordinate format, not indices.
    #SudokuBoard has the row and column checks. The box check is built into SudokuBox
    
    def __init__(self):
        #the data structure is a list of 3 lists, each of which has 3 SudokuBoxes
        
        self.board=[[],
                    [],
                    []]
        
        #Need to create a method to load a puzzle. The starting numbers will go in this list, and not be able to be altered
        self.puzzleSets=[]
        
        for y in range(3):
            for x in range (3):
                self.board[y].append(SudokuBox())
            
    def print_board(self):
        #prints the board
        print(25*'-')
        for boxrow in self.board:
            #for each row of SudokuBoxes
            for i in range(0,3):
                #For each row in the boxes
                rowtoprint='| '

                for box in boxrow:
                    #print that row
                    #this is printing
                    rowtoprint=rowtoprint+' '.join(str(e)for e in box.return_box()[i])+' | '
                print(rowtoprint)
            print(25*'-')
    
    def load_puzzle(self, inputFile)->None:
        # inputfile will be a list of 'number, x, y' entries
        # for each item, make that play, then add [x,y] to a list
        # at the end, load list into puzzleSets
        # if a play is illegal, erase every play before that from the board
        # now puzzleSets hasn't been loaded with data
        # print success or failure
        pass

    def make_play(self,number, x, y):
        #enters the number given into coordinates x,y on the board

        if number not in range(1,10):
            print('Only numbers from 1-9 allowed on the board!')
        elif [x,y] in self.puzzleSets:
            print("That number is given, and can't be changed")

        elif self.check_row(number,y):
            print("That number is already in that row.")
        elif self.check_col(number,x):
            print("That number is already in that column.")
        else:
            x=x-1
            y=y-1
            #use floor to get the box row, and use modulous to get the coordinates within the box
            self.board[y//3][x//3].make_play(number,x%3+1,y%3+1)

            
        ''' Old method of finding correct box and box coordinates
        elif y in range(1,4):
            if x in range(1,4):
                self.board[0][0].make_play(number,x%3,y%3)
            elif x in range(4,7):
                self.board[0][1].make_play(number,x%3,y%3)
            elif x in range(7,10):
                self.board[0][2].make_play(number,x%3,y%3)
                
        elif y in range(4,7):
            if x in range(1,4):
                self.board[1][0].make_play(number,x%3,y%3)
            elif x in range(4,7):
                self.board[1][1].make_play(number,x%3,y%3)
            elif x in range(7,10):
                self.board[1][2].make_play(number,x%3,y%3)
                
        elif y in range(7,10):
            if x in range(1,4):
                self.board[2][0].make_play(number,x%3,y%3)
            elif x in range(4,7):
                self.board[2][1].make_play(number,x%3,y%3)
            elif x in range(7,10):
                self.board[2][2].make_play(number,x%3,y%3)'''

        self.print_board()
                
    def erase_play(self, x, y):
        #erase the number from a given location


        if [x,y] in self.puzzleSets:
            print("That number is given, and can't be changed.")
        else:
            x=x-1
            y=y-1
            self.board[y//3][y//3].erase_play(x%3+1,y%3+1)
        
        self.print_board()
                
    def check_row(self,number,y)->bool:
        #checks if the given number is already in a given row across the entire board
        #True means the number is present
        for box in self.board[(y-1)//3]:
            return box.check_row(number,(y-1)%3+1)
        '''if y in range(1,4):
            for box in self.board[0]:
                if box.check_row(number,y):
                    return True
        elif y in range(4,7):
            for box in self.board[1]:
                if box.check_row(number,y-3):
                    return True
        elif y in range(7,10):
            for box in self.board[2]:
                if box.check_row(number,y-6):
                    return True
        return False'''
    
    def check_col(self,number,x)->bool:
        # checks if the given number is already in a given column across the entire board
        # True means the number is present
        check=False
        if x in range(1,4):
            for line in self.board:
                check= (line[0].check_col(number,x)) or check
                
        elif x in range(4,7):
            for line in self.board:
                check= line[1].check_col(number,x-3) or check

        elif x in range(7,10):
            for line in self.board:
                check= line[2].check_col(number,x-6) or check
        return check
