#!/usr/local/bin/python3

from enum import Enum

def compat_ord(c):
    if type(c) is int:
        return c
    else:
        return ord(c)

class AuthMethod(Enum):
    
    NO_AUTHENTICATION_REQUIRED = 0x00
    GSSAPI = 0x01
    USERNAME_PASSWORD = 0x02
    NO_ACCEPTABLE = 0xFF

class AddressType(Enum):

    IPV4 = 0x01 # 4 octets
    DOMAINNAME = 0x03 # address field (DST.ADDR, BND.ADDR)
    IPV6 = 0x04 # 16 octets

class Socks5Command(Enum):

    CONNECT = 0x01
    BIND = 0x02
    UDP_ASSOCIATE = 0x03


CODES = {
        0x01: "general SOCKS server failure",
        0x02: "connection not allowed by ruleset",
        0x03: "Network unreachable",
        0x04: "Host unreachable",
        0x05: "Connection refused",
        0x06: "TTL expired",
        0x07: "Command not supported",
        0x08: "Address type not supported",
        0xFF: "All methods not allowed"
    }

