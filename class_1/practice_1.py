#concatination using for loop

num_of_input = int(input("How many strings we want to concatenate? ")) #user input from terminal but just for how many strings
 
result=""  #initializing empty string

for i in range(num_of_input):
    user_input = input(f"Enter String : ") #user input from terminal
    result += user_input #concatenation of the strings


print("The result is : ", result)
