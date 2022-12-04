# !/usr/bin/env python
# -*- coding: utf-8 -*-
#   Coded By wolkan

import argparse
from ast import arg
import requests 
import sys
import os
import socket
from datetime import datetime
import whois

# Renkler
reset = "\033[0m"
kirmizi = "\033[1;31m"
yesil = "\033[1;32m"
cyan = "\033[1;36m"

# Semboller ([+],[-],[*],[!],[?])
plus = yesil + "[" + kirmizi + "+" + yesil + "]"
sour = kirmizi + "[" + kirmizi + "-" + kirmizi + "]"
star = yesil + "[" + kirmizi + "*" + yesil + "]"
question = yesil + "[" + kirmizi + "?" + yesil + "]"
exclam = yesil + "[" + kirmizi + "!" + yesil + "]"



def menu():
	print( kirmizi + """   __      __.__        _____       
  /  \    /  \__| _____/ ____\____  
  \   \/\/   /  |/    \   __\/  _ \ 
   \        /|  |   |  \  | (  <_> )
    \__/\  / |__|___|  /__|  \____/ 
         \/          \/             
.:: ACTIVE INFORMATION GATHERING TOOL ::.
          [ Coded By wolkan ]""")


# Parametreler. Help menüsü
parser = argparse.ArgumentParser(description="WINFO Active Information Gathering Tool")
parser.add_argument('-a', '--all' , action='store' , dest='all' , help='Performs all scans in the program')
parser.add_argument('-w', '--whois' , action='store' , dest='whois' , help='Makes a whois query on the target site')
parser.add_argument('-b', '--banner' , dest='banner' , help='Captures the target site banner request')
parser.add_argument('-s', '--subdomain' , dest='subdomain' , help='Detects target subdomains')
parser.add_argument('-d', '--dnslookup' , dest='dnslookup' , help='Performs dns query')
parser.add_argument('-p', '--portscan' , dest='portscan' , help='Scans the ports of the target system')
args = vars(parser.parse_args())

menu()

# Parametrelerin değerleri değişkenlere atanıyor.
winfo_all = args['all']
winfo_whois = args['whois']
banner = args['banner']
traceroute = args['traceroute']
subdomain = args['subdomain']
dnslookup = args['dnslookup']
portscan = args['portscan']

# Eğer programa parametre girilmezse:
if len(sys.argv) == 1:
    sys.exit("\n"+ exclam + " USAGE:" + reset + " winfo.py [-h] [-a ALL] [-w WHOIS] [-b BANNER] [-t TRACEROUTE] [-s SUBDOMAIN] [-d DNSLOOKUP] [-p PORTSCAN]")

# -w parametresi kullanılınırsa:
if winfo_whois:
    w = whois.whois(winfo_whois)
    print("\n"+plus,"Domain Name:",reset,w.domain_name)
    print(plus,"Updated Date:",reset,w.updated_date)
    print(plus,"Creation Date:",reset,w.creation_date)
    print(plus,"Expiration Date:",reset,w.expiration_date)
    print(plus,"Name Servers:",reset,w.name_servers)
    print(plus,"Emails:",reset,w.emails)
    print(plus,"Name:",reset,w.name)
    print(plus,"Organization:",reset,w.org)
    print(plus,"Address:",reset,w.address)
    print(plus,"City:",reset,w.city)
    print(plus,"State:",reset,w.state)
    print(plus,"Postal Code:",reset,w.registrant_postal_code)
    print(plus,"Country:",reset,w.country)

    question = input("\n"+question+" Save results to file(y/n): "+reset)
    
    if question == "y":
        results = open('winfo_whois.txt', 'a')
        results.write(str(w))
        print(exclam,"Successfully saved (winfo_whois.txt)")
    else:
        print(exclam,"Results not saved")


# -b parametresi kullanılınırsa:
if banner:
    response = requests.get("https://"+banner)
    print('\n'+reset,response.headers)
    question = input("\n"+question+" Save results to file(y/n): "+reset)
    
    if question == "y":
        results = open('winfo_httpheader.txt', 'a')
        results.write(str(response.headers))
        print(exclam,"Successfully saved (winfo_httpheader.txt)")
    else:
        print(exclam,"Results not saved")


