import random

digits = '0123456789'
lowercase_letters = "abcdefghijklmnopqrstuvwxyz;"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ;"
punctuation = "!#$%&*+-=?@^_."

pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')
chars = ''

if pwd_digits.lower() == 'да':
    chars += digits
if pwd_uppercase.lower() == 'да':
    chars += uppercase_letters
if pwd_lowercase.lower() == 'да':
    chars += lowercase_letters
if pwd_punctuation.lower() == 'да':
    chars += punctuation
if pwd_exceptions.lower() == 'да':
    chars += pwd_exceptions


def generate_password(pwd_len, chars):
    password = ''
    for j in range(pwd_len):
        password += random.choice(chars)
    return password


for i in range(pwd_quantity):
    print(generate_password(pwd_len, chars))



