# SudokuPy
Create a sudoku game in python

The purpose of this project is to create a Sudoku game in python.

V 0.1
Created box and board classes with setup methods

Created make play methods in both, to allow you to add numbers

Created check row method in both, to allow you to check the play

Created check col method in box, in process of creating it in the board

created check box method in box, in process of implementing it to the board


V 0.2

Large update!

Created an erase play method in both SudokuBox and SudokuBoard

Finalized print_board so it has a display you can actually play sudoku off

Finished check_col function, allowing the engine to check if a number is already in the column, meaning...

Finished the make_play method in SudokuBoard, meaning it will let you add numbers, but only if it was a legal play

Created an erase play method in both SudokuBox and SudokuBoard

Changed the number assigning line in SudokuBoard's make_play, erase_play, and check_row functions to work off of % and // division. This lets me use 2 lines where there used to be 12, but does mean readability goes down. Unsure if this is correct path since Sudoku doesn't scale up.

Created class variable to store given numbers; when the method is created to load puzzle data, this will allow the SudokuBoard to mark some numbers as immutable.

Blank squares are now represented by '\_' instead of '10'


TODO:

Create a method to be able to take in puzzle data to initialize the board with a puzzle.
