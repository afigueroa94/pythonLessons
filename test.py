# animals = ["cat", "dog", "hamster"]
# for animal in animals:
#     print("Hello, " + animal + "!")

# shapes = ["square", "rectangle", "circle"]
# for shape in shapes:
#     print("I love " + shape + "!")


# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(f"Fruit: {fruit.lower()}")  # Convert each fruit name to uppercase

# pastas = ["spaghetti", "rigatoni", "ravioli"]
# for pasta in pastas:
#   print(f"Pasta: {pasta.lower()}")

# word = "PYTHON"
# for letter in word:
#     print(letter)

# sentence = "Hello, World!"
# for char in sentence:
#     if char.isupper():
#         print(f"Uppercase letter: {char}")


# for i in range(2, 11, 4):  # Start at 2, end before 11, step by 2
#     print(i)

# for i in range(1, 9):  # Outer loop from 1 to 5
#     for j in range(1, 6):  # Inner loop from 1 to 5
#         print(f"{i} x {j} = {i * j}")
#     print("----------")


# for i in range(10):
#     if i == 5:
#         break  # Exit the loop when i is 5
#     print(i)


# for i in range(30):
#      if i % 3 == 0:
#          continue  # Skip the even numbers
#      print(i)

# for i in range(1, 11):
#      if i % 2 == 0:
#          print(f"{i} is divisible by 2!")
#      elif i % 4 == 0:
#          print(f"{i} is divisible by 4!")
#      else:
#          print(i)


#----------------- WHILE LOOPS ---------------#
# running = True
# while running:
#     print("Keep running!")
#     # If we find the treasure, we stop running.
#     running = False

# count = 1
# while count <= 5:
#     print("Jump!")
#     count += 1

# count = 1
# while count <= 10:
#     print("😊")
#     count += 1

# number_to_guess = 7
# guess = int(input("Guess the number between 1 and 10: "))
# while guess != number_to_guess:
#     print("Try again!")
#     guess = int(input("Guess the number between 1 and 10: "))
# print("You got it!")

# password = ""
# while password != "1234":
#     password = input("Enter the password: ")
# print("Access granted!")

# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         break
#     print(i)

# import random
# number_to_guess = random.randint(1, 10)
# guess = None
# attempts = 0

# while guess != number_to_guess:
#     guess = int(input("Guess the number between 1 and 10: "))
#     attempts += 1
#     if guess < number_to_guess:
#         print("Too low!")
#     elif guess > number_to_guess:
#         print("Too high!")
# print(f"Correct! It took you {attempts} attempts.")


# x = "awesome"

# def myfunc():
#     print("Python is " + x)

# myfunc()


# def divide_numbers(a, b):
#     return a / b

# result = divide_numbers(10, 10)
# print(result)


# def is_palindrome(word):
#     return word == word[::-1]

# word = "mother"
# print(is_palindrome(word))



# def check_weirdness(n):
#     if n % 2 != 0:  # If n is odd
#         print("Weird")
#     else:  # If n is even
#         if 2 <= n <= 5:
#             print("Not Weird")
#         elif 6 <= n <= 20:
#             print("Weird")
#         elif n > 20:
#             print("Not Weird")

# # Example usage:
# n = int(input("Enter a number: "))
# check_weirdness(n)


print(bool("Hello"))
print(bool("5j"))

