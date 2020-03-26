def multiply(numbers):
    
    """ multiply all the numbers in a list """

    from functools import reduce
    
    return reduce(lambda x,y:x*y, numbers)