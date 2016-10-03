#need to define how data is being taken in and defined as a variable for manipulation before presentation
#assuming services.py is our homemade parse tree
#general idea for data parsing below

import re
import os

#detect nmap scan; re.I is case independent regular expression for string 'nmap'
#this is pretty cool. https://txt2re.com/index-python.php3?s=DIRB&-1

#Need to sit down for a period of 4-5 hours and think very hard. I think I know how to do all of this somewhat """"easy"""""

re1,re.IGNORECASE|re.DOTALL
DIRBDir = z(#http+the whole string\n)
nmap = z(nmap)
nmapOpenPorts = z(#someport+Open)
CVE = z(#CVE+formatting)
Vulns = z(#Vulnerable this ones gonna be super hard)

def datatypeparser(#datacomingoutofsqldatabase???):
    
    