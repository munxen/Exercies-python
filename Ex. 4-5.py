#Summing thousands of numbers: Create a list of numbers from 1 to 1000, then use the min() and
# max() functions and make sure that the list really starts with 1 and ends with 1,000,000.
# Call the sum() function and see how fast Python can sum a million numbers.
numbers =list(range(1,1001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))