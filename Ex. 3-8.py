# See the world: Think of at least five countries you would like to visit.
# Save the country names in the list. Make sure that the list is not stored in alphabetical order.
# Output the list in the original order. Don't worry about the design of the list, just output it as 
# regular Python list.
#Use the sorted() function to output the list in alphabetical order without changing the list.
# Print the list again to show that it is still stored in the original order.
# Use the sorted() function to output the list in reverse alphabetical order without changing the order of the original
#of the list.
# Output the list again to show that the original order has not changed.
#Change the order of the elements by calling reverse(). Output a list to show that the elements follow in 
# in a different order.
#Change the order of the elements by calling reverse() again. Print the list to show that the list is back 
# to the original order.
# Sort the list in alphabetical order by calling sort(). Output a list to show that the elements 
# follow in a different order.
#Call sort() to rearrange the list items in reverse alphabetical order.
#Output a list to show that the order of the elements has changed.

countries = ['japan','france','usa','italy','canada']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries,reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)