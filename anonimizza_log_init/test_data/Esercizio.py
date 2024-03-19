#Lettura file JSON

from json import load, dump
fin = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/anonimizza_test1.json")
listalog = load(fin)
fin.close()

#Anonimizzazione nome utente

d = {} #Dizionario che raccoglie nomi e identificativi
s = 1 #Contatore
for log in listalog:
    if log[1] not in d.keys():
        #Se il nome non è nel dizionario, gli associo un numero
        d[log[1]] = s 
        s = s+1
    log[1] = d[log[1]] #Cambio il nome utente con il numero
    log.pop(2) #Elimino il campo "Utente coinvolto"
    
#Salvataggio in formato JSON

fout1 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/log_anonimizzati.json",'w')
dump(listalog, fout1, indent=3)
fout1.close()

fout2 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/codici_log.json",'w')
dump(d, fout2, indent=3)
fout2.close()