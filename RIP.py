# ====== CREATE BY MIRZUHAIBCODINGS ======
# ====== FOUNDER OF ANONMOUS KASHMIR ======
# ====== TOOL NAME : YAHEOL ======

import socket
import os
import time
import whois

# Clear screen
os.system('clear')

# Banner
print("\033[1;32m")
print("██╗░░██╗░█████╗░██╗░░██╗███████╗░█████╗░██╗░░░░░")
print("██║░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗██║░░░░░")
print("█████═╝░███████║███████║█████╗░░██║░░██║██║░░░░░")
print("██╔═██╗░██╔══██║██╔══██║██╔══╝░░██║░░██║██║░░░░░")
print("██║░╚██╗██║░░██║██║░░██║███████╗╚█████╔╝███████╗")
print("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝")
print("\033[0m")

print("\033[1;36m               TOOL NAME : YAHEOL\033[0m")
print("\033[1;35m         CREATED BY : MIRZUHAIBCODINGS\033[0m")
print("\033[1;31m        FOUNDER OF : ANONMOUS KASHMIR -71\033[0m")
print("\033[1;34m")
print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" TELEGRAM   : https://t.me/ANONMOUS_KASHMIR")
print(" INSTAGRAM  : _bughunter_x_")
print(" WEBSITE    : https://mirzuhaibcodings.blogsport.com")
print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("\033[0m")

# Input
url = input("\033[1;33m[+] Enter Website URL (without https://): \033[0m")

# Resolve IP
try:
    print("\n\033[1;34m[~] Resolving IP...\033[0m")
    time.sleep(1)
    ip = socket.gethostbyname(url)
    print(f"\n\033[1;32m[✔] IP Address: {ip}\033[0m\n")
except socket.gaierror:
    print(f"\n\033[1;31m[✘] Unable to resolve IP for {url}\033[0m\n")
    exit()

# WHOIS info
print("\033[1;34m[~] Fetching WHOIS Information...\033[0m")
try:
    domain_info = whois.whois(url)
    time.sleep(1)
    print("\033[1;32m[✔] WHOIS Information:\033[0m\n")
    print(domain_info)
except Exception as e:
    print(f"\033[1;31m[✘] WHOIS info not found: {e}\033[0m")
