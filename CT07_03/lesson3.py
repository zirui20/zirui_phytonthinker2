
# ## Task 1: Study Timer
# **Task: Write a program that acts as a study timer**
# 1. The user must input how many minutes they plan to study
# 2. Use a while loop to count down the minutes
# 3. Display "Good job!" once the timer is up

# Hint: you will need the time.sleep(). However this function
# only takes in seconds.
# You will need to write a conversion algorithm to change
# minutes to seconds.


# import time
# study_time = int(input("how long do you want to study for? "))
# while True:
#     if study_time <= 0:
#         print("good job!")
#         break
#     print(f"{study_time} mins left")
#     time.sleep(3)
#     study_time -= 1

#     # mins = study_time 
#     # print(study_time)


# ## Task 2: Allowance Savings Tracker
# **Task: Write a program to track how much you save, and
# inform you when your savings is more than $100**
# 1. Create a variable called savings
# 2. Using a while loop, ask how much money you save every
#    day
# 3. While savings is less than 100, you continue to save
# 4. Exit the program when savings is more than 100 and
#    congratulate the user.

# import time
# savings = 0
# amount = input("how much did you save today? ")
# while True:
#     if savings >= 100:
#         print("good job, you have saved 100 dollars!")
#         break
#     time.sleep(1)
#     savings += amount


# ## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"

import random 
questions = 15
lives = 3
num1 = random.randint(2,20)
num2 = random.randint(2,20)
for count in range(15):
        input("what is", str(num1), "x", str(num2),"?")

