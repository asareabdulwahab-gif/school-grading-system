    # # create a list with 5 items
# my_list = ["Apple", "Banana", "Yam", "Rice", "Beans"]

# # listprint the 
# print("my list:", my_list)

# # ask the user to type an item nam
# item_name = input("enter an item name:")

# # print whether the item exitsts in the list or not
# if item_name.capitalize() in my_list:
#     print(f"'{item_name}' exists in the list.")

# else:
#     print(f"'{item_name}'does not exists in the list.")


# def validte_password():
# password = "python123"
# user_input = input("enter password:")
# if user_input == password:
#     print("access granted.")
# else:
#     print("incorrect password access denied")


# def sum_numbers():
# numbers = []
# for i in range(5):
#      num = float(input(f"enter number {i+1}: "))
#      numbers.append(num)
#      break
# # except ValueError:
# print("invalid input. please enter a number.")
# total = sum(numbers)
# print(f"the sum of the number is:{total}")


# def print_even_numbers():
# num = 2
# while num <= 20:
#     print(num)
#     num +=2

# import random

# def guess_the_number():
#     # Computer picks a hidden number between 1 and 10
#     hidden_number = random.randint(1, 10)
#     attempts = 0

#     print("Welcome to the Guess the Number Game!")
#     print("I'm thinking of a number between 1 and 10.")
    
#     while True:
#           "True:"
        
#           guess = int(input("Enter Your Guess: "))
#           attempts += 1
#           if guess < 1 or guess < 10:
#            print("please enter a number between 1 and 10.")
        
# #     attempts -= 1

#     # check if the guess is correct
#     if guess == hidden_number:
#         print(f"Congratulations! You found the number in {attempts} attempts.")
#         # break
#     elif guess < hidden_number:
#         print("Too low! try again.")
#     else:
#          print("Too high! try again.")
# # except ValueError
#     print("Invalid input. please enter a number.")

# play_again = input("Do you want to play again? (yes/no): ")
# if play_again.lower() == "yes":
#     guess_the_number()


# def dictionary_program():
#     word_dict = {
#         "apple": "A sweet, juicy fruit.",
#         "phone": "A device used for communication.",
#         "dance": "To move the body in a rhythmic way.",
#         "smile": "A facial expression showing happiness.",
#         "flute": "A musical instrument.",
#     }
#     word = input("Eter a word: "). lower()
#     if word in word_dict:
#         print(word_dict[word])
#     else:
#         print("Word not found.")


# weight = float(input("enter your weight in kg:"))
# height = float(input("enter your height in meters:"))

# print(f"your weight is:{weight}kg")
# print(f"your height is:{height}meters")

    

# def calculate_bmi(weight, height):
#     bmi = weight / (height*232)
#     return bmi

# def main():
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))

#     bmi = calculate_bmi(weight, height)

#     print(f"Your weight is: {weight} kg")
#     print(f"Your height is: {height} meters")
#     print(f"Your BMI is: {bmi:.2f}")


# def grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"


# score = int(input("Enter your score (0-100): "))
# print(f"Score: {score}, Grade: {grade(score)}")

# import re

# def validate_password(password):
#     if (len(password) >=8 and 
#         re.search("[a-z]", password) and
#         re.search("[A-Z]", password) and
#         re.search(",0-9]", password) and
#         re.search("^A-Za-z0-9]", password)):
#         return "valid"
#     else:
#         return "Invalid"

# print(validate_password("password"))
# print(validate_password("password"))


# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count +=1
#     return count

# print(count_vowels("Hello World"))
# print(count_vowels("AEIOU"))


# def filter_positive(numbers):
#     return list(filter(lambda x:  x > 0, numbers))
# numbers = [-1, 2, 3, 4, 0, 5]
# print(filter_positive(numbers))

# user_age = int(input("please enter your age: "))
# delf_check(a = 17)


# delf_print("welcome you are eligible")
# else_print("please come back nest team")


# WhatsApp-like simple message sender simulation







