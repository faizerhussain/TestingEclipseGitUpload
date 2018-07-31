from math import *
from pprint import pprint as pp
from getpass import fallback_getpass


'''list compre'''
words= "my name is anthony gulsavez main duniya me akela hu".split()
print(words)
print([len(word) for word in words])

f=[len(str(factorial(x))) for x in range(20) ]
print(f )

print("################")
'''set compre'''

f={len(str(factorial(x))) for x in range(20) }
print(f )

'''dict compre'''

country_to_capital={'UK':'London','Brazil':'Braizilia','Morocoo':'Rabat','Sweden':'Stockholm'}
capital_to_country={capital:country for country,capital in country_to_capital.items()}
pp(capital_to_country)


def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x% i ==0:
            return False
    return True
        



c=[x for x in range(101) if is_prime(x)]

print(c)
