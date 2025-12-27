# We want to sum even and odd numbers from 50 to 100

even_sum = 0   # sum of even numbers
odd_sum = 0    # sum of odd numbers

i = 50         # starting point

while i <= 100:            # loop from 50 to 100
    if i % 2 == 0:         # check if number is even
        even_sum += i      # add even number
    else:                  # otherwise number is odd
        odd_sum += i       # add odd number
    i += 1                 # increase i by 1

print("sum of even numbers from 50 to 100 is:", even_sum)
print("sum of odd numbers from 50 to 100 is:", odd_sum)
