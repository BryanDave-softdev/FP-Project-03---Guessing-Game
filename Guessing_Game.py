# PROJECT 3: GUESSING GAME

# 🎯 Number Guessing Game

# HeroBoard Entry: #3 - Day 3 Project 03

import random

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thingking of a number betwwen 1 and 10.\n")

# Secret number

secret_number = random.randint(1, 10)
guess = None
tries = 0

# Loop until correct guess

while guess != secret_number:
guess = int(input("🤔 What's your guess? "))
tries += 1

if guess < secret_number:
print("🔺 Too low! Try again.\n")
elif guess > secret_number:
print("🔻 Too high: Try again.\n")
else:
print("✔ Correct! You guessed the number.")

# Final stats

print(f"\n🎉 You found it in {tries} tries!")
if tries <= 1:
print("🏆 One-shot kill! You're a mind reader!")
elif tries <= 3:
print("💪 Sharp guesser!")
else:
print("😅 That was close! But you made it!")
