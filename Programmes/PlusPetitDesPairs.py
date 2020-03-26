def lesser_of_two_evens(a,b):
    
    "returns the lesser of two given numbers if both numbers are even"
    "returns the greater if one or both numbers are odd"
    
    if a%2 == 0 and b%2 == 0:
        return min (a,b)
    else :
        return max (a,b)