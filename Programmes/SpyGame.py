def spy_game(nums):
"Write a function that takes in a list of integers and returns True if it contains 007 in order"
    Bond = ''   
    for num in nums:
        if num == 0 or num == 7:
            Bond = Bond + str(num)
    return '007' in Bond