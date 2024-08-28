#
# fais un script python qui va lire le contenu d'un fichier 
# Chaque ligne est de la forme :
# domain\user:id:lm:nt:::
# le script devra afficher tous paramètres nt identiques et donner le nombre de duplicatas.
# L'affichage se fera de plus grand nombre de duplicatas vers le plus petit (1 étant exclus)

from collections import Counter
import nturl2path


def lire_fichier(nom_fichier):
    nt_list = []  # Liste pour stocker les paramètres "nt"
    
    try:
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                ligne = ligne.strip()  # Supprime les espaces en début et fin de ligne
                if ligne:  # Vérifie si la ligne n'est pas vide
                    elements = ligne.split(':')
                    if len(elements) >= 4:
                        nt = elements[3]
                        user = elements[0]
                        nt_list.append(nt)
                       
                    else:
                        print("Format de ligne incorrect :", ligne)
    
    except FileNotFoundError:
        print("Fichier non trouvé :", nom_fichier)

    
    # Compte les duplicatas des paramètres "nt"
    duplicatas = Counter(nt_list)
    
    # Trie les duplicatas du plus grand nombre au plus petit (exclus 1)
    duplicatas_tries = sorted(duplicatas.items(), key=lambda x: x[1], reverse=True)
    duplicatas_tries = [(nt, count) for nt, count in duplicatas_tries if count > 1]
    
    # Affiche les paramètres "nt" identiques et le nombre de duplicatas
    if duplicatas_tries:
        print("Paramètres 'nt' identiques trouvés (du plus grand nombre au plus petit) :")
        for nt, count in duplicatas_tries:
            user_list = []  # Liste pour stocker les paramètres "user"
            with open(nom_fichier, 'r') as fichier:
                file = fichier.readlines()

                for ligne in file:
                    ligne = ligne.strip()  # Supprime les espaces en début et fin de ligne
                    if ligne:  # Vérifie si la ligne n'est pas vide
                        elements = ligne.split(':')
                        if len(elements) >= 4:
                            nt2 = elements[3]
                            if nt==nt2:
                                user = elements[0]
                                user_list.append(user)
                        else:
                            print("Format de ligne incorrect :", ligne)
            

            print("Paramètre 'nt' :", nt)
            print("Nombre de duplicatas :", count)
            print("comptes correspndants :")
            for user in user_list:
                print (user)
            print()
    else:
        print("Aucun paramètre 'nt' identique trouvé (avec un nombre de duplicatas supérieur à 1).")


nom_fichier = 'dcsync.txt'  # Remplacez par le chemin réel vers votre fichier
lire_fichier(nom_fichier)