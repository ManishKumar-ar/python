t = (2,3,8,5,4,1)
new_var = sorted(t)
print(new_var)       #this is new list, not a tuple
print(type(new_var))

t2 = tuple(new_var)         # here we typecast back to tuple
print(t2)
print(type(t2))

# output
# [1, 2, 3, 4, 5, 8]
# <class 'list'>
# (1, 2, 3, 4, 5, 8)
# <class 'tuple'>
