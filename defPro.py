from sys import argv

script, input_file = argv

def printall(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

curre_file = open(input_file)

# print printall(curre_file)

print rewind(curre_file)

# print print_a_line(1, curre_file)