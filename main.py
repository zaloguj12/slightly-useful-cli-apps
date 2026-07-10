import scripts.calculator
import scripts.notes
import random
import math

scripts.notes.init_db()


def calc(operation_calc):
    if operation_calc == "+":
        print("enter your number then enter your second number")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        result = scripts.calculator.add(num1, num2)
        print(f"Your result is: {result}")
    elif operation_calc == "-":
        print("enter your number then enter your second number")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        result = scripts.calculator.min(num1, num2)
        print(f"Your result is: {result}")
    elif operation_calc == "*":
        print("enter your number then enter your second number")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        result = scripts.calculator.mult(num1, num2)
        print(f"Your result is: {result}")
    elif operation_calc == "/":
        print("enter your number then enter your second number")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        result = scripts.calculator.div(num1, num2)
        print(f"Your result is: {result}")




while True:
    selected_option = input()
    if selected_option == "help":
        print("Here is a list of avaiable commands:")
        print("note")
        print("calc")
        print("color")
        print("help")
        print("exit")
    elif selected_option == "exit":
        break
    elif selected_option == "calc":
        print("What operation?")
        print("+ - * /")
        calc(input())
    elif selected_option == "note":
        scripts.notes.notes_menu()
    elif selected_option == "color":
        break
    else:
            print("type help for commands")