str = 'Спанч Боб Square Pants!'

slovo = 'Боб'
a = str.find(slovo)
srez = str[a:a + len(slovo)]
print(srez)


str = 'My name is Patrick sadfas. My name is Bob sapgjagj s dfj'
names = str.count('name is ')
findnames = 0
c = 0
while findnames < names:
    a = str.find('name is ', c)
    b = len('name is ')
    c = str.find(' ', a + b)
    srez = str[a + b: c]
    print(srez)
    findnames += 1

text = ['hello my id #123456, my cats id #qwe123, bye', 'hello my id #123456 my cats id #qwe123 bye']

for i in text:
    ids = i.count('#')
    findids = 0
    c = 0
    a = 0
    b = 7
    while findids < ids:
        a = i.find('#', c)
        c = a + b
        srez = i[a : a + b]
        print(srez)
        findids += 1


