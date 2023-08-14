class Draw:
	def __init__(self, rows=3, columns=3):
		self.rows = int(rows)
		self.columns = int(columns)
		self.matrix = [[' ' for _ in range(columns)] for _ in range(rows)]

	def __str__(self):
		return "this object is presenting draw of matrix size\nand add marks to the selected positions"

	def __len__(self):
		return self.rows * self.columns

	def draw(self):
		print("\n" + "-" * (4 * self.columns + 1))
		for i in range(self.rows):
			print("|", end="")
			for j in range(self.columns):
				print(" {} |".format(self.matrix[i][j]), end="")
			print("\n" + "-" * (4 * self.columns + 1))
		print("\n")

	def add_mark(self, row, column, mark):
		if (row-1) < 0 or (row-1) >= self.rows or (column-1) < 0 or (column-1) >= self.columns:
			print("Invalid position")
		elif self.matrix[row-1][column-1] != ' ':
			print("Square already occupied")
		else:
			self.matrix[row-1][column-1] = mark


	def is_square_empty(self, row, column):
		return self.matrix[row][column] == ' '

