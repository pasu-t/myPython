import re

ip_text = """wfohegndfknbd
fklbn 192.168.0.1 sdlgn
dgdgnkdjfgbds.,b b,d,gndgfnfgn255.255.255.0 fd fgnhdofighdoghidhigdfghdfgbkdfgbdfg 1.1.1.1 dkgnihrtyrt 11.128.0.1 sdfndfhdfgnk2.2.2 sdkfih
ifuhfgdjk 888.1.1.1odiuhthnhndfh
2001:0db8:85a3:0000:0000:8a2e:0370:7334
2001:0db8:85a3:0000:0000:8a2e:0370:t334
2001:0db8:85a3:0000:0000:8a2e:0370:733t
fe80:0db8:85a3:0000:0000:8a2e:0370:7
00:0a:95:9d:68:16 WSEGERG FSFSDF  00:0A:95:9D:68:FZ
00:0A:95:9D:68:FA
Windows IP Configuration


Ethernet adapter Npcap Loopback Adapter:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::1851:d72f:b0ec:e72e%20
   Autoconfiguration IPv4 Address. . : 169.254.231.46
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . :

Ethernet adapter VirtualBox Host-Only Network:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::c584:2bc3:75a9:346a%8
   IPv4 Address. . . . . . . . . . . : 192.168.56.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Wireless LAN adapter Local Area Connection* 3:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 14:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::14b8:efe7:daba:247%18
   IPv4 Address. . . . . . . . . . . : 192.168.0.101
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
 """

ipv4_pattern = re.compile(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\b")
ipv4_matches = ipv4_pattern.finditer(ip_text)

ipv6_pattern = re.compile(r"(([a-fA-F0-9]{1,4}\:){7}([a-fA-F0-9]{1,4}))\b") #\b required to make sure word boundary at the end
ipv6_matches = ipv6_pattern.finditer(ip_text)

mac_pattern = re.compile(r"(([a-fA-F0-9]{2}\:){5}[a-fA-F0-9]{2})\b") #\b required to make sure word boundary at the end
mac_matches = mac_pattern.finditer(ip_text)

for match in ipv4_matches:
    print(match)

for match in ipv6_matches:
    print(match)

for match in mac_matches:
    print(match)