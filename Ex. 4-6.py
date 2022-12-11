#Odd numbers: Use the third argument of the range() function
# to create a list of odd numbers from 1 to 20. Print all the numbers in the for loop.

numbers=[]
for value in range(1,20):
    if value%2>=1:
        numbers.append(value)
print(numbers)