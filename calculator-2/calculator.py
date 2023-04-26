"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

user_input = " "
while user_input != "q":
    user_input = input("Please enter your equation >")
    user_input_token  = user_input.split(" ")
    result = 0
    x = 1

    while x < len(user_input_token):
        user_input_token[x] = float(user_input_token[x])
        x+=1
    
    if user_input_token[0] == "+": 
        result = add(user_input_token[1], user_input_token[2])
        
    elif user_input_token[0] == "-":
        result = subtract(user_input_token[1], user_input_token[2])

    elif user_input_token[0] == "*":
        result = multiply(user_input_token[1], user_input_token[2])

    elif user_input_token[0] == "/":
        result = divide(user_input_token[1], user_input_token[2])

    elif user_input_token[0] == "square":
        result = square[user_input_token[1]]

    elif user_input_token[0] == "cube":
        result = cube(user_input_token[1])

    elif user_input_token[0] == "pow":
        result = power(user_input_token[1], user_input_token[2])

    elif user_input_token[0] == "mod":
        result = mod(user_input_token[1], user_input_token[2])
    
    else: 
        total = "Please enter a valid equation."

    print(total)