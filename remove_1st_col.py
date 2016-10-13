"""
Questo codice serve per eliminare la prima colonna di un file
E' da utilizzare perche' alcuni file xyz che esportiamo hanno l'indice come prima colonna
"""

import glob
folder = "D:/Workspace_Poly/user-data/Castelli_nuvole/"
ext = ".xyz"
files_in_folder =  glob.glob(folder + "*" + ext)
print files_in_folder

for items in files_in_folder:
	f = open(items, "r")
	g = open(items[:-4] + "_fixed" + ext, "w")
	for line in f:
		if line.strip(): # https://www.tutorialspoint.com/python/string_strip.htm
			g.write(" ".join(line.split()[1:]) + "\n") # https://www.tutorialspoint.com/python/string_split.htm
	f.close()
	g.close()