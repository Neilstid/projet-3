'''pour chaque ligne du fichier LP faire
    chercher la (ou les) communes dont le nom est le plus proche
    pour chacunes de ces communes faire
        chercher dans communes l'établissement de cette commune dont le nom est le plus proche
fin pour
fin pour'''

##################################################################

### Fonction Levenshtein ###
def levenshtein(mot1,mot2):
	ligne_i = [ k for k in range(len(mot1)+1)]
	for i in range(1, len(mot2) + 1):
		ligne_prec = ligne_i
		ligne_i = [i]*(len(mot1)+1)
		for k in range(1,len(ligne_i)):
			cout = int(mot1[k-1] != mot2[i-1])
			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
	return ligne_i[len(mot1)]

### Code python ###

import sqlite3

liste = []

conn = sqlite3.connect('data.db')
c_LP = conn.cursor()
c_communes = conn.cursor()

for row_LP in c_LP.execute('SELECT ville FROM LP'):
	distanceMinimum=1000
	for row_communes in c_communes.execute('SELECT communes.ville FROM communes, LP where communes.departement = LP.departement'):
		if levenshtein(row_LP[0],row_communes[0]) < distanceMinimum:
			print(levenshtein("\"" + row_LP[0].lower() + "\"", "\"" + row_communes[0].lower() + "\""))
			print(row_LP[0].lower())
			print(row_communes[0].lower())
			distanceMinimum = levenshtein(row_LP[0],row_communes[0])
			correspondance = row_communes[0]
	liste.append(correspondance)
        
print(liste)

conn.commit()
conn.close()
