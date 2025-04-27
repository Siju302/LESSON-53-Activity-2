# create a new file
new_file = open('newfile.txt', 'r')
new_file.close()

# check if a file exists
import os
print("Checking if my file exists or not....")
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("the file does not exist")

# create a new file if it doesn't
my_file = open("file.txt", "w")
my_file.write("Hi! I am Sijuade and I am 15 years old")
my_file.close()

# delete the old file
os.remove("file.txt")

