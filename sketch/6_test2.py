#!/usr/bin/env python3
user = {
    'kek':'12345678',
    'lol':'87654321'}

username = input('Enter an username:\n')
if not username in user:
    print('No such username\n')
else:
    password = input('Enter a password for username {}:\n'.format(username))
    while True:
        if password == user[username]:
            print('Acces is permitted.\n')
            break
        else:
            password = input('Wrong password. Please try again.\n')


