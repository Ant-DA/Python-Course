#Lettura file JSON

from json import load, dump
fin1 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/log_anonimizzati.json")
listalog = load(fin1)
fin1.close()
fin2 = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/codici_log.json")
d = load(fin2)
fin2.close()

#Deanonimizzazione
import Sottoprogrammi
for log in listalog:
    log[1] = Sottoprogrammi.Deanonimizza(log[1], d)

#Salvataggio in formato JSON

fout = open("D:/Dottorato/Corsi di Dottorato/Introduzione a Python/anonimizza_log_init/test_data/log_deanonimizzati.json", 'w')
dump(listalog, fout, indent=3)
fout.close()