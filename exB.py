from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime
 
doms = ('com', 'edu', 'net', 'org', 'gov')
 
for i in range(randint(5, 10)):
 
    #generate time in string format
    dtint = randint(0, maxint - 1)
    dtstr = ctime(dtint)
 
    #generate user name, length:4~7
    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)
 
    #generate domain name, length:shorter~12
    longer  = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)


print '%s::%s@%s' %(dtstr, em, dn)