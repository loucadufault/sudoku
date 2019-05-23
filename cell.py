class Cell():
    def __init__(self, col, row, value):
        if value == 0:
            self.value = 0
            self.candidates = digits[:] #ffs
        else:
            self.value = value
            self.candidates = [value]

        self.col = col
        self.row = row
        self.box = self.get_box()

    def __str__(self):
        return "{}{}".format(letters[self.col], self.row+1)

    def is_empty(self):
        return self.value == 0

    def set_value(self, value):
        draw(sudoku)
        self.value = value

    def get_box(self):
        for key, val in boxes.items():
            if ((self.col >= val[0]) and (self.col < val[0]+3)) and ((self.row >= val[1]) and (self.row < val[1]+3)):
                return key

    def remove_candidate(self, value):
        #print('trying to remove {} from cell {}'.format(value, self))
        if self.is_empty():
            #print(self.candidates)
            if value in self.candidates:
                (self.candidates).remove(value) #prolly wrong
                #print('value removed')
                #else:
                #print('no value removed')

    if len(self.candidates) == 1:
        self.set_value(self.candidates[0])
        self.propagate()
        #print('finished propagation for cell: ', self)

    def propagate(self):
        elim_from_col(self.col, self.value)
        elim_from_row(self.row, self.value)
        elim_from_box(self.box, self.value)

    def elim_by_col(self):
        for i_row in range(9):
            compare = sudoku[i_row][self.col]
            if not compare.is_empty():
                self.remove_candidate(compare.value)

    def elim_by_row(self):
        for i_col in range(9):
            compare = sudoku[self.row][i_col]
            if not compare.is_empty():
                self.remove_candidate(compare.value)

    def elim_by_box(self):
        coords = boxes[self.box]
        col = coords[0] #3
        row = coords[1] #0
        for i_row in range(row, row+3):
            for i_col in range(col, col+3):
            compare = sudoku[i_row][i_col]
            if not compare.is_empty():
                self.remove_candidate(compare.value)
