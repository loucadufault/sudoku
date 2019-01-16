digits = list(range(10))
blocks = {'a':(0,0), 'b':(3,0), 'c':(6,0), 'd':(0,3), 'e':(3,3), 'f':(6,3), 'g':(6,0), 'h':(3,6), 'i':(6,6)}
rows = []
columns = []
#	 0 1 2 3 4 5 6 7 8
input =[[5,1,7,6,0,0,0,3,4], #0
	[2,8,9,0,0,4,0,0,0], #1
	[3,4,6,2,0,5,0,9,0], #2
	[6,0,2,0,0,0,0,1,0], #3
	[0,3,8,0,0,6,0,4,7], #4
	[0,0,0,0,0,0,0,0,0], #5
	[0,9,0,0,0,0,0,7,8], #6
	[7,0,3,4,0,0,5,6,0], #7
	[0,0,0,0,0,0,0,0,0]] #8

objects = []
def place_objects(input):
	for i_col in range(9):
		objects.append([])
		for i_row in range(9):
			cell = Cell(i_col, i_row, input[i_col][i_row])
			objects[i_col].append(cell)


def elim_from_row(i_row, value):
	for i in range(9):
		objects[i_row][i].remove_possible(value)

def elim_from_col(i_col, value):
	for i in range(9):
		objects[i][i_col].remove_possible(value)	

def elim_by_block(block, value):
	coords = blocks[block]
	i_col = coords[0] #3
	i_row = coords[1] #0
	for i in range(i_col, i_col+3):
		objects[i_row][i].remove_possible(value)
	
0 1 2 3 4 5 6 7 8 9
1
2
3
4
5
6
7
8
9
class Cell():
	def __init__(self, x_pos, y_pos, value):
		self.value = value
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.possibles = digits
	def update_value(value):
		self.value = value
	def remove_possible(value):
		self.possibles = self.possibles.remove(value)
		if len(self.possibles) == 1:
			self.value = self.possibles[0]
		elif len(self.possibles) < 1:
			print('impossible')

	def get_possibles():
		return self.possibles
	def place():
		
		