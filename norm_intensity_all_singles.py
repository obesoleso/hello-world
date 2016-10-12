"""
il codice elimina la prima colonna di un file di una determinata estensione
e normalizza i valori dell'ultima colonna a 255 per ciascun file cosi
che polyworks possa leggere l'intensita
"""

import glob
folder = ("D:/Workspace_Files/user-data/bbb/")
ext = (".xyz")
files_in_folder =  glob.glob(folder + "*" + ext)
print files_in_folder

# CODICE


for items in files_in_folder:
    max_intensity = 0 # cosi' individua per ogni file l'intensita massima
    f = open(items, "r") # apre il file da cui leggere
    g = open(items[:-4] + "_norm.xyz", "w") # crea un nuovo file con il suffisso "_norm"
    for line in f: # per ciascuna linea del file
        print "max intensity is " + str(max_intensity)  # printa la intensita massima
        parts = line.split() # splitta ciascuna riga del file in base agli spazi bianchi
        print parts[-1]
        if int(parts[-1]) > int(max_intensity): # coulmn 5 > max intensity
            max_intensity = parts[-1] # column 5 is the new max_intensity

    print "max intensity is " + max_intensity # printa la intensita massima

    fattore = 255 / float(max_intensity) # normalizza la max_intensity a 255 ... fattore e' float

    print "intensity factor is " + str(fattore) # prina il fattore di normalizzazione

    f.seek(0) # riporta il cursore in cima al file

    for line in f: # for each line in file_name
        splitted_line = line.split() # splitta la linea e la trasforma in una lista
        print splitted_line[:-1]
        intensity_normed = (int(splitted_line[-1]) * fattore)
        g.write(("\t".join(splitted_line[1:-1]) + "\t" + str(int(intensity_normed)) + "\n")) # converto prima in int e poi in str per fare l'arrotondamento

    g.close() # chiude il file g
    f.close() # chiude il file f