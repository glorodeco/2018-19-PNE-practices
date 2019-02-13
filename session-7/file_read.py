# Example of reading file located in our filesystem

NAME = "mynotes.txt"
# Open the file

myfile = open(NAME, 'r')

print('File opened: {}'.format(myfile.name))


contents = myfile.read()

print("The file contents are: {}".format(contents))