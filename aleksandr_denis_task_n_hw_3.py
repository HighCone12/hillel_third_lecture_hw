1.
S1 = 'spam'
S2 = 'eggs'
print(S1 + S2)
'spameggs' #Сложение

print('spam' * 3)
spamspamspam # Дублирование строки

len('spam')
4 #Длинна строки

S = 'spam'
S[0]
's'
S[2]
'a'
S[-2]
'a' #Доступ по индексу

s = 'spameggs'
s[3:5]
'me'
s[2:-2]
'ameg'
s[:6]
'spameg'
s[1:]
'pameggs'
s[:]
'spameggs'  #Извлечения среза

s[::-1]
'sggemaps'
s[3:5:-1]
''
s[2::2]
'aeg'  #Извлечение среза с указанием шага

2.
a)  x = 'apple'
    y = "juice"
    z = 'turtle'
b)  x = 123
    y = 12.3
    z = 00.1
с)  grocery = ['sausage', 'bread', 'cucumbers']
    to_do_list = ['clean the room', 'do the dishes', 'watch a movie']
    dates = ['12.07', '28.12', '01.02']
d)  dict_letters = {'a', 'b', 'c'}
    dict_words = {'lettuce', 'corn', 'pumpkin'}
    dict_numbers = {'12','13','14'}
e)  my_tuple = (book, paper, pen)
    your_tuple = (pencil, eraser, copybook)
    our_tuple = (book, paper, pen, pencil, eraser, copybook)

3.  x = ['4', '11', '6', '31']
# функция `max` сравнивает
# числа как строки
max(x)
'6'
x = list('abcdifgh')
max(x)
'i'
max([1.2, 1.3, 1.5, 2, 5.52])
'5.52'

x = ['4', '11', '6', '31']
# функция `min` сравнивает
# числа как строки
min(x)
'11'
x = list('abcdifgh')
min(x)
'a'
min([1.2, 1.3, 1.5, 2, 5.52])
'1.2'

5. "cad" in "cadillac" вернет #True.
1 in [2,3,1,6] вернет #True.
"hi" in {"hi":2,"bye":1} вернет #True.

6. if test1:
    state1
elif test2:
    state2
else:
    state3

if 1:
    print('true')
else:
    print('false')
#True

a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')