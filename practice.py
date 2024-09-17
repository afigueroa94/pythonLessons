import random

def guess_the_number(best_score):
  while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    incorrect_guesses = 0
    max_attempts = 7
    print("\nWelcome to the Number Guessing Game!")
    print(f"I have selected a number between 1 and 100. You have {max_attempts} attempts to guess it.")


    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
            incorrect_guesses += 1
        elif guess > secret_number:
            print("Too high! Try again.")
            incorrect_guesses += 1
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        
            if best_score is None or attempts < best_score:
                best_score = attempts
                print(f"New best score: {best_score} attempts!")
            break

        if incorrect_guesses == 3:
            if secret_number  % 2 == 0:
              print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")
        elif incorrect_guesses == 5:
            if secret_number % 3 ==0:
                print("Hint: The number is divisible by 3.")
            else:
                print("Hint: The number is not divisible by 3.")

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts! The number was {secret_number}.")

    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print(f"Your best score was: {best_score} attempts. Thanks for playing!")
        break

  return best_score


best_score = float()



best_score = guess_the_number(best_score)