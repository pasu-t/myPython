import re

ip_text = """wfohegndfknbd
fklbn 192.168.0.1 sdlgn
dgdgnkdjfgbds.,b b,d,gndgfnfgn255.255.255.0 fd fgnhdofighdoghidhigdfghdfgbkdfgbdfg 1.1.1.1 dkgnihrtyrt 11.128.0.1 sdfndfhdfgnk2.2.2 sdkfih
ifuhfgdjk 888.1.1.1odiuhthnhndfh
2001:0db8:85a3:0000:0000:8a2e:0370:7334
2001:0db8:85a3:0000:0000:8a2e:0370:t334
2001:0db8:85a3:0000:0000:8a2e:0370:733t
fe80:0db8:85a3:0000:0000:8a2e:0370:7"""

ipv4_pattern = re.compile(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\b")
ipv4_matches = ipv4_pattern.finditer(ip_text)

ipv6_pattern = re.compile(r"(([a-fA-F0-9]{1,4}\:){7}([a-fA-F0-9]{1,4}))\b") #\b required to make sure word boundary at the end
ipv6_matches = ipv6_pattern.finditer(ip_text)

for match in ipv4_matches:
    print(match)

for match in ipv6_matches:
    print(match)