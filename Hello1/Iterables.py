iterable= ['spreing','sdummer','autumn','winter']
iterator=iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    raise ValueError("Iterator is finished")
    
