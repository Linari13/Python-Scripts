""" Defaultdict is a dictionary like object which provides all methods
 provided by dictionary but takes first argument (default_factory)
  as default data type dfor the dictionary.
Using defaultdict is faster than doing the same using dict.set_default method.

A defaultdict will never raise a KeyError.
Any key that does not exist gets the value returned by the default factory.
"""


from collections import defaultdict

d = {'K1':1} #On créer un dictionaire normal
print('Si on appelle K1, on aura la valeur 1')
print(d['K1'])

"""print('Si on appelle K2, qui n\'exite pas on aura une KeyError')
d['k2']"""

#using the defaultdict we set the unexisting key entered as default
d = defaultdict(object)
d['one']

for item in d:
    print (item)

print('Using a lambda fonction we can assign \na default value to these unexisting (default)keys.')

d = defaultdict(lambda : 0)
d['one']
d['two']
print(d)