#Write a python programme to count the number of even & odd number from a series of numbers.


lst = [15, 12, 16, 25, 30, 32, 37]
 
even_count, odd_count = 0, 0
 
# iterating each number in list
for element in lst:
 
    # checking condition
    if element % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
 
print("Total Even number:-", even_count)
print("Total Odd number:-", odd_count)