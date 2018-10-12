#!/usr/bin/env python3
#Задание 9.4
#Функция обрабатывает конфиг и возвращает словарь. 
#Все команды верхнего урованя - ключи, команды второго уровня - это значения у этого ключа (в видео списка)
ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def config_to_dict(config):
    ''' Функция открывает конфигурационный файл'''
    config_dict = {}
    config_list = []
    key = ''
    with open(config) as f:
        for line in f:
            if line.startswith('\n'):
                continue
            if ignore_command(line, ignore) == False and not line.startswith('!') and not line.startswith(' '):
                if key:
                    config_dict[key] = config_list
                key = line.rstrip()
                
                config_list = []                            
                continue
            elif ignore_command(line, ignore) == False and not line.startswith('!') and line.startswith(' '):
                config_list.append(line.rstrip())
    print(config_dict)

config_to_dict('config_sw1.txt')






 



