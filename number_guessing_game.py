import random
lives = 3
levels = [
    (1, 0, 9),
    (2, 0, 50),
    (3, 0, 100)
]

print("Welcome to the Number Guessing Game!")
print("You have 3 lives. Guess the bot's number to move to the next level.\n")

level_index = 0

while level_index < len(levels) and lives > 0:
    level_num, low, high = levels[level_index]
    bot_number = random.randint(low, high)

    print(f"Level {level_num}: Guess a number between {low} and {high}")
    guess = int(input("Your guess: "))

    if guess == bot_number:
        print("Correct! Moving to the next level.\n")
        level_index += 1
    else:
        lives -= 1
        print(f"Wrong! The number was {bot_number}. Lives left: {lives}\n")

if level_index == len(levels):
    print("Congratulations! You cleared all 3 levels!")
else:
    print("Game Over! You ran out of lives.")
