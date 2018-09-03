#!/usr/bin/env python3
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

num = input('Enter a number from num_list:\n')
print(len(num_list)-1-num_list[::-1].index(int(num)))
word = input('Enter a word from word_list:\n')
print(len(word_list)-1-word_list[::-1].index(word))



