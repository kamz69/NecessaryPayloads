# fait moi un script en python qui transforme un mail de la forme prénom.nom@nemera.net en : première lettre du prénom + nom
# Les mails se trouvent dans un fichier à parcourir


def transform_email(email):
    # Sépare le nom d'utilisateur et le domaine
    username, domain = email.split('@')
    compteur_points = 0

    #on compte les points
    for caractere in username:
        if caractere == '.':
            compteur_points += 1

    # Sépare le prénom et le nom
    if '.' in username:
        if compteur_points < 2:
            first_name, last_name = username.split('.')
            # Génère le nouvel email en utilisant la première lettre du prénom et le nom complet
            new_email = first_name[0] + last_name
        else:
             new_email='fake'
    
    else:
         new_email = username
         
    return new_email


# Nom du fichier contenant les adresses e-mail
filename = "emails.txt"

# Liste pour stocker les nouvelles adresses e-mail transformées
transformed_emails = []

# Ouvre le fichier en mode lecture
with open(filename, 'r') as file:
    # Parcours chaque ligne du fichier
    for line in file:
        # Supprime les espaces en début et fin de ligne
        line = line.strip()
        
        # Transforme l'adresse e-mail et l'ajoute à la liste
        new_email = transform_email(line)
        transformed_emails.append(new_email)

# Affiche les pseudo dans un fichier
nom_fichier = "pseudo.txt"
with open(nom_fichier, "a") as fichier:
        for pseudo in transformed_emails:
            fichier.write(str(pseudo) + "\n")
