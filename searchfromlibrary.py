import json
import time

#save the Json file in input into the data string
with open('namelist.json','r') as json_file:
    data = json.load(json_file)

#initiate the Command Line
print('Research a name from the Json course and receive the grade.\nSelect one of the following options:')
time.sleep(0.5)
print('___________________________________________________________')
print('||   1   ||  Research a name from the library            ||')
print('||   2   ||  Show the Name List                          ||')
print('||   3   ||  Show the Grade List                         ||')
print('||   4   ||  Exit                                        ||')
print('***********************************************************')
time.sleep(1)

while True:
    menuchoice = int(input('Enter one of the commands\n>> '))
    if menuchoice == 1:
        #request the name to be searched 
        namecapital = input('Enter the name you want to search:\n>> ').upper()
        #search namecapital in the json keys
        if namecapital in data:
            print('\nGrade: '+str(data[namecapital]))
        else:
            print('Name not found')
        #return to the main menu
        time.sleep(1.5)
        print('\nDo you want to continue?\nSelect one of the following options:')
        print('___________________________________________________________')
        print('||   1   ||  Research a name from the library            ||')
        print('||   2   ||  Show the Name List                          ||')
        print('||   3   ||  Show the Grade List                         ||')
        print('||   4   ||  Exit                                        ||')
        print('***********************************************************')
    if menuchoice == 2:
        print(str(data.keys())+'\n')
        time.sleep(1.5)
        print('\nDo you want to continue?\nSelect one of the following options:')
        print('___________________________________________________________')
        print('||   1   ||  Research a name from the library            ||')
        print('||   2   ||  Show the Name List                          ||')
        print('||   3   ||  Show the Grade List                         ||')
        print('||   4   ||  Exit                                        ||')
        print('***********************************************************')
    if menuchoice == 3:
        print(str(data.values())+'\n')
        time.sleep(1.5)
        print('\nDo you want to continue?\nSelect one of the following options:')
        print('___________________________________________________________')
        print('||   1   ||  Research a name from the library            ||')
        print('||   2   ||  Show the Name List                          ||')
        print('||   3   ||  Show the Grade List                         ||')
        print('||   4   ||  Exit                                        ||')
        print('***********************************************************')
    if menuchoice == 4:
        break
    if menuchoice < 1 or menuchoice > 4:
        time.sleep(1.5)
        print('\nWrong selection!\nSelect one of the following options:')
        print('___________________________________________________________')
        print('||   1   ||  Research a name from the library            ||')
        print('||   2   ||  Show the Name List                          ||')
        print('||   3   ||  Show the Grade List                         ||')
        print('||   4   ||  Exit                                        ||')
        print('***********************************************************')

print('\nHave a good day sir.\n')

        