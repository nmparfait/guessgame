from art import logo
print(logo)

#global variables 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#check the difficulty
def set_difficulty():
  """ Giving to the user the possibility to select the level he would like to play"""
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

#Make a function to check the answer
#Track the number of turns and reduce by 1 if they get it wrong.
def check_answer(guess, answer, turns):
  """ Check guess against answer and also track the number of turns remainiing """
  if guess > answer:
    print("Too high.")
    return turns - 1 
  elif guess < answer:
    print("Too low.")
    return turns - 1 
  else:
    print(f"You got it! The answer was {answer}.")
#Making a function to define our game
#Choosing a random number between 1 and 100.
def game():
  """Calling our function all together to get the game functionnality"""

  #Welcome to the game 
  print("Welcome to the Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  from random import randint
  answer = randint(1, 100)
  print(f"Psssss the correct answer is {answer}")
  turns = set_difficulty()
  

  #Repeat the guessing functionnality to see if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts")
    guess = int(input("Make a guess "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses. You lose!")
      return

game()








