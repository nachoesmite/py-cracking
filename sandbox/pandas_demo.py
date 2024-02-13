# from numpy.random import default_rng
# from pandas import Series, DataFrame
from random import randint, choice
from string import ascii_lowercase
# rng = default_rng(0)
# print(type(rng.integers(-10,10,size=5)))
# s = Series(rng.integers(-10,10,size=5))
# print(s)

# for x in s.items():
#     print(f'{x =}')

# for _, x in s.items():
#     print(f'{x =}') 

# for x in s:
#     print(f'{x =}')

# df = DataFrame(rng.integers(-10,10,size=(5,3)),columns=list('abc'))

# print(df)

# for x in df: print(f'{x =}')

d = {choice(ascii_lowercase):randint(1,100) for _ in range(10)} 
print(d)