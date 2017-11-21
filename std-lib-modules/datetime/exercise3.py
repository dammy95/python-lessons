import random


if __name__ == '__main__':
  value = random.randint(0, 100)
  
  guesses = 0
  while True:
    user_input = int(input("Please enter your guess: "))

    if user_input > value:
      print("Your value is too high")
    elif user_input < value:
      print("Your value is too low")
    elif user_input == value:
      print("You guessed correctly! ")  
      guesses += 1 
      break
    guesses += 1
