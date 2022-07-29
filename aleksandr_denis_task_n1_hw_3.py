user_age = int(input('Fill up your age: '))
if user_age == 21: #Пробовал проверять тут возраст, состоит он из числа или из текста, с помощью type и .isdigit, но все равно почему-то не получилось
    print('You should visit Holland')
elif user_age > 21:
    print('You should visit Vietnam')
else:
    print('Travel everywhere')



