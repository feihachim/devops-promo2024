#!/bin/bash

echo "Advance Disk Usage:"
echo "Ecrivez un répertoire à exclure"
read -r input
echo "Taille maximale des ficiers en octets"
read -r maxFileSize
argsList=""
for var in $input
do
 argsList+="$var|"
done
#echo "input vaut "
excludeList=${argsList:0:-1}
du -a /* 2>/dev/null | sort -nrk 1 |awk -v FILESIZE=$maxFileSize '$1<=FILESIZE {print $0}'| grep -Ev $excludeList 2>/dev/null | head -n 100 > report.txt
