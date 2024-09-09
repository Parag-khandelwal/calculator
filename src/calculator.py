"""A simple calculator module that contains addition, subtraction and 
product of two positive integers."""

class Calculator:
    def __init__(self):
        pass

    def addition(self, *args):
        """Takes multiple numbers and returns the sum of them"""
        return sum(args)

    def substraction(self, x,y):
        """Takes two numbers and returns the substraction of them"""
        return x-y

    def product(self, x, y):
        """Takes two numbers and returns the product of those two numbers"""
        return x*y

if __name__ == "__main__":

    cal = Calculator()

    print(f"Addition: {cal.addition(1,2,3,4,5)}")
    print(f"Substraction: {cal.substraction(10, 5)}")
    print(f"Product: {cal.product(10, 5)}")