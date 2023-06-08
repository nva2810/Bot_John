def start(bot_name, birth_year, bot_version):
    print(f'''Hello, man! My name is {bot_name}.
I was created by NVA in {birth_year}.
My version is {bot_version} and will be updated.''')


def user_name():
    name = input('\nPlease enter your name: ')
    print(f'Nice to meet you, {name}!')


def choice():
    while True:
        print('''\nI can do a few things:
1. I can guess your date of birth!
2. I can guess your number!
3. I can output the Fibonacci numbers!
4. I can count to any number!
5. Nothing... (exit)''')
        user_choice = int(input('Enter the serial number, what should I do: '))
        while user_choice <= 0 or user_choice > 5:
            print('Incorrect data. Please try again!')
            user_choice = int(input('Enter the serial number, what should I do: '))
        if user_choice == 1:
            date_of_birth()
        elif user_choice == 2:
            user_number()
        elif user_choice == 3:
            fibonacci()
        elif user_choice == 4:
            user_count()
        elif user_choice == 5:
            print(f"\nThat's it all! My congratulations, have a nice day!")
            print(input('\nPress Enter to finish...'))
            break


def date_of_birth():
    print('\nDid you have a birthday this year?')
    birthday_this_year = input('Enter this here ("yes" or "no"): ')
    while birthday_this_year != 'yes' and birthday_this_year != 'no':
        print('Incorrect data. Please try again!')
        birthday_this_year = input('Enter this here ("yes" or "no"): ')
    print("""Okay. It's time to get a calculator!
\nMultiply your age by 2 (yourself).
Add 5 and multiply the result by 50.
Now you need to subtract 365.
\nHmm, too easily...
Pick any number up to 100 and add it to the result.""")
    age_and_number = int(input('Now enter what you received: ')) + 115
    print("""I'll remember it, don't you mind?
Go on!
\nNow multiply your birthday by 2 (yourself).
Add 5 and multiply the result by 50.
Add the number of the month in which you were born.
Example: October = 10""")
    day_and_month = int(input('Enter the result here: ')) - 250
    number = age_and_number % 100
    age = age_and_number // 100

    def user_day():
        day = day_and_month // 100
        if day == 1 or day == 21 or day == 31:
            day = str(day) + str('st')
        else:
            if day == 2 or day == 22:
                day = str(day) + str('nd')
            else:
                if day == 3:
                    day = str(day) + str('rd')
                else:
                    day = str(day) + str('th')
        return str(day)

    def year_of_birth():
        import datetime
        now = datetime.datetime.now()
        if birthday_this_year == 'no':
            year = now.year
            year -= age + 1
        else:
            year = now.year
            year -= age
        return year

    def months_of_year():
        month = day_and_month % 100
        months = ('', 'January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December')
        month = months[month]
        return month

    print(f'''\nWell, now I know more about you!
Your number is {number}!
You were born on {months_of_year()}, {user_day()}, {year_of_birth()}!
You are {age} years old!
Is that right? Excellent!''')


def user_number():
    print("""\nPlease pick a number from 1 to 60.
Are you ready?
Now look at these blocks.
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
\nWrite the numbers of the blocks together, where your number is located:
Example: 146 (if it's number 28)""")
    blocks = int(input('Enter here: '))

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
    print(f'Your number is {sum_blocks}, right?')


def fibonacci():
    n = int(input('\nEnter any number of the sequence element: '))
    x = []
    for n in range(n):
        if n <= 1:
            x.append(n)
            print(x[n])
        else:
            x.append(x[n-1] + x[n-2])
            print(x[n])


def user_count():
    num = int(input('Enter any number here: '))
    curr = 0
    while curr <= num:
        print(f'{curr}!')
        curr += 1


start('John', '2020', '2.1')
user_name()
choice()
