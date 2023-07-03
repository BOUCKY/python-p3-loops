#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    square_num = [x**2 for x in int_list]
    return(square_num) 

def fizzbuzz():
    num = 0
    while num < 100:
        num += 1
        # Have to do AND first otherwise if smaller one (5 or 3) is true, it will cancel this one out
        if (num % 3 == 0 and num % 5 == 0):
            print('FizzBuzz')
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
