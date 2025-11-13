#!/bin/bash

################  MY NETWORK SCAN (MNC) ###################
#                   
# Network scan
# give scope txt in argument (cidr or ip)
# The script will generate :
#    File with up hosts
#    File with detailed scope
#    File with accessible web ports
#    File with accessible ports
#    File with accessible webservices
#    File with accessible web vulns
#    File with accessible infra vulns
#   
##########################################################

# Vérification des arguments
if [ $# -ne 1 ]; then
    echo "Usage: $0 <scope_file>"
    exit 1
fi

SCOPE_FILE=$1
OUTPUT_FILE="mnc_accessible_ports.txt"
TEMP_IPS="mnc_detailed_scope.txt"
UP_IPS="mnc_ips_up.txt"
WEB_OUTPUT_FILE="mnc_accessible_ports_web.txt"
WEBSERVERS="mnc_webservers.txt"
WEBVULNS="mnc_webVulns.txt"
INFRAVULNS="mnc_infraVulns.txt"

# Vérifier que le fichier existe
if [ ! -f "$SCOPE_FILE" ]; then
    echo "Fichier $SCOPE_FILE introuvable."
    exit 1
fi


# Vérifier si pv est installé
if ! command -v pv &> /dev/null; then
    echo "[!] L'outil 'pv' n'est pas installé. Il est nécessaire pour afficher la progression."
    sudo apt-get update && sudo apt-get install -y pv
fi


# Étape 1 : Expansion des CIDR en IPs
echo "[*] Expansion des CIDR..."
> $TEMP_IPS
while read line; do
    if [[ $line == *"/"* ]]; then
        prips $line >> $TEMP_IPS
    else
        echo $line >> $TEMP_IPS
    fi
done < $SCOPE_FILE

sort -u $TEMP_IPS -o $TEMP_IPS
TOTAL_IPS=$(wc -l < $TEMP_IPS)
echo "[*] Total IPs à scanner : $TOTAL_IPS"

# Étape 2 : Vérifier les IPs UP avec naabu (ping scan)
echo "[*] Vérification des IPs UP..."
cat $TEMP_IPS | pv -l -s $TOTAL_IPS | naabu -silent -sn -ping -rate 10000 -c 100 | sort -u > $UP_IPS
TOTAL_UP=$(wc -l < $UP_IPS)
echo "[*] IPs UP : $TOTAL_UP"

# Étape 3 : Scan des ports avec naabu
echo "[*] Scan des ports ..."
> $OUTPUT_FILE

#scan de port (au choix full ou top ports)
cat $UP_IPS | pv -l -s $TOTAL_UP | naabu -top-ports full -rate 20000 -c 100 -silent | sort -u > $OUTPUT_FILE
#cat $UP_IPS | pv -l -s $TOTAL_UP | naabu -top-ports 1000 -rate 20000 -c 100 -silent > $OUTPUT_FILE

echo "[*] Scan de port terminé. Résultats dans $OUTPUT_FILE"

#Etape 4 : Scan de vulnérabilités web avec nucléi
echo "[*] Scan de vulnérabilités web avec Nucléi..."

#scan all web ports
cat $UP_IPS | pv -l -s $TOTAL_UP | naabu -p 80,443,441,442,8000,8443,440,8008,8015,8083,8081,8080,8082,8181,8443,9080,9443,9990,65444,65443,1194,7001 -rate 20000 -c 100 -silent > $WEB_OUTPUT_FILE

# Filtrage des services web (nécéssaire pour nuclei)
httpx=/root/.asdf/installs/golang/1.22.2/packages/bin/httpx
cat $WEB_OUTPUT_FILE | pv -l -s $TOTAL_UP | $httpx -silent > $WEBSERVERS

#scan de vulns web
cat $WEBSERVERS | pv -l -s $TOTAL_IPS | nuclei -max-host-error 10 -as -rate-limit 40 -stats -silent -o $WEBVULNS

echo "[*] Scan de vulns web terminé. Résultats dans $WEBVULNS"

#Etape 5 : Scan de vulnérabilités Infra avec nucléi
echo "[*] Scan de vulnérabilités Infra avec Nucléi..."

#scan de vulns infra
cat $OUTPUT_FILE | pv -l -s $TOTAL_IPS | nuclei -max-host-error 10 -tags network -rate-limit 30 -stats -silent -o $INFRAVULNS

echo "[*] Scan de vulns infra terminé. Résultats dans $INFRAVULNS"
