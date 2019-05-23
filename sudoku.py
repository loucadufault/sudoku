import time

digits = list(range(1,10))
letters = 'abcdefghi'
boxes = {'tl':(0,0), 'tm':(3,0), 'tr':(6,0), 'ml':(0,3), 'mm':(3,3), 'mr':(6,3), 'bl':(0,6), 'bm':(3,6), 'br':(6,6)}
total_iters = 0

#		 0 1 2 3 4 5 6 7 8
input =[[5,1,7,6,0,0,0,3,4], #0
		[2,8,9,0,0,4,0,0,0], #1
		[3,4,6,2,0,5,0,9,0], #2
		[6,0,2,0,0,0,0,1,0], #3
		[0,3,8,0,0,6,0,4,7], #4
		[0,0,0,0,0,0,0,0,0], #5
		[0,9,0,0,0,0,0,7,8], #6
		[7,0,3,4,0,0,5,6,0], #7
		[0,0,0,0,0,0,0,0,0]] #8

sudoku = []

def view_candidates():
	global total_iters
	for i_row in range(9):
		for i_col in range(9):
			cell = sudoku[i_row][i_col]
			#print('at cell ({}, {})'.format(i_col, i_row))
			#print(str(cell) + " candidates: " + str(cell.candidates))
			#print(str(cell) + " value: " + str(cell.value))
			#print(str(cell) + " box: " + str(cell.box) + '\n')
			total_iters+=1

def create_sudoku(input):
	global total_iters
	for i_row in range(9):
		sudoku.append([])
		for i_col in range(9):
			cell = Cell(i_col, i_row, input[i_row][i_col])
			sudoku[i_row].append(cell)
			total_iters+=1

def elim_from_col(col, value):
	global total_iters
	for i_row in range(9):
		cell = sudoku[i_row][col]
		if cell.value == 0:
			#print('cell {} does not have a value yet'.format(cell))
			cell.remove_candidate(value)
		total_iters+=1

def elim_from_row(row, value):
	global total_iters
	for i_col in range(9):
		cell = sudoku[row][i_col]
		if cell.value == 0:
			cell.remove_candidate(value)
		total_iters+=1	

def elim_from_box(box, value):
	global total_iters
	coords = boxes[box]
	col = coords[0] #3
	row = coords[1] #0
	for i_row in range(row, row+3):
		for i_col in range(col, col+3):
			#print(sudoku[i_row][i_col])
			cell = sudoku[i_row][i_col]
			if cell.value == 0:
				cell.remove_candidate(value)
			total_iters+=1

def draw(sudoku):
	horizon_div = '------+-------+------'
	print('    A B C   D E F   G H I\n')
	for i_row in range(9):
		print(str(i_row+1) + '  ', end='')
		for i_col in range(9):
			cell = sudoku[i_row][i_col]
			#print(' {}'.format(cell.box), end='')
			print(' {}'.format(cell.value if cell.value else ' '), end='')
			if (i_col==2 or i_col==5):
				print(' |', end='')
		if (i_row==2 or i_row==5):
			print('\n    '+horizon_div, end='')
		print('')
	print('')

def is_solved(sudoku):
	global total_iters
	for i_row in range(9):
		for i_col in range(9):
			cell = sudoku[i_row][i_col]
			if cell.is_empty():
				return False
			total_iters+=1
	return True

def basic():
	global total_iters
	for i_row in range(9):
		for i_col in range(9):
			cell = sudoku[i_row][i_col]
			#print('basic at cell:', cell)
			if cell.is_empty():
				cell.elim_by_col()
				cell.elim_by_row()
				cell.elim_by_box()
			total_iters+=1

def main():
	global total_iters
	create_sudoku(input)
	draw(sudoku)
	time.sleep(1)
	while not is_solved(sudoku):
		#view_candidates()
		basic()
		draw(sudoku)
		total_iters+=1
	print('solved after {} iterations'.format(total_iters))

if __name__=='__main__':
	main()	
		
