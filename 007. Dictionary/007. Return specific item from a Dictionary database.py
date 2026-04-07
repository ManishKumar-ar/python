# Description
# Write code to fetch the profession of the employee with Employee id - 104 from an employee input given in the form of a dictionary where key represent employee id and values represent the name, age, and profession (in the same order).
# Sample input:
# Employee_data = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}
# Sample output:
# 'Product Lead'

Employee_data = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}

########## method - 1 #################################################
list2 = Employee_data.get(104)
print(list2)
print(list2[2])

########## method - 2 #################################################

print(Employee_data.get(104)[2])

########## method - 3 #################################################

print(Employee_data[104][2])



###########################output###########################################################
# ['Ansari', 29, 'Product Lead']
# Product Lead
# Product Lead
# Product Lead
