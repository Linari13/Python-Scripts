def has_33(nums): 
"Given a list of ints, return True if the array contains a 3 next to a 3 somewhere."   
    res = False
    ind = 0
    while ind in range(len(nums)-1):        
        if nums[ind] == 3 and nums[ind+1]==3:
            res = True
        ind += 1
    return res