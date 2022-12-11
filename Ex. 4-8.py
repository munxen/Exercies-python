#Cubes: The result of raising a number to the third power is called a cube. For example, cube 2 is written in the language
#Python in the form of 2**3. Create a list of the first 10 cubes (that is, cubes of all integers from 1 to 10) and 
# output the values of all cubes in the for loop.
nums=[]
for value in range(1,10):
    nums.append(value**3)
print(nums)