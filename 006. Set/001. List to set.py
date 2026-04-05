list1 = [1,2,3,4,5,6,5,7,2,2,2,3]                      #here we generate list that contain duplicate also
print(type(list1))    
print(len(list1))                     # give length of list
set_1 = set(list1)                     # convert into the set
print(set_1)
print(len(set_1))           #give len of set after duplicate remove'

#output
# <class 'list'>
# 12
# {1, 2, 3, 4, 5, 6, 7}
# 7
