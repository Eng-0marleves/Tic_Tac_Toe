from Draw import Draw
from Execute import Execute


class Play:
	def __init__(self):
		pass

	def __str__(self):
		return "this object is run the game"

	def help(self):
		print("Welcome to Tic Tac Toe!")
		print("To play the game, follow these instructions:")
		print("1. The game is played on a nxm grid.")
		print("2. Each player takes turns to place their mark (X or O) on the grid.")
		print("3. The goal is to get three of your marks in a row (horizontally, vertically, or diagonally).")
		print("4. The first player to achieve this wins the game.")
		print("5. If all squares are filled and no player has won, the game ends in a draw.")
		print("6. To place your mark, enter the row and column numbers when prompted.")

		print("\nExample:")
		print("Let's say it's player 1's turn (X mark). The current grid is:")
		print("   1   2   3")
		print("1  X |   | X ")
		print("  ---+---+---")
		print("2  O | X | O ")
		print("  ---+---+---")
		print("3  X | O |   ")
		print("\nPlayer 1 wants to place their mark in row 3, column 2.")
		print("They would enter '3' when prompted for the row, and '2' when prompted for the column.")
		print("\n" * 2)


	def start(self):
		check_knowledge= input("Do you know how to play (enter help to show how to play or enter any thing to skip): ")
		if check_knowledge.lower().strip() == "help":
			self.help()

		while True:
			command = input("Do You want to start (yes or no): ")
			if command is not None:
				if command.lower().strip() == "yes":
					Execute.run()
					again = input("Do you want to play again (yes or no): ")
					if again.lower().strip() == "yes":
							Execute.run()
							again = input("Do you want to play again (yes or no): ")

					elif again.lower().strip() == "no":
						print("Stoped")
						return 0
					else:
						print("unknown input, so the program will be stopped")
						return 0
				elif command.lower().strip() == "no":
					print("Stoped")
					return 0
				else:
					print("unknown input, please enter (yes) to start or (no) to stop: ")
					continue
			else:
				print("unknown input, please enter (yes) to start or (no) to stop: ")
