# Addition: when entering numeric data, a typical problem often occurs: the user enters text instead of 
# of numbers. When trying to convert data to int, a TypeError exception occurs. Write a program that 
# requests two numbers, adds them together and outputs the result.Catch the TypeError exception if any
# of the input values is not a number, and output a convenient error message. Test your 
# program: first, enter two numbers, and then enter text instead of one of the numbers.

while True:
    print ("Enter two numbers for sum ")
    print ("\nIf you want to exit,enter 'q'")
    first_num =input ("\nFirst number: ")
    if first_num == 'q':
        break
    second_num =input ("Second number: ")
    if second_num == 'q':
        break
    try:
       answer = int(first_num) + int(second_num)
    except ValueError:
     print ("Please, use numbers (1,2,3...245)")
    else:
     print (answer)

