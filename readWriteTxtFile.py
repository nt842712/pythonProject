file = open('text.txt')

# Read all the contents of file
# print(file.read(8))
# print(file.readline())
# print(file.readline())
line=file.readline()
# file.read()
# file.close()

#while line != "":
 #   print(line)
    # line = file.readline()


for line in file.readlines():
    print(line)


file.close()
