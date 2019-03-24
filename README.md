Intuitive 9x9 Sudoku solver in Python 3.7

<h1>Program Structure</h1>

All code for the sudoku solver is currently in a single `sudoku.py` file. It will eventually be broken up into:
1. `cell.py`, containing the code for the Cell class.
2. `algorithms.py`, containing the code for all 3 solving algorithms.
3. `utils.py`, containing all helper functions that display UI, take input, ensure proper functioning of the main loop, or keep track of execution metrics.
4. `sudoku.py`, containing the code for building the sudoku, running the main solving loop, and displaying the interface.

<h1>Terminology</h1>

sudoku: a well-made sudoku should have a unique answer, although this akgorithm can find one answer among many

counting: iterating through the cells in the sudoku, starting at the top row and ending at the bottom row, starting at the leftmost cell and ending at the rightmost cell for each row.

cell: a square in the sudoku grid, can have a value from 1-9 or no value, represented by a 0

box: a 3x3 subgrid of the sudoku. There are 9 boxes; tl (top left), tm, tr, ml (middle left), mm, mr, bl (bottom left), bm, br.

fill: an empty cell can be filled by determining its value (the only value it could take without breaking the sudoku) to become a solved cell. A given cell is already filled.

given: a cell that was given a value from the initial input matrix

empty: a cell that had no value in the input matrix (represented by the integer 0), and that has not yet been filled.

solved: a solved sudoku has all 81 of its cells filled such that the sudoku is valid

candidates: list of possible values for each cell, i.e values that cell could become without breaking the sudoku.
For given cells, it is an array containing one item, that cell's value. For empty cells, it is initialized to a list of digits 1-9.

<h1>Data Structures</h1>

<h3>input</h3>

`input` is initialized to a global matrix that holds 81 integer values representing the values of each cell in the sudoku that we are trying to solve. It has 9 nested arrays, each with 9 items, making it a 9x9 matrix. 

Each item's position correpsonds directly to a cell in the sudoku to solve; for example, the item in the first nested array (`input[0]`) at index 4 (`input[0][4]`) holds the value of the cell in the first row and the 5th position (arrays start at 0) in the sudoku to solve. 

If a item in the input matrix has value 1-9, it means the cell in the sudoku to solve had a given value. If the item has value 0, it means the cell in the sudoku to solve was empty. 

Currently the input matrix must be manually edited within the source code but there is work to facilatate this process with alternate input methods.

<h3>sudoku</h3>

`sudoku` is a matrix of the same exact shape as the `input` matrix above, i.e. it has 9 nested arrays, each with 9 items, making it a 9x9 matrix. 

The only difference, is that instead of holding 81 integer values, it holds 81 `Cell` objects. Each item with integer value in the `input` matrix is used to create a `Cell` object, which is then stored in the exact same position in the `sudoku` matrix. 

`sudoku` is initialized to an empty global array, then built from the `input` matrix by the function `create_sudoku()`, which counts through each item in the `input` matrix and constructs a `Cell` object from that integer value (reagrdless of whether it is 1-9, or 0), which it then places at the same row and column position in the `sudoku` matrix.

For example, assuming the item at position say `input[0][4]` in the `input` matrix was a given cell in the sudoku to solve, with a certain value say 7, then we could `assert(input[0][4] == sudoku[0][4].value)`. The item at a given position in the `input` matrix would be storing the same integer as what was held in the `value` attribute of the `Cell` object at the same given position in the `sudoku` matrix. 

<h3>Cell</h3>

The items representing cells in the `sudoku` matrix are instances of a `Cell` class. There are 81 instances stored in a `sudoku` matrix.



The `Cell` class constructor sets 5 attributes:
1. A value, either a digit from 1-9, or 0 to represent that the cell is empty
2. An array of candidates, either containing one item, the cell's value, or initialized to an array of digits for empty cells
3. A column, representing the cell's column in the sudoku matrix (i.e. its index in one of the nested row arrays in the sudoku)
4. A row, representing the cell's row in the sudoku matrix (i.e. the index of of its nested row array in the sudoku)
5. A box, representing the cell's box in the sudoku matrix. (i.e. the string corresponding to the name of the box , see Terminology>box)

Note, although each cell has a unique column-row pair, for each of the 9 boxes, 9 cells share the same box.

explain logic in constructor

<h1>Algorithms</h1>

<h2>Counting Elimination</h2>

0: Build the sudoku from an 9x9 input matrix containing either numbers from 1-9, or a 0 if the cell is empty. 
The sudoku is represented by a 9x9 matrix containing Cell objects. in the same arrangement as the input.
Each cell has a value (1-9 or 0 if the input cell was empty), a list of candidates (initialized as an array of all digits from 1-9, or the cell's value if the input cell was a given)
1: Iterate through the cells in

<h2>Recursive Constraint Propagation </h2>

<h2>Guess Bactracking</h2>
