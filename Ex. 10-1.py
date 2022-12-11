#Learning Python: Open an empty file in a text editor and write a few lines of text about the possibilities 
# Python. Each line should start with the phrase: "In Python you can..." Save the file under the name 
# learning_python.txt in the catalog used for the examples in this chapter. Write a program that 
# reads the file and outputs the text three times: with reading the entire file, with iterating through the lines of the file object and with 
# saving rows in the list and then displaying the list outside the with block.

with open('C:/Users/proro/Desktop/python/Delete/python_text.txt') as file:
    content=file.read()
print(content)
with open('C:/Users/proro/Desktop/python/Delete/python_text.txt') as file:
    for line in file:
        print(line.rstrip())
with open('C:/Users/proro/Desktop/python/Delete/python_text.txt') as file:
    lines = file.readlines()
for rline in lines:
    print (rline.strip())


    