import math
a= 10 % 3
print (a)
tunnel = """
....: interface Tunnel0
....: ip address 10.10.10.1 255.255.255.0
....: ip mtu 1416
....: ip ospf hello-interval 5
....: tunnel source FastEthernet1/0
....: tunnel protection ipsec profile DMVPN
....: """

intf = "interface"
tun = "tunnel0"

#print (intf + ' ' + tun)

#print (intf * 5)

string1 = 'interface FastEthernet1/0'
print (string1[10:])
print (string1[-3:])
a = "1234556790"
print (a[::-1])
