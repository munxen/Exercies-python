#Triples: Create a list of numbers that are multiples of 3, ranging from 3 to 30. Print all the numbers in your list
# in the for loop
nums=[]
for num in range(3,31):
    if num%3==0:
        nums.append(num)
print(nums)
