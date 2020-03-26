def ran_check(num,low,high):

""" checks whether a number is in a given range (inclusive of high and low)"""

    if num in range(low,high):
        print (f'{num} is in the range between {low} and {high}')
    else:
        print (f'{num} is not in the range between {low} and {high}')

def ran_bool(num,low,high):
"""return a boolean whether a number is in a given range (inclusive of high and low)"""
    return num in range(low,high)