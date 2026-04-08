def greater(num):
  return num>10       #return true when condition is pass

l = [10,20,33,40,5]
newl = list(filter(greater,l))   # convert filter object into list
print(newl)

#output
# [20, 33, 40]
