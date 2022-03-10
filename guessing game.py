# Now, we will make a game using loops. We will call this game a guessing game.

# 1

# In this game we take any number, let us suppose this number is number 5.

# 2

# After this we take any number as an input from the user between 1 to 10. The user tries to guess
#  this number.

# 3

# Suppose the user gives 3as an input. We will then check if 3 is equal to 5 or not?

# 4

# 3 is not equal to 5 so we will ask the user for another input.

# 5

# Now, we will check if that number is equal to 5 or not.

# 6

# User will get 5 chances to guess.



# num=6
# i=1
# while i<=5:
#     user=int(input("enter your choice:"))
#     if user==num:
#         print("yeah..your choice is correct,you win;)") 
#         break  
#     else:
#         print("please try again...?")     
#     i+=1    



number_to_guess = int(input("What should the number_to_guess be...:? "))
guesses = int(input("How many guesses.:? "))

guess_any_num = 0
user_guess = int(input("Guess a number: "))
guess_any_num += 1
if number_to_guess < user_guess:
    print("The number is lower than that.")
elif number_to_guess > user_guess:
    print("The number is higher than that")

while user_guess !=number_to_guess and guess_any_num < guesses:
    user_guess = int(input("Guess a number: "))
    guess_any_num += 1
    if number_to_guess < user_guess:
        print("The number is lower than that.")
    elif number_to_guess > user_guess:
        print("The number is higher than that")

if guess_any_num >= guesses and user_guess !=number_to_guess:
    print("You lose; the number was ", number_to_guess)
if user_guess ==number_to_guess:
    print(" WOW..You guess right number...win!")