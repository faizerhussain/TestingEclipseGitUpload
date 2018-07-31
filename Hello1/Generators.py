def gen123():
    yield 1
    yield 2
    yield 3
    return

g=gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))

print("##########")
    
for v in gen123():
    print(v)
