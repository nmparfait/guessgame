from art import logo
print(logo)

#global variables 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#check the difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

#Make a function to check the answer
def check_answer(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it! The answer was {answer}.")
#Choosing a random number between 1 and 100.
def game():
  #Welcome to the game 
  print("Welcome to the Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  from random import randint
  answer = randint(1, 100)
  print(f"Psssss the correct answer is {answer}")
  turns = set_difficulty()
  print(f"You have {turns} attempts")

  #Repeat the guessing functionnality to see if they get it wrong
  guess = 0
  while guess != answer:
    guess = int(input("Make a guess "))
    check_answer(guess, answer)

game()





#Function to check the user's guess against actual answer. 

#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.



