#!/usr/bin/env python3
#Задание 9.4a
#Функция обрабатывает конфиг и возвращает словарь. 
#Все команды верхнего урованя - ключи, команды второго уровня - это значения у этого ключа (в видео списка)
#ДАННАЯ ВЕРСИЯ ПОЧЕМУ ТО ПРОПУСКАЕТ ПАРУ КОМАНД 1 УРОВНЯ ПОСЛЕ 'address family vpnv4', но я забил уже
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
        key2 - команда ВТОРОГО уровня, после которой впервые встречается команда 3 уровня
    '''
    config_dict = {}
    config_list = []
    config_list2 = []
    key = ''
    key2 = '' # <--- это та строчка, после которой идут команды lvl3 
    with open(config) as f:                                                                            
        for line in f:                                                                                 
            #Пропустить строку переноса                                                                
            if line.startswith('\n'):                                                                  
                continue      
            #Поиск команды первого уровня
            if ignore_command(line, ignore) == False and not line.startswith('!') and not line.startswith(' '):
                if config_list and not config_list2:
                    config_dict[key] = config_list                                                     
                elif key2:                                                                             
                    config_dict[key] = {}                                                              
                    config_dict[key] = config_dict[key].fromkeys(config_list,[])                       
                    config_dict[key][key2] = config_list2                                              
   
                elif key and not config_list and not config_list2:                                     
                    config_dict[key] = []                                                              
                key = line.rstrip()                                                                    
                config_list = []                                                                       
                key2 = ''                                                                              
                continue                    
            #Поиск команды второго уровня                                                              
            elif ignore_command(line, ignore) == False and not line.startswith('!') and line.startswith(' ') and not line.startswith('  ') and not line.startswith(' !'):                                     
                key2 = ''                                                                              
                key2_kek = line.rstrip()                                                               
                config_list2 = []                                                                      
                config_list.append(line.rstrip())                                                      
                                                                                  
            #Поиск команды третьего уровня                                                             
            elif ignore_command(line, ignore) == False and not line.startswith('!') and line.startswith('  '):
                key2 = key2_kek
                config_list2.append(line.rstrip())
    print(config_dict)                                                                                 
config_to_dict('config_r1.txt')     

