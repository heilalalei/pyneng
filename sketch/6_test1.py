#!/usr/bin/env python3
username = input('Enter an username:\n')
password = input('Enter a password for username {}:\n'.format(username))
while True:
    if len(password) < 8:
        print('Too short password.')
    elif username in password:
        print('Password contains an username.')
    else:
        print('Password for {} has been installed.'.format(username))
        break
    password = input('\nRe-enter a password: ')


