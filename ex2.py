from sys import argv

script, filename = argv

txt = open(filename)

print "here's your file %r:" %filename

print txt.read()

print "type the file again:"

file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()



