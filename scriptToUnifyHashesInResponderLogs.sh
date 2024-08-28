#!/bin/bash

# Créer un nouveau fichier "all_hashes.txt" s'il n'existe pas déjà
touch all_hashes.txt

# Parcourir tous les fichiers dans le répertoire courant dont le nom commence par "SMB-NTLMv2"
for file in SMB-NTLMv2*
do
    # Vérifier que le fichier est un fichier ordinaire (et non un répertoire)
    if [ -f "$file"  ]
    then
        # Ajouter le contenu du fichier à la fin de "all_hashes.txt"
        cat "$file" >> all_hashes.txt
    fi
done

