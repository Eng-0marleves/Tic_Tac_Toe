import os
import random
import signal
from Draw import Draw


class Execute:
	def __init__():
		pass

	def __str__(self):
		return "this object is executing command"

	def checker(matrix):
		n = len(matrix)
		m = len(matrix[0])
		pattern_len = 3

		# check rows
		for i in range(n):
			for j in range(m - pattern_len + 1):
				if matrix[i][j:j+pattern_len] == ['X', 'X', 'X'] or matrix[i][j:j+pattern_len] == ['O', 'O', 'O']:
					return "win"

		# check columns
		for j in range(m):
			for i in range(n - pattern_len + 1):
				column_pattern = [matrix[i+k][j] for k in range(pattern_len)]
				if column_pattern == ['X', 'X', 'X'] or column_pattern == ['O', 'O', 'O']:
					return True

		# Check diagonals (top-left to bottom-right)
		for row in range(n - 2):
			for col in range(m - 2):
				if matrix[row][col] != ' ' and matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2]:
					return "win"

		# Check diagonals (top-right to bottom-left)
		for row in range(n - 2):
			for col in range(2, m):
				if matrix[row][col] != ' ' and matrix[row][col] == matrix[row + 1][col - 1] == matrix[row + 2][col - 2]:
					return "win"

		return "draw" if Execute.is_board_full(matrix) else "ongoing"


	def is_board_full(matrix):
		for row in matrix:
			if ' ' in row:
				return False
		return True


	def run():
		os.system("clear"),

		rows = int(input("Enter the number of Matrix rows: "))
		if rows < 3:
			print("Matrix rows must be at least 3")
			rows = 3

		columns = int(input("Enter the number of Matrix columns: "))
		if columns < 3:
			print("Matrix columns must be at least 3")
			columns = 3

		player1 = input("Enter the player 1 name: ")
		player2 = input("Enter the player 2 name: ")

		if random.randint(0, 1) == 0:
			print(player1 + " play by X\n" + player2 + " play by O")
			player1_mark = 'X'
			player2_mark = 'O'
		else:
			print(player1 + " play by O\n" + player2 + " play by X")
			player1_mark = 'O'
			player2_mark = 'X'

		draw = Draw(rows, columns)

		while True:
			draw.draw()

			print("please {} Enter your square".format(player1))
			row = int(input("\t>> row: "))
			column = int(input("\t>> column: "))
			draw.add_mark(row, column, player1_mark)
			draw.draw()

			if Execute.checker(draw.matrix) == "win":
				print("=" * 30)
				print("{} had won".format(player1))
				print("=" * 30)
				print("\n \n")
				break
			elif Execute.checker(draw.matrix) == "balance":
				print("=" * 30)
				print("Balance, All squares occupied")
				print("=" * 30)
				print("\n \n")
				break


			print("please {} Enter your square".format(player2))
			row = int(input("\t>> row: "))
			column = int(input("\t>> column: "))
			draw.add_mark(row, column, player2_mark)

			if Execute.checker(draw.matrix ) == "win":
				print("=" * 30)
				print("{} had won".format(player2))
				print("=" * 30)
				print("\n \n")
				break
			elif Execute.checker(draw.matrix) == "balance":
				print("=" * 30)
				print("Balance, All squares occupied")
				print("=" * 30)
				print("\n \n")
				break
