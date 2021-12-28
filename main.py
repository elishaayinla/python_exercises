# Write a python program that accepts the radius of a circle from the user and compute the area
# user_input = input("Please, enter the radius of the circle\n")
# r = float(user_input)
# area = 3.14*r*r
# print(f'The area of the triangle is {area}')

# this program converts degree to radian
# user_input = input("Kindly input the value of the degree to be converted to radian\n")
# value = float(user_input)
# radian = value * 3.142/180
# print(f'{value} degrees to radian is {radian} radian')

# This program converts radian to degrees

# user_input = input('Please enter the value in radian to be converted to degrees\n')
# radian = float(user_input)
# degree = radian * 180/3.142
# print(f'{radian} rad is {degree} degrees')

# method 2
# pi =22/7
# radian = float(input('Input radians:'))
# degree = radian * (180/pi)
# print (degree)

# Calculation for area of a trapezium
# a = float (input('input first side:\n'))
# b = float(input('input second side:\n'))
# L = float(input('input Length:\n'))
# area = 0.5 * (a+b)*L
# print(area)

# Accepts ones first name and last name and print it in reverse
# first_name = input('What is your first name?\n')
# last_name = input('What is your last name?\n')
# print(f'{last_name} {first_name}')
# print ('Hello ' +last_name+ ' '+first_name+'!')

# Exercise 1: Given two integer numbers return their product.
# If the product is greater than 1000, then return their sum
# print('This programme calculates the product of 2 integers whose product is less than 1000')
# first_int = input("Enter the first number:\n")
# second_int = input("Enter the second number:\n")

# int1 = int(first_int)
# int2 = int(second_int)
# product = int1 * int2
# sum1_2 = int1 + int2

# def both_prods():
# if product > 1000:
#   print(f"The sum of {int1} and {int2} is {sum1_2}.")
# else:
#   print(f"The product of {int1} and {int2} is {product}")

# both_prods()
# current_num = input("Enter the value of any number to calculate the next 10 numbers; addition of current and previous "
#                    "number\n")
# current_int = int(current_num)
# init_num = current_int-1
# sum_ini_cur = current_int + init_num
# print(f"current number: {current_int} initial number:  {init_num} sum: {sum_ini_cur}")

# def sumNum(num):
#    previousNum = 0
#    for i in range(num):
#        sum = previousNum + i
#        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
#        previousNum = i

# print("Printing current and previous number sum in a given range(10)")
# sumNum(10)

# import random

# number = random.randint(1, 25)

# number_of_guesses = 0

# while number_of_guesses < 9:
#   print('Guess a number between 1 and 25:')

#  guess = input()
# guess = int(guess)

# number_of_guesses = number_of_guesses + 1

# if guess == number:
#   break

password1 = input("what is your password1?\n")
password1_confirm = input("Please confirm your password1:\n")
while password1 == password1_confirm:

    password1 = input("what is your password1?\n")
    password1_confirm = input("Please confirm your password1:\n")

    print(f"Your password is {password1}")

print("your password does not match!")

#################################################

while True:
    password = input("What is your password?\n")
    password_confirm = input("Please confirm your password\n")
    if password == password_confirm:
        break
    print("Your password does not match!")
print(f"Your pass is {password}")
