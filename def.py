# -*- coding: utf-8 -*-

def print_tow(*args):
	arg1, arg2 = args
	print "arg1 %s, arg2 %s" %(arg1, arg2)


def print_two(arg1, arg2):
	print "arg1 value %s, arg2 value %s" %(arg1, arg2)

print print_tow("小红君", "大脸猫")
print print_two("小老肥", "大帅哥")