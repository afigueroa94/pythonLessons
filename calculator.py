def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return ("Error, cannot divide by 0.")
    
def calculator():
    print("Select operation")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choice = input("Enter your choice 1234: ")

    if choice in ["1", "2", "3", "4"]:
        num1 = input("Enter the first number.")
        num2 = input("Enter the second number.")

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input.")

if __name__ == "__main__":
  while True:
        calculator()
        another_calculation = input("Try another one? Yes or no: ")
        if another_calculation.lower() != "Yes.":
            break
    




        