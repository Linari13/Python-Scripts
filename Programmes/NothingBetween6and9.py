def summer_69(arr):
"Return the sum of the numbers in the array"
"Ignore sections of numbers starting with a 6 and extending to the next 9"
"(every 6 will be followed by at least one 9)."
" Return 0 for no numbers."

    total=0
    flag = True
    for number in arr:
        if number!=6 and flag == True:
            total = total + number
        else :
            flag = number==9
        print (flag)             
    return total