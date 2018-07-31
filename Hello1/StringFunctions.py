from _operator import pos
from macpath import join
myStr ='Hello World'

print(myStr.capitalize())
print(myStr.swapcase())
print(len(myStr))
print((myStr.replace('World', 'every1')))

subString ='l'
print(myStr.count(subString))

print(myStr.startswith('Hello'))
print(myStr.endswith('d'))

#string to list

print(myStr.split())

#position of subString
print(myStr.find('World'))
print(myStr.find('e')) # gives -1 if not found

print(myStr.index('e')) # gives error if not found

#check alphanumeric
print(myStr.isalnum())

#check alphanbetic
print(myStr.isalpha())

"""from plural
"""

print("unforgetable".partition("forget"))
afterPartition=depart,separator,arrival="Hyd:bbsr".partition(':')
print(afterPartition)

print("the age of {} is {}".format('Faiz', 20))
print("the age of {0} is {1}".format('Faiz', 20))

position=(62.2,86.4,34.9)
print("Galatic postion x={position[0]} x={position[0]} x={position[0]}".format(position=position))


import math
print("Math constants: pi={m.pi} and e={m.e}".format(m=math)) 

colors=";".join(['a2#','b3#','c2$'])
print(colors)
colors.split(';')
print(colors)

print(''.join(['a','b','c']))


print('####################################')

#h='mera naam faizer hai  aur main hyderabad me rehta hu'.split()

h='mera nam hai hyderabad me rehta '.split()
h.sort(key=len)
print(h)

print(' '.join(h))


print('####################################')

x=[5,2,7,3]
y=sorted(x)
print(y)
print('####################################')

x=[5,2,7,3]
y=reversed(x)
print(list(y))





 



#
