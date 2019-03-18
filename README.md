Intuitive Sudoku solver in Python 3.7

<h1>Terminology</h1>
counting: iterating through the cells in the sudoku, left to right then top to bottom.

propagating: 

cell: a cell in the sudoku grid, can have a value from 1-9 or no value, represented by a value of 0

box: a 3x3 subgrid of the sudoku. There are 9 boxes; tl (top left), tm, tr, ml (middle left), mm, mr, bl (bottom left), bm, br.

given: a cell that was given a value from the initial input matrix

candidates: list of possible values for each cell, i.e values that cell could become without breaking the sudoku.
For given cells, it is an array containing one item, that cell's value. For empty cells, it is initialized to a list of digits 1-9.

<h1>Program Structure</h1>

The sudoku is represented by a 2 dimensional array.
The cells in the sudoku are represented by Cell objects. There are 81 instances stored in an sudoku matrix (see above).
Each cell has 5 attributes:
1. A value, either a digit from 1-9, or 0 to represent that the cell is empty
2. An array of candidates, either containing one item, the cell's value, or initialized to an array of digits for empty cells
3. A column, representing the cell's column in the sudoku matrix (i.e. its index in one of the nested row arrays in the sudoku)
4. A row, representing the cell's row in the sudoku matrix (i.e. the index of of its nested row array in the sudoku)
5. A box, representing the cell's box in the sudoku matrix. (i.e. the string corresponding to the name of the box , see Terminology>box)

Note, although each cell has a unique column-row pair, for each of the 9 boxes, 9 cells share the same box.

<h1>Algorithm</h1>

0: Build the sudoku from an 9x9 input matrix containing either numbers from 1-9, or a 0 if the cell is empty. 
The sudoku is represented by a 9x9 matrix containing Cell objects. in the same arrangement as the input.
Each cell has a value (1-9 or 0 if the input cell was empty), a list of candidates (initialized as an array of all digits from 1-9, or the cell's value if the input cell was a given)
1: Iterate through the cells in
