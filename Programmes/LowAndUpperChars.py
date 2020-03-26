def up_low(s):

""" calculates the number of upper case letters and lower case letters"""

    UpChar = LoChar = 0
    
    for char in s:
        if char.isalpha() and char.isupper():
            UpChar+=1
        elif char.isalpha():
            LoChar+=1
    print ('Original String :  Hello Mr. Rogers, how are you this fine Tuesday?')
    print (f'No. of Upper case characters :  {UpChar}')
    print (f'No. of Lower case characters :  {LoChar}')