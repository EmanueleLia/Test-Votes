import json
import time
import os
import guiapp

print('*************************************************************************')
print('*******                      Test Vote Tool                       *******')
print('*************************************************************************\n\n')
print('This application allows you to manually enter the names of the students of the course in Mechanics applied to Machines and the corresponding grade of the course.')
print('At the end of the procedure the arithmetic average will be calculated and saved externally in the mediacorso.json file\n')
print('To be able to stop the input data, simply enter the word "quit" as the student name.\n')

n = 0
sommavoti = 0
nomevoto = []
arrayvoti = []
arraynomi = []
arraynomicapital = []
arraykeyvalue = []
jsonkeyvalue = str
nomecapital = str

print('Do you want to use the GUI version of this app? (y/n)')
guiChoice = input('>>> ')
if guiChoice == 'y':
    guiapp.showWindow()
    quit()
else:
    while True:
        nome = str(input('Enter student name (enter quit to stop)\n>>> '))
        nomecapital = nome.upper()
        arraykeyvalue.append(nomecapital)
        nomevoto.append(nome)
        arraynomi.append(nome)
        arraynomicapital.append(nomecapital)
        if nome == 'quit':
            nomevoto.remove('quit')
            arraynomi.remove('quit')
            arraykeyvalue.remove('QUIT')
            break
        else:
            voto = int(input('Enter the grade\n>>> '))
            while voto < 18 or voto >30:
                time.sleep(1)
                print('The grade entered must be between 18 and 30\n')
                time.sleep(1)
                voto = int(input('Please enter your grade again\n>>> '))
            else:
                nomevoto.append(voto)
                arrayvoti.append(voto)
                arraykeyvalue.append(voto)
                sommavoti = sommavoti + voto
                n = n + 1
                print('\n')

media = sommavoti/n

jsonoutput = {
    "coursename": "Mechanics applied to the machines",
    "average": media
}

#write the jsonoutput in the mediacorso.json file
with open('mediacorso.json','w') as json_file:
    json.dump(jsonoutput,json_file)

jsonkeyvalue = {arraykeyvalue[i]: arraykeyvalue[i + 1] for i in range(0, len(arraykeyvalue), 2)}

#write the jsonkeyvalue in the namelist.json file
with open('namelist.json','w') as json_file:
    json.dump(jsonkeyvalue,json_file)

time.sleep(2)
print('\n')
print('The arithmetic mean of the course is equal to ',media)
time.sleep(1)
print('The relative course and the average will be automatically saved in the mediacorso.json file.\n')

print('Choose one of the following commands to continue:')
print('1 - View the entered values;')
print('2 - Show entered names;')
scelta = int(input('3 - Exit.\n\n>>> '))

while True:
    if scelta == 1:
        print('\nHere are the values ​​entered:')
        print(nomevoto)
        time.sleep(1)
        print('\nChoose one of the following commands to continue:')
        print('1 - View the entered values;')
        print('2 - Show entered names;')
        scelta = int(input('3 - Exit.\n\n>>> '))
    elif scelta == 2:
        print('\nHere are the Names entered:')
        print(arraynomi)
        time.sleep(1)
        print('\nChoose one of the following commands to continue:')
        print('1 - View the entered values;')
        print('2 - Show entered names;')
        scelta = int(input('3 - Exit.\n\n>>> '))
    elif scelta == 3:
        time.sleep(0.5)
        print('\nYour satisfaction is our best reward!\n')
        time.sleep(2)
        quit()
    else:
        time.sleep(1)
        print('\nThe entered value is incorrect.\n')
        print('\nChoose one of the following commands to continue:')
        print('1 - View the entered values;')
        print('2 - Show entered names;')
        scelta = int(input('3 - Exit.\n\n>>> '))


