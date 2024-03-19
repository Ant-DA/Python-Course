#Lettura file JSON

from json import load, dump
fin1 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/anonimizza_test1.json")
listalog1 = load(fin1)
fin1.close()
fin2 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/anonimizza_test2.json")
listalog2 = load(fin2)
fin2.close()

#Anonimizzazione nome utente

import Sottoprogrammi
d = {} #Dizionario che raccoglie nomi e identificativi
for log1 in listalog1:
    Sottoprogrammi.Anonimizza(log1[1], d, 5)
    log1[1] = d[log1[1]] #Cambio il nome utente con il numero
    log1.pop(2) #Elimino il campo "Utente coinvolto"
for log2 in listalog2:
    Sottoprogrammi.Anonimizza(log2[1], d, 5)
    log2[1] = d[log2[1]] #Cambio il nome utente con il numero
    log2.pop(2) #Elimino il campo "Utente coinvolto"
    
#Salvataggio in formato JSON

fout1 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/log_anonimizzati.json",'w')
dump(listalog1, fout1, indent=3)
fout1.close()

fout2 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/log_anonimizzati2.json",'w')
dump(listalog2, fout2, indent=3)
fout2.close()

fout3 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/codici_log.json",'w')
dump(d, fout3, indent=3)
fout3.close()


