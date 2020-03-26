"""It could bve important to know how long the code is taking to run,
or at least if a particular line of code is slowing down the entire project"""

import timeit

print("-".join(str(n) for n in range(100)))
# pour savoir le temps en secondes que cette ligne prend pour tourner 10000 fois on rentre
print("for loop : ",timeit.timeit(("-".join(str(n) for n in range(100))), number=10000))
print("Map function : ",timeit.timeit(("-".join(str(n) for n in range(100))), number=10000))

