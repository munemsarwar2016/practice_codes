#We want to sum even numbers 50 to 100

sum_even = 0    # initialize sum_even variable
sum_odd = 0     # initialize sum_odd variable 
i = 50     # starting point

while i <= 100: # Loop runs while i is less than or equal to 100
    if i % 2 == 0 : 
        sum_even += i    # add current value of i to sum_even
    else:
        sum_odd += i     # add current value of i to sum_odd  
    i += 1      # increase i by 1

print("sum value of even from 50 to 100 is: ",sum_even)

print("sum value of odd from 50 to 100 is: ",sum_odd)