import argparse
from collections import Counter
import nturl2path

nt_list = []  # Liste pour stocker les paramètres "nt"

# Créez un objet ArgumentParser
parser = argparse.ArgumentParser(description="Script qui fait la corélation entre le outputfile hashcat et le outputfile dcsync pour retrouver le mot de passe de chaque compte")

# arguments
parser.add_argument('--input-hashcat', required=True, help="dump hashcat")
parser.add_argument('--input-ntds', required=True, help="dump NTDS.DIT")
parser.add_argument('-s', '--statistics', action='store_true', help="Afficher le pourcentage et le nombre de comptes crackés")


# Analysez les arguments
args = parser.parse_args()



# Code
#correspondance entre le hash et le mdp en clair
fichier_hashcat= args.input_hashcat


#correspondance entre le compte et le hash
    # Chaque ligne est de la forme domain\user:id:lm:nt:::
fichier_ntds = args.input_ntds


with open(fichier_hashcat, 'r') as f_recherche:
        hashcat = f_recherche.read().strip().split('\n')

with open(fichier_ntds, 'r') as f_valeurs:
        ntds = f_valeurs.read().strip().split('\n')
        



#count cracked passwords
total_cracked_passwords = len(hashcat)
#count all passwords ntds
total_passwords = len(ntds)

####################### statistics #######################
def show_statistics():
      # Calculer le pourcentage d'utilisation du mot de passe
    percentage = (total_cracked_passwords / total_passwords) * 100
    #print(f"Le mot de passe '{password}' a été utilisé {total_cracked_passwords} fois, ce qui représente {percentage:.2f}% de l'utilisation totale.")
    print(f"[+] '{total_cracked_passwords}' password ont été crackés sur un total de '{total_passwords}' soit '{percentage:.2f}'% ")
    
if (args.statistics):
      show_statistics()

#correspondance compte/mot de passe
print("[+] corélation compte:password")

for ligne in hashcat:
    hash = ligne.split(':')[0].strip()
    password = ligne.split(':')[1].strip()

    
    for ligne2 in ntds:
        elements = ligne2.split(':')
        if len(elements) >= 4:
                        nt = elements[3]
                        user = elements[0]
                        nt_list.append(nt)
                       

        if hash in ligne2 :
             username = ligne2
             print('    '+username+':'+password)



