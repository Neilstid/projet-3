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
cLP = conn.cursor()
cSIRENE = conn.cursor()

for row_LP in cLP.execute('SELECT ville FROM LP'):
	distanceMinimum=1000
	for row_communes in cSIRENE.execute('SELECT ville FROM communes'):
		print(row_LP)
		print(row_communes)
		print(levenshtein("\""row_LP"\"","\""row_communes"\""))
		if levenshtein("\""row_LP"\"","\""row_communes"\"") < distanceMinimum:
			distanceMinimum = levenshtein("\""row_LP"\"","\""row_communes"\"")
			correspondance = row_communes
	liste.append(correspondance)
        
print(liste)

conn.commit()
conn.close()



