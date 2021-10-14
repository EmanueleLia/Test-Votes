import json
import time
import os

#Inizializziamo l'applicazione

print('*************************************************************************')
print('*******                      Test Vote Tool                       *******')
print('*************************************************************************\n\n')
print('This applicazione permette di inserire manualmente i nomi degli studenti del corso di Meccanica applicata alle Macchine ed il corrispettivo voto del corso.')
print('Al termine della procedura verrà calcolata la media aritmetica e salvata esternamente in file mediacorso.json\n')
print('Per poter stoppare i dati in input basterà inserire la parola "quit" come nome dello studente.\n')

nomevoto = []
n = 0
sommavoti = 0
arraynomi = []
nomecapital = str
arraynomicapital = []
arrayvoti = []
nomeindex = int

while True:
    nome = str(input('Inserisci il nome dello studente (inserisci quit per stoppare)\n>>> '))
    nomecapital = nome.upper()
    nomevoto.append(nome)
    arraynomi.append(nome)
    arraynomicapital.append(nomecapital)
    if nome == 'quit':
        nomevoto.remove('quit')
        arraynomi.remove('quit')
        break
    else:
        voto = int(input('Inserisci il voto\n>>> '))
        while voto < 18 or voto >30:
            time.sleep(1)
            print('Il voto inserito deve essere compreso tra 18 e 30\n')
            time.sleep(1)
            voto = int(input('Inserisci nuovamente il voto\n>>> '))
        else:
            nomevoto.append(voto)
            arrayvoti.append(voto)
            sommavoti = sommavoti + voto
            n = n + 1
            print('\n')

media = sommavoti/n

time.sleep(2)
print('\n')
print('La media aritmetica del corso ottenuta è pari a ',media)
time.sleep(1)
print('Il relativo corso e la media saranno salvati in automatico nel file mediacorso.json.\n')

print('Scegli uno dei seguenti comandi per continuare:')
print('1 - Visualizza i valori inseriti;')
print('2 - Mostra i nomi inseriti;')
print('3 - Visualizza il voto per ricerca nome;')
scelta = int(input('4 - Esci.\n\n>>> '))

while True:
    if scelta == 1:
        print('\nEcco di seguito i valori inseriti:')
        print(nomevoto)
        time.sleep(1)
        print('\nScegli uno dei seguenti comandi per continuare:')
        print('1 - Visualizza i valori inseriti;')
        print('2 - Mostra i nomi inseriti;')
        scelta = int(input('3 - Esci.\n\n>>> '))
    elif scelta == 2:
        print('\nEcco di seguito i Nomi inseriti:')
        print(arraynomi)
        time.sleep(1)
        print('\nScegli uno dei seguenti comandi per continuare:')
        print('1 - Visualizza i valori inseriti;')
        print('2 - Mostra i nomi inseriti;')
        scelta = int(input('3 - Esci.\n\n>>> '))
    elif scelta == 3:
        time.sleep(0.5)
        print('\nLa sua soddisfazione è il nostro miglior premio!\n')
        time.sleep(2)
        quit()
    else:
        time.sleep(1)
        print('\nIl valore inserito non è corretto.\n')
        print('Scegli uno dei seguenti comandi per continuare:')
        print('1 - Visualizza i valori inseriti;')
        print('2 - Mostra i nomi inseriti;')
        scelta = int(input('3 - Esci.\n\n>>> '))

jsonoutput = {
    'nomecorso': 'Meccanica applicata alle macchine',
    'media': media
}

with open('mediacorso.json','w') as json_file:
    json.dump(jsonoutput,json_file)
