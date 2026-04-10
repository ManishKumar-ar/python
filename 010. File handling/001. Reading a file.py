############ method - 1 ################################
file = open('manish.txt', 'r')              # here we create  session to read file
for linestatement in file:                   # create for loop to read the file
    print(linestatement)

# #####outout #########
# this is manish prajapati
# i am a new teacher here



############ method -  2 ################################
file = open("manish.txt", "r")
print(file.read())
# #####outout #########
# this is manish prajapati
# i am a new teacher here
