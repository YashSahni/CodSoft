import tkinter as tk
from tkinter import messagebox
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid Input")

       
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()




def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.num1_label = tk.Label(root, text="Enter first number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(root, text="Enter second number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        self.result_var = tk.StringVar()
        self.result_display = tk.Label(root, textvariable=self.result_var)
        self.result_display.pack()

        self.add_button = tk.Button(root, text="Add", command=self.add)
        self.add_button.pack()

        self.subtract_button = tk.Button(root, text="Subtract", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(root, text="Multiply", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(root, text="Divide", command=self.divide)
        self.divide_button.pack()

    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = add(num1, num2)
            self.result_var.set(result)

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = subtract(num1, num2)
            self.result_var.set(result)

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = multiply(num1, num2)
            self.result_var.set(result)

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = divide(num1, num2)
            self.result_var.set(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

