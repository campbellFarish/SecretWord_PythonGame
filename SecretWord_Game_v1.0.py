#Secret Word Game
#author: R. Campbell Farish
import random


### classes

# letter info class holds onto toggle for if the letter has been guessed 
# and a list of references to where that letter is in the puzzle for quicker search later 
class letter_info():
	def __init__( self, letter ):
		self.letter = letter
		self.guessed = 0
		self.index_list = [] #(line,index)

	# return a dash if has been guessed otherwise return letter
	def return_letter( self ):
		if self.guessed == 0:
			return self.letter
		else:
			return '-'



### functions

# returns a string of the alphabet with letters that have been guessed lined out
def return_alphabetString( curr_alphabet ):

	temp_alpha = [ "" ]
	
	# call sub funciton for 3 chunks of the alphabet with new lines in between
	for c in alphabet_line1:
		temp_alpha.append( curr_alphabet[c].return_letter() )
	temp_alpha.append("\n ")
	
	for c in alphabet_line2:
		temp_alpha.append( curr_alphabet[c].return_letter() )
	temp_alpha.append("\n")

	for c in alphabet_line3:
		temp_alpha.append( curr_alphabet[c].return_letter() )
	temp_alpha.append("\n")

	return ' '.join( temp_alpha )


# returns a string of the current state of the puzzle with guessed letters revealed
def return_puzzleString( curr_puzzle ):

	temp_puzzle = ""

	for x in range( 0, 4 ):
		temp_puzzle += " " + " ".join( curr_puzzle[x] ) + "\n"

	return temp_puzzle


# print the entire gameBoard, compile the string and then send to print
def print_gameBoard( curr_alphabet, curr_puzzle, curr_score ):

	#line 1: hash tag boarder
	print_string = "###################\n"

	#line 2-4: alphabet
	print_string += return_alphabetString( curr_alphabet )

	#line 5: has tag boarder
	print_string += "###################\n"
	
	#line 6-9: PUZZLE
	print_string += return_puzzleString( curr_puzzle )
	
	#line 10: has tag boarder
	print_string += "###################\n"

	#line 11: level and score
	print_string += "LVS:%2d  SCR:%7d\n" % ( lives_left, curr_score ) 

	#line 12: has tag boarder
	print_string += "###################\n"

	print( print_string )


def printNo():
	print("\n     :( NO :(       ")
	

def printYes():
	print("\n     =D YES =D       ")




### variables

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_line1 = "ABCDEFGHI"
alphabet_line2 = "JKLMNOPQ"
alphabet_line3 = "RSTUVWXYZ"
word_list = [ ["CHICKEN", "MONKEY", "OWL", "ELEPHANT"], ["LIZARD", "MOUSE", "HAMSTER", "LEOPARD"], ["ALLIGATOR", "LIONESS", "DOG", "PIGEON"], ["STORK", "LLAMA", "KITTEN", "PORCUPINE"], ["KOALA", "TURTLE", "KANGAROO", "SNAKE"], ["SALMON", "PANTHER", "DOLPHIN", "WHALE"], ["ROOSTER", "PENGUIN", "HOUND", "WORM"], ["MOOSE", "LAMB", "RHINO", "BEETLE"], ["ZEBRA", "BADGER", "LYNX", "COUGAR"], ["CHEETAH", "GRIZZLY", "SHARK", "GECKO"]]




# begin round

# intialize variales
curr_level = 1
curr_score = 0


# ask to play
should_exit = 0
lives_left = 10
while ( should_exit == 0 ):

	play_choice = ( raw_input( " PLAY AGAIN? (Y/N): " ) ).upper()
	
	if play_choice == 'N':
		should_exit = 1
	
	elif play_choice == 'Y':

		# choose a word
		secret_words = random.choice(word_list)
		secret_words_all = secret_words[0] + secret_words[1] + secret_words[2] + secret_words[3]
		num_of_letters_left = len(secret_words_all)

		# pre-process the word

		# intialize variales
		curr_puzzle = [[],[],[],[]]
		curr_alphabet = dict()

		# create a dictionary of letters 
		for c in alphabet:
			curr_alphabet[c] = letter_info(c)

		# pre-process the four lines/words
		for x in range( 0, 4 ):
			counter = 0
			for c in secret_words[x]:
				#blank out the game board
				curr_puzzle[x].append('_')
				#record indicies of if/when they appear in secret word
				curr_alphabet[c].index_list.append([x,counter])
				counter = counter + 1


		#loop while the game is not won or lost (in won state or lost state)
		while ( num_of_letters_left !=0 and should_exit == 0 ):

			# print Game Screen
			print_gameBoard( curr_alphabet, curr_puzzle, curr_score )

			# get a single guess input 
			valid_guess = 0
			while valid_guess == 0:

				# input a guess letter from the user
				curr_guess = (raw_input(" GUESS A LETTER: ")).upper()
				
				# break out and exit program with number 1
				if curr_guess == '1':
					should_exit = 1
					valid_guess = 1
				# make sure choice is letter
				elif curr_guess not in alphabet:
					print(" LETTERS ONLY")
				# make sure it's not empty
				elif curr_guess == '':
					print(" I DIDN'T GET THAT")
				# if it's a valid unguessed letter than move on
				elif curr_alphabet[curr_guess].guessed == 0:
					#record that the letter has been guessed and set loop breaking condition
					curr_alphabet[curr_guess].guessed = 1
					valid_guess = 1
				# this letter has already been guessed, input again
				else:
					#or loop back around and try again
					print(" ALREADY GUESSED")

			if should_exit == 0:
				#check if the inputed letter is in the secret word
				i_list = curr_alphabet[curr_guess].index_list
				if len(i_list) != 0:
					#if it is in the secret word, reveal letter in the secret word
					for i in i_list:
						line_num = i[0]
						line_idx = i[1]
						curr_line = curr_puzzle[line_num]
						curr_line[line_idx] = curr_guess
						num_of_letters_left = num_of_letters_left - 1
						curr_score += 50
					printYes()
				else:
					lives_left = lives_left - 1
					curr_score -= 50
					if lives_left == 0:
						should_exit = 1
					printNo()


		if num_of_letters_left > 0:	
			print("WAY TO GO")
			print_puzzle( curr_puzzle )
		elif should_exit == 1:
			print("GOODBYE.")
		else:
			print("DANG :(")