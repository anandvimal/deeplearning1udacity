'''
just a small example to show we cant do calculations with big decimals in python
'''
total = 0
value = 1000000000
small_increment = 0.000001
total_number_of_increments = 1000000


total = total + value

for i in range(total_number_of_increments):
    #print(i)
    total = total + small_increment

total = total - value

#total should be 1. but we got 0.95367431640625
print(total)
