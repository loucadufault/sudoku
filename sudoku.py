digits = list(range(10))
letters = 'abcdefghi'
boxes = {'a':(0,0), 'b':(3,0), 'c':(6,0), 'd':(0,3), 'e':(3,3), 'f':(6,3), 'g':(6,0), 'h':(3,6), 'i':(6,6)}

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

cells = []

def create_cells(input):
	for i_row in range(9):
		objects.append([])
		for i_col in range(9):
			cell = Cell(i_col, i_row, input[i_row][i_col])
			cells[i_row].append(cell)

def elim_from_col(col, value):
	for i_row in range(9):
		cells[i_row][col].remove_possible(value)

def elim_from_row(row, value):
	for i_col in range(9):
		cells[row][i_col].remove_possible(value)	

def elim_from_box(box, value):
	coords = boxes[box]
	col = coords[0] #3
	row = coords[1] #0
	for i_row in range(row, row+3):
		for i_col in range(col, col+3):
			cells[i_row][i_col].remove_possible(value)

class Cell():
	def __init__(self, col, row, value):
		self.value = value
		self.col = col
		self.row = row
		self.box = self.get_box()
		self.possibles = digits

	def get_possibles():
		return self.possibles

	def set_value(value):
		self.value = value

	def get_box():
		for key, val in boxes.items():
			if ((self.col > val[0]) and (self.col < val[0]+3)) and ((self.row > val[1]) and (self.row < val[1]+3)):
				return key

	def remove_possible(value):
		if value in self.possibles:
			(self.possibles).remove(value) #prolly wrong
			print('value removed')
		else:
			print('no value removed')
		if len(self.possibles) == 1:
			self.set_value(self.possibles[0])
			self.propagate()
			print('finished propagation for this cell')
		# elif len(self.possibles) < 1:
		# 	print('impossible')

	def propagate():
		elim_from_col(self.col, self.value)
		elim_from_row(self.row, self.value)
		elim_from_box(self.box, self.value)

	def __str__():
		return "{}{}".format(letters[self.col], self.row)


def draw(cells):
	horizon_div = '------+-------+------'
	print('    A B C   D E F   G H I\n')
	for i_row in range(9):
		print(str(i_row+1) + '  ', end='')
		for i_col in range(9):
			cell = cells[i_row][i_col]
			print(' {}'.format(cell if cell else ' '), end='')
			if (i_col==2 or i_col==5):
				print(' |', end='')
		if (i_row==2 or i_row==5):
			print('\n    '+horizon_div, end='')
		print('')

draw(input)
		
		