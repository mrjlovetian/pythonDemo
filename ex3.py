from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
print "if you don't want that. hit CTRL_C (^C)"
print "if you do want that, hit RETUEN"

raw_input("?")

print "Open the file.."

#'w'表示给予写的权限
target = open(filename, 'w')

print "Truncating the file. Goodbye"

# 清空记录
target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line1 :")

line2 = raw_input("line2 :")

line3 = raw_input("line3 :")

print "I'm going ro write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."

# 相当于保存
target.close()

