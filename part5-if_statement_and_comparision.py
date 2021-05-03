#!/usr/bin/env python3.6

# != not equal

# This scenario allow us to compare a series of numbers

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(10, 20, 30))

# This is a practice exercise

def fish(fish1, fish2, fish3):
    if fish1 == "dog" and fish2 == "chicken" and fish3 == "cat":
        return fish1


print(fish("dog", "chicken", "cat"))