# -s parametresi kullanılınırsa:
if subdomain:
    find_subdomain = 'https://api.hackertarget.com/hostsearch/?q='+ subdomain
    info = requests.get(find_subdomain)
    print('\n'+reset+info.text)
    question = input("\n"+question+" Save results to file(y/n): "+reset)

    if question == "y":
        results = open('winfo_subdomains.txt', 'a')
        results.write(str(info.text))
        print(exclam,"Successfully saved (winfo_subdomains.txt)")
    else:
        print(exclam,"Results not saved")


# -d parametresi kullanılınırsa:
if dnslookup:
    find_dnslookup = 'https://api.hackertarget.com/dnslookup/?q='+ dnslookup
    info = requests.get(find_dnslookup)
    print('\n'+reset,info.text)
    question = input("\n"+question+" Save results to file(y/n): "+reset)

    if question == "y":
        results = open('winfo_dnslookup.txt', 'a')
        results.write(str(info.text))
        print(exclam,"Successfully saved (winfo_dnslookup.txt)")
    else:
        print(exclam,"Results not saved")


# -p parametresi kullanılınırsa:
if portscan:
    print("\n"+reset+star,reset,"Scanning Target: " + portscan)
    print(reset+star,reset,"Scanning started at:" + str(datetime.now()))
    print("-------------------------------")

    target = socket.gethostbyname(portscan)
  
    try:
        
        for port in range(1,1000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            result = s.connect_ex((target,port))
            if result ==0:
                print(plus,reset,"Port {} is open".format(port))
            s.close()

    except socket.gaierror:
            print("\n"+sour,"Hostname not be resolved")
            sys.exit()

    except socket.error:
            print("\n"+sour,"Server not responding")
            sys.exit()


# -a parametresi kullanılınırsa:
if winfo_all:

    w = whois.whois(winfo_all)
    print("\n"+plus,"Domain Name:",reset,w.domain_name)
    print(plus,"Updated Date:",reset,w.updated_date)
    print(plus,"Creation Date:",reset,w.creation_date)
    print(plus,"Expiration Date:",reset,w.expiration_date)
    print(plus,"Name Servers:",reset,w.name_servers)
    print(plus,"Emails:",reset,w.emails)
    print(plus,"Name:",reset,w.name)
    print(plus,"Organization:",reset,w.org)
    print(plus,"Address:",reset,w.address)
    print(plus,"City:",reset,w.city)
    print(plus,"State:",reset,w.state)
    print(plus,"Postal Code:",reset,w.registrant_postal_code)
    print(plus,"Country:",reset,w.country)
    
    response = requests.get("https://"+winfo_all)
    print('\n'+reset,response.headers)

    find_subdomain = 'https://api.hackertarget.com/hostsearch/?q='+ winfo_all
    info = requests.get(find_subdomain)
    print('\n'+reset+info.text)
    
    find_dnslookup = 'https://api.hackertarget.com/dnslookup/?q='+ winfo_all
    info2 = requests.get(find_dnslookup)
    print('\n'+reset,info2.text)

    print("\n"+reset+star,reset,"Scanning Target: " + winfo_all)
    print(reset+star,reset,"Scanning started at:" + str(datetime.now()))
    print("-------------------------------")

    target = socket.gethostbyname(winfo_all)
  
    try:
        
        for port in range(1,1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            result = s.connect_ex((target,port))
            if result ==0:
                print(plus,reset,"Port {} is open".format(port))
            s.close()

    except socket.gaierror:
            print("\n"+sour,"Hostname not be resolved")
            sys.exit()

    except socket.error:
            print("\n"+sour,"Server not responding")
            sys.exit()

    question = input("\n"+question+" Save results to file(y/n): "+reset)
    
    if question == "y":
        results = open('winfo.txt', 'a')
        results.write(str(w))
        results.write(str(response.headers))
        results.write(str(info.text))
        results.write(str(info2.text))
        print(exclam,"Successfully saved (winfo.txt)")
    else:
        print(exclam,"Results not saved")
