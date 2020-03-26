def blackjack(a,b,c):
"Given three integers between 1 and 11"
"If their sum is less than or equal to 21, return their sum."
"If their sum exceeds 21 and there's an eleven, reduce the total sum by 10."
"Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'"
    total = a+b+c
    if total > 21 and (a or b or c == 11):
        total -= 10
    if total > 21:        
        total='BUST'
    return total