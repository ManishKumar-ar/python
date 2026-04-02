#///////////////////////////// tuple inside tuple///////////////////////////////////////
tuple1 = (10,20,30,40,"hello", "world", (11,21,31))
print(tuple1[1])
print(tuple1[4])
print(tuple1[6][0])
print(tuple1[6][2])
# output
# 20
# hello
# 11
# 31




#///////////////////////////// list inside tuple///////////////////////////////////////
tuple1 = (10,20,30,40,"hello", "world", [11,21,31])
print(tuple1[1])
print(tuple1[4])
print(tuple1[6][0])
print(tuple1[6][2])
# output
# 20
# hello
# 11
# 31




# //////////////////////////////negative nesting /////////////////////////////////////
tuple1 = (10,20,30,40,"hello", "world", (11,21,31))
print(tuple1[-1])
print(tuple1[-4])
print(tuple1[-1][0])
print(tuple1[-1][-1])
# output
# (11, 21, 31)
# 40
# 11
# 31






tuple1 = (10,20,30,40,"hello", "world", [11,21,31])
print(tuple1[-1])
print(tuple1[-4])
print(tuple1[-1][0])
print(tuple1[-1][-1])
# output
# (11, 21, 31)
# 40
# 11
# 31
