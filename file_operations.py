# Operations with external files.
# Operations like open, write inside file, edit the file, create, delete.
# CSV, JSON, TXT ...
# ----------------------------------------------------------
# greeting_file = open("greeting.txt", "r")
#
# print(greeting_file.read())
#
# greeting_file.close()   -   NEED TO CLOSE FILE IF OPENED
# ----------------------------------------------------------
# with open("greeting.txt") as greeting_file:
#     greeting = greeting_file.read()
#
# print(greeting) # - CLOSES OPENED FILE AUTOMATICALLY
# ----------------------------------------------------------
# with open("greeting.txt", "w") as greeting_file:
#     greeting = greeting_file.write("Hello, Estonia!")
#
# with open("greeting.txt", "r") as greeting_file:
#     print(greeting_file.read())   -   CHANGES THE FILE AND PRINTS IT OUT IN TWO STEPS
#-----------------------------------------------------------
# with open("greeting.txt", "w") as greeting_file:
#    greeting = greeting_file.write("Hello, Estonia!\n")
#
# with open("greeting.txt", "r") as greeting_file:
#     greetings = greeting_file.readlines()
#     for line in greetings:
#         word = line.split()
#         print(word)  - SPLIT
# ----------------------------------------------------------
# with open("greeting.txt", "a") as greeting_file:
#     greeting = greeting_file.write("Hello, Estonia!\n")
#
# with open("greeting.txt", "r") as greeting_file:
#     greetings = greeting_file.readlines()
#     for line in greetings:
#         print(line)
# ---------------------------------------------------------
result = 4 + 3

with open("greeting.txt", "a") as greeting_file:
    greeting = greeting_file.write(f"{str(result)}\n")

with open("greeting.txt", "r") as greeting_file:
    greetings = greeting_file.readlines()
    for line in greetings:
        print(line)


