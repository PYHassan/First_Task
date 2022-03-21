"""a Python function that generates the output of a lottery game (it should return a list)"""
import random

def lottery_withdrowal():
    # balls is a list from 1 to 50
    balls = list(range(1, 51))
    #choosed_balls are the selected balls
    choosed_balls = random.sample(balls, 10)
    # Sorting the selected balls
    choosed_balls.sort()
    return choosed_balls

# Test the script
print(lottery_withdrowal())

# Test Results
# [3, 7, 11, 27, 30, 31, 32, 34, 38, 48]

# We can use unit test to :
# make sure that all numbers are within the range.
# check that the return list has correct length.
# the list is sorted correctly.  
