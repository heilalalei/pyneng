#!/usr/bin/env python3
#Task 12.3

from tabulate import tabulate
from answer_12_1 import check_ip_addresses

print(tabulate(check_ip_addresses(['8.8.8.8', '8.8.4.4','10.1.1.10']), headers = ['Reachable', 'Unreachable']))
