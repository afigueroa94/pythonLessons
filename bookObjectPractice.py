class Book:
    def __init__(self, pages, color):
        self.pages = pages
        self.color = color

    def show_color(self):
        print(f"This book is {self.color}")

    def read(self):
        print(self.pages)

book1 = Book("20", "black")
book2 = Book("30", "pink")

book2.read()