
# Task 1
# print("Hello user")
# print("Please enter a number from 1 to 7 and we will display the day of the week")
# numb = None
# while numb is None:
#     try:
#             numb = int(input("Nunber: "))
#             match  numb:
#                 case 1:
#                     print("Monday")
#                 case 2:
#                     print("Tuesday")
#                 case 3:
#                     print("Wednesday")
#                 case 4:
#                     print("Thursday")
#                 case 5:
#                     print("Friday")
#                 case 6:
#                     print("Saturday")
#                 case 7:
#                     print("Sunday")
#     except ValueError:
#         print("Enter a number from 1 to 7 without letters")
#     finally:
#         print("Thank you for using our program.")

# task 2
# print("Hello user")
# print("Please enter two numbers")
# try:
#     numb1 = int(input("Nunber1: "))
#     numb2 = int(input("Nunber2: "))
#     if numb1 == numb2:
#         print("The numbers are equal")
#     elif  numb1 != numb2:
#         result = max (numb1, numb2)
#         result1 = min(numb1, numb2)
#         print(result1, result)
#     else:
#         print("Invalid condition")
# except ValueError:
#     print("Enter the numbers")
# except Exception as error:
#     print("Error")
# finally:
#     print("End")

# task 3
# print("Hello user")
# print("Please enter two numbers")
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (+, -, *, /): ")
#
#     if operation == "+":
#         result = num1 + num2
#         print(result)
#     elif operation == "-":
#         result = num1 - num2
#         print(result)
#     elif operation == "*":
#         result = num1 * num2
#         print(result)
#     elif operation == "/":
#         result = num1 / num2
#         print(result)
# except ValueError:
#      print("Enter the numbers")
# except Exception as error:
#      print("Error")
# finally:
#     print("End")

