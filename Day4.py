# user_name = input("What is your name?")
# user_age = int(input("What is your age?"))
# print(user_name, user_age + 1)
# if user_age == 100:
#     print("Congratulations you are going to be 100")

# i = 0
# num_list = []
# while i < 4:
#     user_question = int(input("Please put a number?"))
#     i += 1
#     num_list.append(user_question)
#
# num_average = sum(num_list)/len(num_list)
# print(round(num_average, 2))


# i = 0
#
# while i < 101:
#     i = i + 1
#     print(i)

# def add(num):
#     return num + 5
#
#
# print(add(5))


# NUMBER = 10

# guess = True

# while guess:
#     try:
#         user_question = int(input("Please put a number?"))
#         if user_question > NUMBER:
#             print("Your number is too high")
#         elif user_question < NUMBER:
#             print("Your number is too low")
#         else:
#             print("That's correct!")
#             guess = False
#     except ValueError:
#         print("Warning ! Put a number not a world or character")

# x = ["a", "b", "c", "d"]
# print(len(x))
# print(x[0])
# print(x[1])

# for char in x:
#     print(char)

# import random

# print(random.randrange(0,10))


# import random

# random_number = random.randint(1, 6)

# def dice():
#     return random_number

# print(dice())

# import camelcase

# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

# try:
#     user_num = int(input("please put a number"))
#     print(user_num / 0)
# except ZeroDivisionError:
#     print("You can't divide by 0")



# try:
#     string = "Bundoora"
#     num = 5
#     result = string + num
#     print(result)

# except TypeError:
#     print("can only concatenate str to str")

# with open("test.txt","r") as file:
#     content = file.read()
#     print(content)
    
# with open("test.txt","r") as file:
#     content = file.readlines()
#     print(content)
#     print(content[2])

# with open("test.txt","r") as file:
#     content = file.read()
#     print(content)

# my_list = content.split()
# print(my_list)

# for i in my_list:
#     print (i)

with open("myFile.txt", "w") as File:
    content = File.write("this has been written")
    print(content)