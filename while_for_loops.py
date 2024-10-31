# while loops = execute some code WHILE some condition remains true

#This is known as i'teration = loop     (iterate) this is the verb form, meaning that we are looping through it
# name = input("Enter your name: ")
# while name == ' ':
#     print("you did not enter your name")
#     name = input("Enter your name: ") #IF this is removed then we get an infinite loop which is bad

# print(f"hello {name}")

# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"you are {age} years old")

# food = input("Enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like (q to quit): ")

# print("bye")


# num = int(input("Enter a number between 1-10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1-10: "))

# print(f"your number is {num}")

# for loops = execute a block of code a fixed number of times
#             you can iterate over a range, string, sequence, etc. 



# for x in reversed(range(1,11, 2)):
# #     print(x)
# # print("happy new year!")
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x ==13 :
#         break
#     else:
#         print(x)

# # create a list of 
# horror_characters = ("freddy cougar", "jason voorhees", "Micheal myers", "pennywise", "chucky" )
# for x in horror_characters:
#     # if x == "Micheal myers" :
#     #     continue
#     # print(x)
#     if x == "freddy cougar":
#         x = "Dracula"
#     print(x)

horror_movie = ("Scream", "The skinning","Long legs","IT")
for movie in horror_movie:
    if movie == "IT":
        break
    elif movie =="The skinning":
        movie = "Halloween"
    print(movie)
    