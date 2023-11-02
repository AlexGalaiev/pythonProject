number_1 = float(input("input number 1:" ))
number_2 = float(input("input number 2:" ))
operation = input("input operation: *, -, +, /: ")

if operation == "*":
    print("result is:", number_1 * number_2)
elif operation == "-":
    print("result is:", number_1 - number_2)
elif operation == "+":
    print("result is: ", number_1 + number_2)
elif operation == "/":
    if number_1 == 0:
        print("result is: 0")
    elif number_2 == 0:
        print("incorrect number 2")
    else:
        print("result is:", number_1 / number_2)

