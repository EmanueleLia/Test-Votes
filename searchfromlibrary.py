import json
import time

print('Research a name from the Json course and receive the grade.\nSelect one of the following options:')

time.sleep(0.5)

print('___________________________________________________________')
print('||   1   ||  Research a name from the library            ||')
print('||   2   ||  Show the Name List                          ||')
print('||   3   ||  Show the Grade List                         ||')
print('||   4   ||  Exit                                        ||')
print('***********************************************************')
print('\n')

time.sleep(1)

while True:
    menuchoice = int(input('Enter one of the commands\n>> '))
    if menuchoice == 1:
        #save the Json file in input into the data string
        with open('namelist.json','r') as json_file:
            data = json.load(json_file)
        #request the name to be searched 
        namecapital = input('\nEnter the name you want to search:\n>> ').upper()
        #search namecapital in the json keys
        if namecapital in data:
            print(data[namecapital])
        else:
            print('Name not found')

        