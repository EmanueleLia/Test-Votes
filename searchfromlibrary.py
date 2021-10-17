import json
import time

print('Research a name from the Json course and receive the grade.\nWrite one of the following command:')
print('___________________________________________________________')
print('||   -r   || Research a name from the library            ||')
print('||   -n   || Show the Name List                          ||')
print('||   -g   || Show the Grade List                         ||')
print('||   -e   || Exit                                        ||')
print('\n')

while True:
    menuchoice = str(input('Enter one of the commands\n>> '))