#!/bin/bash

echo "Work in Progress"
touch report.txt

system_security_check()
{
  echo "================= System Security Check =====================" > report.txt
  echo " " >> report.txt
  echo "****** Liste des fichiers world writable ******" >> report.txt
  sudo find / -perm -o+w | head -n 40 >> report.txt
  echo " " >> report.txt
  echo "****** Liste des utilisateurs ******" >> report.txt
  cat /etc/passwd | awk -F":" '$3>=1000 {print $1}' >> report.txt
  echo " " >> report.txt
  echo "=============================================================" >> report.txt
}

audit_disk_usage()
{
  echo "==================== Audit Disk Usage =======================" >> report.txt
  echo " " >> report.txt
  cat /etc/passwd | awk -F":" '$3>=1000 {
    system(" echo \" *** Les plus gros fichiers de " $1 " *** \" >> report.txt")
    system("du -a " $6 " 2>/dev/null | sort -nrk 1 | head -n 10 >> report.txt")

}' 
  
  echo "****** Disk Usage du répertoire /home  ******" >> report.txt
  du -a /home/* 2>/dev/null | sort -nrk 1  | head -n 10 >> report.txt
  echo "****** Disk usage du répertoire /tmp ******" >> report.txt
  du -a /tmp/* 2>/dev/null | sort -nrk 1 | head -n 10 >> report.txt
  echo "****** Disk usage du répertoire /var ******" >> report.txt
  du -a /var/* 2>/dev/null | sort -nrk 1 | head -n 10 >> report.txt
  echo " " >> report.txt
  echo "=============================================================" >> report.txt
}

unused_package_cleaner()
{
  echo "Unused Package Cleaner"
}

system_security_check
audit_disk_usage
unused_package_cleaner
