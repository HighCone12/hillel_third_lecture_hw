print('Hello dear user!')
user_name: str = input('Укажите ваше имя: ')
user_age: int = int(input('Укажите ваш возраст: '))
user_sex: str = input('Укажите ваш пол: ')
if user_name == 'admin':
    print('Привет, повелитель!')
if 10 < user_age < 14 and user_sex == 'М' or user_age > 30 and user_sex == 'М':
    print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'")
if 22 < user_age < 32 and user_sex == "Ж":
    print("Советую Вам посмотреть 'Трансформеры'")
if user_age < 16 and user_sex == 'Ж':
    print("Советую Вам посмотреть 'Инсургент'")
if user_name == 'Женя':
    print("Советую Вам посмотреть 'TMNT'")
if user_name == 'Guido':
    print("Советую Вам посмотреть 'TMNT', " 'Огромное спасибо!')