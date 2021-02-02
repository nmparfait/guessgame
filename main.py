from art import logo
print(logo)

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
from random import randint

#Choosing a random number between 1 and 100.
answer = randint(1, 100)
print(f"Psssss the correct answer is {answer}")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Make a function to set difficulty.
def check_answer(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it! The answer was {answer}.")

#check the difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS




#Let user guess a number
guess = int(input("Make a guess: "))
turns = 0

set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")

#Function to check the user's guess against actual answer. 

#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.



