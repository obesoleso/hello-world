"""
il codice elimina la prima colonna di un file di una determinata estensione
e normalizza i valori dell'ultima colonna a 255 tra tutti i file cosi
che polyworks possa leggere l'intensita
"""

import glob # https://docs.python.org/2/library/glob.html
import time


# folder = "D:/Workspace_Files/user-data/test/"
folder = "D:/Workspace_Poly/user-data/Castelli_nuvole/" # path del file
ext = (".xyz") # estensione dei file
files_in_folder = glob.glob(folder + "*" + ext) # elenca tutti i file all'interno della cartella con quella determinata estensione
print files_in_folder # printa tutti i file riconosciuti

max_intensity = 0 # non toccare

# CODICE

start = time.clock()

# il codice prima individua il fattore di normalizzazione della intensita all'interno di un gruppo di file e poi
# lo applica a tutti quanti...
# individua pertanto l'intensita piu elevata all'interno del gruppo

print "checking the max intensity..."

for items in files_in_folder:
    f = open(items, "r") # apre il file da cui leggere
    # g = open(items[:-4] + "_norm.xyz", "w") # crea un nuovo file con il suffisso "_norm"
    for line in f: # per ciascuna linea del file
        # print "max intensity is " + str(max_intensity)  # printa la intensita massima
        parts = line.split() # splitta ciascuna riga del file in base agli spazi bianchi
        # print parts[-1] # printa l'ultima colonna
        if int(parts[-1]) > int(max_intensity): # if last column > max intensity
            max_intensity = parts[-1] # last column is the new max_intensity

print "max intensity is " + max_intensity # printa la intensita massima
fattore = 255 / float(max_intensity) # normalizza la max_intensity a 255 ... fattore e' float
print "intensity factor is " + str(fattore) # printa il fattore di normalizzazione

f.close() # chiude il file

print "now im creating the new files..."

for items in files_in_folder:
    f = open(items, "r") # apre il file da cui leggere
    g = open(items[:-4] + "_norm.xyz", "w") # crea un nuovo file con il suffisso "_norm"
    for line in f: # for each line in file_name
        splitted_line = line.split() # splitta la linea e la trasforma in una lista
        # print splitted_line[:-1] # stampa l'ultimo termine
        intensity_normed = (int(splitted_line[-1]) * fattore) # moltplica l'intensita per il fattore di normalizzazione
        g.write((" ".join(splitted_line[1:-1]) + " " + str(int(intensity_normed)) + "\n")) # converto prima in int e poi in str per fare l'arrotondamento
        # il \t e' cio' che viene inserito in mezzo ai singoli termini che erano una volta splittati ...  a questo si concatena la nuova intensita e poi si manda a capo con \n
    g.close() # chiude il file appena creato
    f.close() # chiude il file che e' stato letto

print str(time.clock() - start) + " seconds"