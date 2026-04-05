A = {0,2,4,6,8}
B = {1,2,3,4,5}

#union()
print(A | B)                         #method - 1
print(A.union(B))                    #method - 2
print(len(A.union(B)))

#intersection()
print(A & B)                        #method - 1
print(A.intersection(B))            #method - 2


#difference
print(A - B)                        #method - 1
print(A.difference(B))              #method - 2

#symmetric difference
print(A ^ B)                      #method - 1


#output
# {0, 1, 2, 3, 4, 5, 6, 8}
# {0, 1, 2, 3, 4, 5, 6, 8}
# 8
# {2, 4}
# {2, 4}
# {0, 8, 6}
# {0, 8, 6}
# {0, 1, 3, 5, 6, 8}
