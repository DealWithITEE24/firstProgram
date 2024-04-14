# # Boolean = True || /
# # | = "or"
# # & = "and"
# # for the if/else statements we are evaluating the expressions as "truth" or "false"
#
# # users_name = "Victoria"
# # short_name = users_name[3:8]
#
# print("Hello! This is a simple calculator.")
# print("It performs basic mathematical operations")
#
# # first_number = float(input("Please enter the first number: "))
# # operator: str = input("enter the mathematical operation to run")
# # print(f"my chosen operator: {operator}")
# # operator = operator[0]
# # second_number = float(input("Please enter the second number: "))
#
# first_number: str = input("Please enter the first number: ")
# operator: str = input("enter the mathematical operation to run")
# print(f"my chosen operator: {operator}")
# operator = operator[0]
# second_number: str = input("Please enter the second number: ")
#
# if first_number.isdigit():
#     print("Yes its a digit")
#
# else:
#     exit("Not a digit. exiting...")
#
# # if first_number.isdigit():
#     # print("Yes its a digit")
#
# # if not first_number.isdigit():
#     # exit("Not a digit. exiting...")
#
# if operator == "+":
#     operation_result: int = int(first_number) + int(second_number)
#
# elif operator == "-":
#     operation_result: int = int(first_number) - int(second_number)
#
# elif operator == "*":
#     operation_result: int = int(first_number) * int(second_number)
#
# elif operator == "/":
#
#     operation_result: float = int(first_number) / int(second_number)
# # for the division it has to have FLOAT data type hint
# else:
#     exit("Wrong operator")
#
# operation_result: float = round(operation_result, 2)
#
# result: str = f"{first_number} {operator} {second_number} = {operation_result}"
#
# print(result)