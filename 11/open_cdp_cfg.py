from pprint import pprint
def open_file(filename):
    """ Фукнция открывает файл"""
    result = []
    with open(filename) as f:
        for line in f:
            result.append(line)
    return result
pprint(open_file('sw1_sh_cdp_neighbors.txt'))
    
