#!/usr/bin/env python3
#Задание 9.4a
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
    ''' Функция обрабатывает конфигурационный файл
        config_dict - итоговый словарь    
        config_list - список команд второго уровня
        config_list2 - список для команд 3 уровня вложенности
        key - команда ПЕРВОГО уровня вложенности
    '''
    config_dict = {}
    config_list = []
    key = ''
    trigger = False
    with open(config) as f:
        for line in f:
            if line.startswith('\n'):
                continue
            if trigger == True:
                config_dict[key] = {}
                config_list2 = []    
            
            if ignore_command(line, ignore) == False and not line.startswith('!') and not line.startswith(' '):
                if key:
                    config_dict[key] = config_list
                key = line.rstrip()
                config_list = []                 
                config_dict2 = {}           
                continue
            elif ignore_command(line, ignore) == False and not line.startswith('!') and line.startswith(' ') and not line.startswith('  '):
                config_list.append(line.rstrip())
            elif ignore_command(line, ignore) == False and not line.startswith('!') and line.startswith('  '):
                trigger = True
                #config_dict[key][*config_list] = *config_list2
                config_dict[key].fromkeys(config_list,[])
                config_list2.append(line)
                               
    print(config_dict)

config_to_dict('config_r1.txt')


