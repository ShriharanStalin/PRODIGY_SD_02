# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:04:38 2024

@author: Shriharan S
"""

import random

def guessing_game():
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    user_guess = None

    print("Welcome to the Guessing Game!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it.")

    while user_guess != random_number:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guessing_game()
