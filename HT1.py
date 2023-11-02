# ##################
# print("task 1-3")
# number_1 = float(input("input number 1:" ))
# number_2 = float(input("input number 2:" ))
# operation = input("input operation: *, -, +, /, //, %: ")
#
# if operation == "*":
#     print("result is:", number_1 * number_2)
# elif operation == "-":
#     print("result is:", number_1 - number_2)
# elif operation == "+":
#     print("result is: ", number_1 + number_2)
# elif operation == "/":
#     if number_1 == 0:
#         print("result is: 0")
#     elif number_2 == 0:
#         print("incorrect number 2")
#     else:
#         print("result is:", number_1 / number_2)
# elif operation == "//":
#     if number_1 == 0:
#         print("result is: 0")
#     elif number_2 == 0:
#         print("incorrect number 2")
#     else:
#         print("result is:", number_1 // number_2)
# else:
#     if number_1 == 0:
#         print("result is: 0")
#     elif number_2 == 0:
#         print("incorrect number 2")
#     else:
#         print("result is:", number_1 % number_2)
# #################
# print(" task4")
#
# string = str(input("input string for convertion:"))
# print('integer version:', int(string))
# #################
# print("task 5")
# number_1 = int(input("input number 1:" ))
# number_2 = int(input("input number 2:" ))
# print('sum is integer is', number_1+number_2)
# print("sum is in string is", str(number_1) + str(number_2))
#
# ################
# print("task#6")
# name = str(input("name is:"))
# age = int(input("In what year your were born:"))
# year = int(input("what year is it now:"))
# print("this user is:", name, "age is", year-age)
##################
print("task 7")
cels_temperature = float(input("please input temerature in cels: "))
print("temperature in faringets is:", (cels_temperature * (9/5)) + 32)
##################
print("task 8")
far_temperature = float(input("please input temerature in faringeits: "))
print("temperature in cels is:", (far_temperature - 32) * (5/9))
##################
print("task 9")
side_1 = float(input("please input side 1 value: "))
side_2 = float(input("please input side 2 value: "))
side_3 = ((side_1**2)+(side_2**2))**(1/2)
print("GIPOTENUZA is:", side_3)