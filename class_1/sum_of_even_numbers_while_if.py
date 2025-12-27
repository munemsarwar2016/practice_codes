# We want to sum even numbers from 50 to 100

sum = 0      # initialize sum variable
i = 50       # starting point

while i <= 100:          # loop until 100
    if i % 2 == 0:       # check if number is even
        sum += i         # add even number to sum
    i += 1               # increase i by 1

print("sum of even numbers from 50 to 100 is:", sum)
