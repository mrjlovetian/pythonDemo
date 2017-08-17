from sys import argv

#判断文件是否存在
from os.path import exists

# 多个参数输入
script, from_file, to_file = argv

print "please input from_file %s and to_file %s" %(from_file, to_file)

# 打开文件
in_file = open(from_file)

# 文件读取
indate = in_file.read()

print "the input file is %d byte long" %len(indate)

print "Does the output file exist ? %r" %exists(to_file)

print "ready hit renturn to countine, CTRL-C to abort"

raw_input()

out_file = open(to_file, 'w')

out_file.write(indate)

out_file.close()

in_file.close()