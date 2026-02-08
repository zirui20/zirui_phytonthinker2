## Recap 1: Pseudocode (Recycling logic)
# Task: Write down the steps on how to solve the problem below

# Design pseudocode for a recycling robot that sorts items
# into bins for glass, plastic, and paper. The robot should
# check each item's material and place it in the correct bin.

# create a variable for glass bin, plastic bin and paper bin.
# robot print("what are you recycling today?")
# user input "glass" glass will be stored in glass bin
# user input "plastic" glass will be stored in plastic bin
# user input "paper" glass will be stored in paper bin
# each item will be stored in specific variables




## Recap 2: Variables & Mind map
# Use mindmap to think about the number of variables you need for
# the following. Then, create a program that does the following:

# You just had lunch at a sushi restaurant and have to calculate
# the total amount you have spent. Different coloured plates
# costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates,
# and 4 green plates. Calculate and print the total amount you
# have spent:

# green_plate = 3
# blue_plate = 2
# red_plate = 1

# green = green_plate*4
# blue = blue_plate*5
# red = red_plate*3

# total = green + blue + red
# print("the total amount is",total, "dollars" )

# ask the user for the number of plate for red, blue and green
# red = int(input("how many red plates have you eaten? "))
# blue = int(input("how many blue plates have you eaten? "))
# green = int(input("how many green plates have you eaten? "))

# amount_red = red*1
# amount_blue = blue*2
# amount_green = green*3

# total_amount = amount_blue + amount_red + amount_green

# print("the total price is :", total_amount, "dollars")

## Recap 3: Debugging Average Score Program
# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:

score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two + score_three

average_score = (total / 3)

student_name = "Alex"

# print("Average score for " , student_name + " is: " , average_score)
print("Average score for " + student_name + " is: " + str(average_score))

## Recap 4: If..elif..else & Flowchart
# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.

score = input("what score did you get? ")


if score >=75 :
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("fail")

