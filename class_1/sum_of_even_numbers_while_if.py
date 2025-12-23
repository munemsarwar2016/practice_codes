#We want to sum even numbers 50 to 100

sum = 0    # initialize sum variable
i = 50     # starting point

while i <= 100: # Loop runs while i is less than or equal to 100
    if i % 2 == 0 : 
        sum += i    # add current value of i to sum
    i += 1      # increase i by 1

print("sum value from 50 to 100 is: ",sum) 