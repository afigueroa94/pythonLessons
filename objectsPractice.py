# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def birthday(self):
#         self.age += 1
#         print(f"Happy birthday, {self.name}! You are now {self.age} years old.")

# person = Person("Sebastian", 25)

# person.birthday()


# class Rectangle:
#     def __init__(self, length, width=None):
#         if width is None:
#             width = length
#         self.length = length
#         self.width = width

#     def display(self):
#         print(f"Length: {self.length}, Width: {self.width}")

# rect = Rectangle(4, 5)
# square = Rectangle(4)

# rect.display()
# square.display()



animals = ["cat", "dog", "hamster"]
for animal in animals:
   print("Hello, " + animal + "!")