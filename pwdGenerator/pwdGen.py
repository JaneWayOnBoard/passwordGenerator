#!/bin/pyhton3
import random

print('''
Password Generator
==================
''')

"""create a string of chars"""
chars = 'abcdefghijklmnopqrstuvwxyz!@£$%^&*().,?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@£$%^&*().,?'

"""ask user the number of passwords he wants"""
number = input('number of passwords ? : ')
number = int(number)

"""ask the user for the pwds lenght"""
length = input('password length ? : ')
length = int(length)

"""print the required pwds"""
print('\nhere are your passwords:')


"""create a loop to generate a random password"""
for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
