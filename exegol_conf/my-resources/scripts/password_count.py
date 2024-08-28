#fais un script python qui donne le pourcentage d'utilisation d'un mot de passe

# Demander à l'utilisateur de fournir le chemin du fichier source
file_path = input("Veuillez entrer le chemin du fichier source : ")

# Demander à l'utilisateur de fournir le mot de passe à analyser
password = input("Veuillez entrer le mot de passe à analyser : ")

# Lire les mots de passe à partir du fichier source
with open(file_path, 'r') as file:
    passwords = file.read().splitlines()

# Compter le nombre total de mots de passe
total_passwords = len(passwords)

# Compter le nombre d'occurrences du mot de passe spécifié
password_count = passwords.count(password)

# Calculer le pourcentage d'utilisation du mot de passe
percentage = (password_count / total_passwords) * 100

# Afficher le résultat
print(f"Le mot de passe '{password}' a été utilisé {password_count} fois, ce qui représente {percentage:.2f}% de l'utilisation totale.")
