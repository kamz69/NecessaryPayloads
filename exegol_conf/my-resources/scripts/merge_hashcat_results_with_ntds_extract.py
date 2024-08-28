# Exemple d'utilisation
fichier_recherche = 'hash_cracked_uniq.txt'
fichier_valeurs = 'dcsync.txt'


with open(fichier_recherche, 'r') as f_recherche:
        recherche = f_recherche.read().strip().split('\n')

with open(fichier_valeurs, 'r') as f_valeurs:
        valeurs = f_valeurs.read().strip().split('\n')
        
for ligne in recherche:
    hash = ligne.split(':')[0].strip()
    password = ligne.split(':')[1].strip()
    #print(hash)
    #print(password)
    
    for ligne2 in valeurs:
        if hash in ligne2 :
             username = ligne2
             print(username+':'+password)
             #with open("hash_cracked_users.txt", "w") as fichier:
                # Écriture de la variable dans le fichier
                #fichier.write(username+':'+password)