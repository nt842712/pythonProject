# file=open('text.txt')
# read file and store all the lines in list

with open('text.txt' , 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt' , 'w') as writer:
        for line in reversed(content):
            writer.write(line)



