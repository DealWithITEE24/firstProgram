# #result = None
# #needed only within the loop
# #python is dynamically typed language (types can change)
# #second_number> int --> this is called a TypeHint
#
#
#
# print("Hello! This is a simple calculator.")
# print("It can only make + and - operations")
# #first_number: int = int(input("Please enter the first number: "))
# #second_number: int = int(input("Please enter the second number: "))
# #result: int = first_number + second_number
#
# #first_number = int(input("Please enter the first number: "))
# #second_number = int(input("Please enter the second number: "))
#
# # str, int, NoneType
#
#
# #result: int = first_number + second_number
#
# #print(first_number, "+", second_number, "=", result)
#
#
# # String interpolation / insert dynamic values (variables) inside the string
# first_number = int(input("Please enter the first number: "))
# operator: str = input("enter the mathematical operation to run")
# second_number = int(input("Please enter the second number: "))
#
# #if, elif, else
#
# if operator == "+":
#     # == --> is equal? != --> it is not_
#     operation_result: int = first_number + second_number
# #else:
#     #operation_result: int = first_number - second_number
# elif operator == "-":
#     operation_result: int = first_number - second_number
# else:
#     print("this calculator only makes - or +")
#     first_number = int(input("Please enter the first number: "))
#     operator: str = input("enter the mathematical operation to run")
#     second_number = int(input("Please enter the second number: "))
# if operator == "+":# == --> is equal? != --> it is not_
#
#     operation_result: int = first_number + second_number
# #else:
#     #operation_result: int = first_number - second_number
# elif operator == "-":
#     operation_result: int = first_number - second_number
# else:
#     print("this calculator doesn't perform this kind of operation. Please start the calculator again!")
#
# #plus_operation: int = first_number + second_number
# #minus_operation: int = first_number - second_number
#
# #f-string interpolation
# result: str = f"{first_number} {operator} {second_number} = {operation_result}"
#
# # .format() interpolation
#
# #result:str = "{} + {} = {}".format(first_number, second_number, plus_operation)
# #arg = arguments that go inside the methods. grey automatic hints will appear automaticcaly by python
#
# # modulo (%)interpolation
#
# #result: str = "%s + %s = %s" % (first_number, second_number, plus_operation)
#
#
#
#
# #plus_operation: int = first_number + second_number
# #minus_operation: int = first_number - second_number
#
# #f-string interpolation
# #print(operator)
# #result: str = f"{first_number} {operator} {second_number} = {operation_result}"
#
#
# # .format() interpolation
#
# #result:str = "{} + {} = {}".format(first_number, second_number, plus_operation)
# #arg = arguments that go inside the methods. grey automatic hints will appear automaticcaly by python
#
# # modulo (%)interpolation
#
# #result: str = "%s + %s = %s" % (first_number, second_number, plus_operation)
#
#
#
# print(result)