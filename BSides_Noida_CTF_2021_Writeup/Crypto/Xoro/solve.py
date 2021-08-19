# solve.py
from pwn import *

conn = remote('104.199.9.13', 1338)

nulls = '00'*32 # 32 null bytes

conn.sendlineafter('(hex)]>  ', nulls)

# get the ciphertext that the program gives
# and decode it from hex
cipher = bytes.fromhex(conn.recvline().decode().split()[-1])

# Extract key and flag from cipher
key = cipher[:32]
flag = cipher[32:]

flag = xor(flag, key)

print(flag.decode())
