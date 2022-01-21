from operator import floordiv


# foo = int(input("please put a number"))
# foo +=5
# foo -=2
# foo *=4

# print (foo)


# foo = "Cyber Security"

# print(foo[4:6])


# foo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in foo:
#    print(i)


# for b in range(10):
#     print(b)
#     for i in range(9, -1, -1):
#         print(i)


# myList = ["item1", "item2", "item3", "item4"]

# if "item1" in myList:
#     print("its in the list")
# else:
#     print("its not in the list")

# while True: 
#     my_num_list = [1, 2, 3, 4, 5]
#     bar = input("put a number")
#     # if int(bar) in my_num_list:
#     #     print("it is correct")
#     # else:
#     #     print("try again")

#     # ternary conditional operator
#     output = "it is correct" if int(bar) in my_num_list else "it is not correct"
#     print(output)
    

guess_game = True

while guess_game:
    num = input("Please guess a number.\n")
    if int(num) == 3:
        print("You got it!")
        guess_game = False
