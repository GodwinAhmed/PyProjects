import random

print("Welcome to Password Generator\n ")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*,.'

number = input('Enter the number of passwords to generate: ')
number = int(number)

length = input('input the password length you reqire: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)