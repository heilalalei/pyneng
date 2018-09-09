#!/usr/bin/env python3
while True:
    a = input('Print a:\n')
    b = input('Print b:\n')
    try:
        result = int(a)/int(b)
    except ValueError:   
        print('Wrong type of variables')
    except ZeroDivisionError:
        print('Division by zero is prohibited')
    else:
        print(result)
        break
