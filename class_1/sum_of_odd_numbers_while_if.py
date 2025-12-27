# We want to sum odd numbers from 50 to 100

sum = 0      # initialize sum variable
i = 50       # starting point

while i <= 100:           # loop from 50 to 100
    if i % 2 != 0:        # check if number is odd
        sum += i          # add odd number to sum
    i += 1                # increase i by 1

print("sum of odd numbers from 50 to 100 is:", sum)
