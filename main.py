str = 'hello world'
print(len(str))
print(str[6])
# str[6]='#' это не работает!!!
# print(str)

print(str.count('o'))
print(str.find('world'))

str1 = str.replace('hello', 'privet').replace('world', 'kot')
print(str)
print(str1)

gubka = '''
Вы готовы дети
- Да, Капитан!
-Я не слыыышуууу!
-ТАК ТОЧНО, КАПИТАН!

Ктооооооооооооо.........
Кто проживает на дне океана

Спанч Боб Square Pants!
Желтая губка, малыш без изъяна...
Спанч Боб Square Pants!
Кто побеждает всегда и везде
Спанч Боб Square Pants!
Кто также ловок как рыба в воде
Спанч Боб Square Pants!

Спанч Боб Square Pants!
Спанч Боб Square Pants!
Спанч Боб Square Pants!
Спанч Боб Square Pants!'''

print(gubka.count('Спанч Боб'))
valera = gubka.replace('Боб', 'Валера')
print(valera)

str = 'hello world worls'
arr = str.split()
print(arr)
arr2 = list(str)
print(arr2)

str = ' '.join(arr)
print(str)

newgubka = gubka.splitlines()
print(newgubka)
print('###\n'.join(newgubka))