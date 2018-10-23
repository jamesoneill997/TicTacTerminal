import random
b = ["1","2","3","4","5","6","7","8","9"]



print("Type 'start' to begin, press return to exit")

if input() == 'start':
	print('Please input player names:')
	names = [input(),input()]
	firstup = random.randint(0,1)



	print("{} is first to move as X's".format(names[firstup]))
	if firstup == 1:
		names = names[::-1]

	else:
		names = names
else:
	exit()

def set_board():
	print('                                    |         |            ')
	print('                             ',b[0],'    |   ',b[1],'   |  ',b[2],'    ')
	print('                                    |         |            ')
	print('                          ++++++++++++++++++++++++++++++  ')
	print('                                    |         |            ')
	print('                             ',b[3],'    |   ',b[4],'   |  ',b[5],'    ')
	print('                                    |         |            ')
	print('                          ++++++++++++++++++++++++++++++  ')
	print('                                    |         |            ')
	print('                             ',b[6],'    |   ',b[7],'   |  ',b[8],'    ')
	print('                                    |         |            ')
set_board() 



Winner = False
Full = False

turn  = 'Player 1'
def checker():
	inputs = 'XO'
	if b[0] == b[1] and b[1] == b[2]:
		return True
	elif b[3] == b[4] and b[4] == b[5]:
		return True
	elif b[6] == b[7] and b[7] == b[8]:
		return True
	elif b[0] == b[3] and b[3] == b[6]:
		return True
	elif b[1] == b[4] and b[4] == b[7]:
		return True
	elif b[2] == b[5] and b[5] == b[8]:
		return True
	elif b[0] == b[4] and b[4] == b[8]:
		return True
	elif b[2] == b[4] and b[4] == b[6]:
		return  True
	return False

for i in range(9):

	inputs = 'XO'
	if b[0] in inputs and b[1] in inputs and b[2] in inputs and b[3] in inputs and b[4] in inputs and b[5] in inputs and b[6] in inputs and b[7] in inputs and b[8] in inputs and checker() == False:
		print('Well, Well, Well, this calls for a rematch')
		break
	while turn == 'Player 1' and checker() == False:

		try:
			place = b.index(input())

			b[place] = 'X'
			set_board()
			
			break
		except ValueError:
			print('Cell is occupied or does not exist, please try again')
			set_board()
	

	turn = 'Player 2'

	while turn == 'Player 2' and checker() == False:
		try:
			place = b.index(input())
	
			b[place] = 'O'
	
			set_board()
			
			turn = 'Player 1'
			break
		except ValueError:
			print('Cell is occupied or does not exist, please try again')
			set_board()



if 'X' == b[0] and b[0] == b[1] and b[1] == b[2]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[3] and b[3] == b[4] and b[4] == b[5]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[6] and b[6] == b[7] and b[7] == b[8]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[0] and b[0] == b[3] and b[3] == b[6]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[1] and b[1] == b[4] and b[4] == b[7]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[2] and b[2] == b[5] and b[5] == b[8]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[0] and b[0] == b[4] and b[4] == b[8]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'X' == b[2] and b[2] == b[4] and b[4] == b[6]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[0]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[0] and b[0] == b[1] and b[1] == b[2]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[3] and b[3] == b[4] and b[4] == b[5]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[6] and b[6] == b[7] and b[7] == b[8]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[0] and b[0] == b[3] and b[3] == b[6]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[1] and b[1] == b[4] and b[4] == b[7]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[2] and b[2] == b[5] and b[5] == b[8]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[0] and b[0] == b[4] and b[4] == b[8]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
elif 'O' == b[2] and b[2] == b[4] and b[4] == b[6]:
	print('Congrats {}, you are the undisputed champion of python tic tac toe..... Get a life man...\n Would you like a rematch?'.format(names[1]))
	if input() == 'y':
		b = ['1','2','3','4','5','6','7','8','9']
		checker() == False
		turn = 'Player 1'
		set_board()
		checker() == False
		turn = 'Player 1'
	else:
		exit()
