fo = open('test.txt','w') # write mode
print('name ',fo.name)
print('isclosed',fo.closed)
print('mode',fo.mode)

fo.write(' i am indian')
fo.write(' and lives in Hyd')
fo.close()

fo = open ('text2.txt','w') # append mode
fo.write('in tolichowki')
fo.close()
print('executed')

fo= open('test.txt','r+')
text= fo.read()
text2= fo.read(10)
print(text)
print(text2)

fo = open ('text3.txt','w+') # append mode
fo.write('in tolichowki')
fo.close()
