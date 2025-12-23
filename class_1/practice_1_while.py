#concatination using while loop

num_of_input = int(input("How many strings we want to concatenate? ")) #user input from terminal but just for how many strings
 
result=""  #initializing empty string

"""for i in range(num_of_input):
    user_input = input(f"Enter String {i+1}: ") #user input from terminal
    result += user_input #concatenation of the strings
"""

i = 0

while i<num_of_input:
    user_input = input(f"Enter String {i+1}: ") #user input from terminal
    result += user_input #concatenation of the strings
    i+= 1



print("The result is : ", result)


"""For loop and while loop differences

For for loop line 7 to 9 difference between 

for while loop line 12 to 17 difference between"""     
