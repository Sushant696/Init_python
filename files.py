# Open the source file for reading
source_file = open("a.txt", 'w+')
source_file.write('written into the file')
source_file.close()

anotherfile = open("b.txt")
print('hello')

# # Write the contents to the destination file
# destination = open('b.txt', 'w+')
# destination.write(file_contents)
# destination.close()

# destination = open("a.txt",'r')
# data = destination.read()
# destination.close()