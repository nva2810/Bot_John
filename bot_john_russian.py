def start(bot_name, birth_year, bot_version):
    print(f'''Привет, чувак! Меня зовут {bot_name}.
Я был создан NVA в {birth_year} году.
Моя версия {bot_version} и будет обновляться.''')


def user_name():
    name = input('\nПожалуйста, введи свое имя: ')
    print(f'Приятно познакомиться, {name}!')


def choice():
    while True:
        print('''\nЯ могу сделать несколько вещей:
1. Угадать дату рождения!
2. Угадать ваш номер!
3. Вывести числа Фибоначчи!
4. Посчитать до любого числа!
5. Ничего... (выход)''')
        user_choice = int(input('Введите порядковый номер, что мне сделать: '))
        while user_choice <= 0 or user_choice > 5:
            print('Неверные данные. Пожалуйста, попробуйте еще раз!')
            user_choice = int(input('Введите порядковый номер, что мне сделать: '))
        if user_choice == 1:
            date_of_birth()
        elif user_choice == 2:
            user_number()
        elif user_choice == 3:
            fibonacci()
        elif user_choice == 4:
            user_count()
        elif user_choice == 5:
            print(f'\nВот и все! Мои поздравления, хорошего Вам дня!')
            print(input('\nНажмите Enter, чтобы закончить...'))
            break


def date_of_birth():
    print('\nУ тебя был день рождения в этом году?')
    birthday_this_year = input('Напиши здесь ("да" или "нет"): ')
    while birthday_this_year != 'да' and birthday_this_year != 'нет':
        print('Неверные данные. Пожалуйста, попробуйте еще раз!')
        birthday_this_year = input('Напиши здесь ("да" или "нет"): ')
    print('''Окей, бро. Пришло время воспользоваться калькулятором!
\nУмножь свой возраст на 2 (самостоятельно).
Плюсуй 5 и умножай полученный результат на 50.
Теперь тебе нужно вычесть 365.
\nХм, слишком легко...
Загадай любое число до 100 и добавь его к результату.''')
    age_and_number = int(input('Теперь введи то, что ты получил: ')) + 115
    print('''Я запомню это, не возражаешь?
Двигаемся дальше!
\nТеперь умножь свой день рождения на 2 (самостоятельно).
Прибавь 5 и умножь результат на 50.
Добавь число месяца, в котором ты родился.
Например: Октябрь = 10''')
    day_and_month = int(input('Введи полученный результат сюда: ')) - 250
    number = age_and_number % 100
    age = age_and_number // 100
    day = day_and_month // 100

    # def user_day() не нужна для русского языка

    def year_of_birth():
        import datetime
        now = datetime.datetime.now()
        if birthday_this_year == 'нет':
            year = now.year
            year -= age + 1
        else:
            year = now.year
            year -= age
        return year

    def months_of_year():
        month = day_and_month % 100
        months = ('', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')
        month = months[month]
        return month

    # немного изменен ответ, из-за другой орфографии на русском
    print(f'''\nНу вот, теперь я знаю о тебе больше!
Ты загадал число {number}!
Ты родился {day} {months_of_year()} {year_of_birth()} года!
Сейчас тебе {age} лет!
Всё верно? Превосходно!''')


def user_number():
    print('''\nПожалуйста, загадай любое число от 1 до 60.
Ты готов?
А теперь взгляни на эти блоки.
\n1.  4 13 22 31 44 53  2.  2 11 22 31 42 51
    5 14 23 36 45 54      3 14 23 34 43 54
    6 15 28 37 46 55      6 15 26 35 46 55
    7 20 29 38 47 60      7 18 27 38 47 58
   12 21 30 39 52        10 19 30 39 50 59
\n3.  1 11 21 31 41 51  4.  8 13 26 31 44 57
    3 13 23 33 43 53      9 14 27 40 45 58
    5 15 25 35 45 55     10 15 28 41 46 59
    7 17 27 37 47 57     11 24 29 42 47 60
    9 19 29 39 49 59     12 25 30 43 56
\n5. 32 37 42 47 52 57  6. 16 21 26 31 52 57
   33 38 43 48 53 58     17 22 27 48 53 58
   34 39 44 49 54 59     18 23 28 49 54 59
   35 40 45 50 55 60     19 24 29 50 55 60
   36 41 46 51 56        20 25 30 51 56
\nЗапиши ниже номера блоков слитно, где есть твое загаданное число:
Например: 146 (если это число 28)''')
    blocks = int(input('Ввести здесь: '))

    def first_block():
        block_1 = blocks % 100000 // 10000
        if block_1 == 2:
            block_1 = 2
        elif block_1 == 4:
            block_1 = 8
        elif block_1 == 5:
            block_1 = 32
        elif block_1 == 6:
            block_1 = 16
        elif block_1 == 1:
            block_1 = 4
        elif block_1 == 3:
            block_1 = 1
        return block_1

    def second_block():
        block_2 = blocks % 10000 // 1000
        if block_2 == 2:
            block_2 = 2
        elif block_2 == 4:
            block_2 = 8
        elif block_2 == 5:
            block_2 = 32
        elif block_2 == 6:
            block_2 = 16
        elif block_2 == 1:
            block_2 = 4
        elif block_2 == 3:
            block_2 = 1
        return block_2

    def third_block():
        block_3 = blocks % 1000 // 100
        if block_3 == 2:
            block_3 = 2
        elif block_3 == 4:
            block_3 = 8
        elif block_3 == 5:
            block_3 = 32
        elif block_3 == 6:
            block_3 = 16
        elif block_3 == 1:
            block_3 = 4
        elif block_3 == 3:
            block_3 = 1
        return block_3

    def fourth_block():
        block_4 = blocks % 100 // 10
        if block_4 == 2:
            block_4 = 2
        elif block_4 == 4:
            block_4 = 8
        elif block_4 == 5:
            block_4 = 32
        elif block_4 == 6:
            block_4 = 16
        elif block_4 == 1:
            block_4 = 4
        elif block_4 == 3:
            block_4 = 1
        return block_4

    def fifth_block():
        block_5 = blocks % 10
        if block_5 == 2:
            block_5 = 2
        elif block_5 == 4:
            block_5 = 8
        elif block_5 == 5:
            block_5 = 32
        elif block_5 == 6:
            block_5 = 16
        elif block_5 == 1:
            block_5 = 4
        elif block_5 == 3:
            block_5 = 1
        return block_5

    sum_blocks = int(first_block()) + int(second_block()) \
        + int(third_block()) + int(fourth_block()) \
        + int(fifth_block())
    print(f'Ты загадал число {sum_blocks}, верно?')


def fibonacci():
    n = int(input('\nВведите любое число элемента последовательности: '))
    x = []
    for n in range(n):
        if n <= 1:
            x.append(n)
            print(x[n])
        else:
            x.append(x[n-1] + x[n-2])
            print(x[n])


def user_count():
    num = int(input('Введи здесь любое число: '))
    curr = 0
    while curr <= num:
        print(f'{curr}!')
        curr += 1


start('Джон', '2020', '2.1')
user_name()
choice()
