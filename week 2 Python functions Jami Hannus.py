# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:51:30 2021

@author: Jami

1.Write a function that converts from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds in the main program.
2.Write a Python function to sum all the numbers in a list
3.Write a Python function to check whether a number is in a given range.
4.Write a Python function that takes a number as a parameter and check the number is prime or not. Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
5.Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
1
"""
print("Task 1")
print("Function that converts from kilograms to pounds.")
print("Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.")
print("Lastly, print the resulting array of weights in pounds in the main program.")
weight_kg = float(input("Please imput your weight in kilograms, you have 2 seconds then programm will use 70kg:"))
if not weight_kg:
    weight_kg = 70
weight_lb = 2.2*weight_kg
print("Your weight is ",weight_kg,", your weight in lbs is",weight_lb,)
print("\n")
print("Task 2")
print("Write a Python function to sum all the numbers in a list \n")
try:
    userdata = []  
    while True:
        userdata.append(int(input("Please type list of numbers.Defult list is:1 2 3 4 5.Use number then enter, leave input empty when want to stop:")))     
except:
    if not userdata:
        userdata=[1,2,3,4,5]
    Sum=sum(userdata)
    print("Your numbers are",userdata,"Added together they are:",Sum)
    
print("Task 3")
print("Simple program to test if input number is in range")
user_range_start = int(input("Please type in the range starting number:"))
user_range_end = int(input("Please type in the range ending number:"))+1
user_test_number = int(input("Please type in the number you want to test:"))

user_range = range(user_range_start,user_range_end)
is_in_range = user_test_number in user_range
print("Your",user_range, "and number what you picked is",user_test_number)
if is_in_range:
    print("Your number is inside the range")
else:
    print("Your number is not inside the range")
    
print("Task 4")
user_prime_number = int(input("Please type number you check if its a prime or not:"))
if user_prime_number > 1:
    for i in range(2,user_prime_number):
        if(user_prime_number % i) == 0:
            print(user_prime_number,"not a prime as")
            print(i," * ",user_prime_number//i,"equals",user_prime_number)
            break
    else:
        print(user_prime_number,"is a prime number")
        
print("Task 5")
print("Programm will test if inputed string is palindrome, same in reverse like madam")
user_string = str(input("Please input a string palindrome:"))
user_string_reversed = user_string[::-1]
is_palindrome =  user_string == user_string_reversed
print("Your string is",user_string,"and in reverse its",user_string_reversed)
if is_palindrome:
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")