def unique_list(lst):
""" returns a new list with unique elements of the input list"""

    UniqList = []
    
    for elem in lst:
            if elem not in UniqList:
                UniqList.append(elem)
    return UniqList