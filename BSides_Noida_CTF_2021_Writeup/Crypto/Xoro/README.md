# Xoro 388 points

# Description
"You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face." – Roronoa Zoro

Connection : `nc 104.199.9.13 1338`
# Attachments
[chall link](https://storage.googleapis.com/noida_ctf/Crypto/xoro.py)

# Solution
If we connet with `nc 104.199.9.13 1338`, it asks for plain text in *hex* and when we give that, it will give the cipher text back
```
$ nc 104.199.9.13 1338
===== WELCOME TO OUR ENCRYPTION SERVICE =====

[plaintext (hex)]>  41414141
[ciphertext (hex)]> 9003faa1a9f690ddcb605180c518972e57ae6c2a1945717dda301fb96aeb3ce9941de3afb9fae1939d254d
See ya ;)
```
Let's look at the given code (xoro.py)!
```python
#!/usr/bin/env python3
import os

FLAG = open('flag.txt','rb').read()

def xor(a, b):
    return bytes([i^j for i,j in zip(a,b)])

def pad(text, size):
    return text*(size//len(text)) + text[:size%len(text)]

def encrypt(data, key):
    keystream = pad(key, len(data))
    encrypted = xor(keystream, data)
    return encrypted.hex()


if __name__ == "__main__":
    print("\n===== WELCOME TO OUR ENCRYPTION SERVICE =====\n")
    try:
        key = os.urandom(32)
        pt = input('[plaintext (hex)]>  ').strip()
        ct = encrypt(bytes.fromhex(pt) + FLAG, key)
        print("[ciphertext (hex)]>", ct)
        print("See ya ;)")
    except Exception as e:
        print(":( Oops!", e)
        print("Terminating Session!")
```

The **flag** is stored in a variable called `FLAG`.

The program store key with **32 bytes long** random string from [os.urandom(32)](https://docs.python.org/3/library/os.html#os.urandom).Next, it gets our input.And, then, it concatenate our input with *flag* and passes it as first argument to `encrypt` function.

The `encrypt` function will return *cipher text* and the program print it.

Let's look at the `encrypt` function!
```python
def encrypt(data, key):
    keystream = pad(key, len(data))
    encrypted = xor(keystream, data)
    return encrypted.hex()
```
It first calls `pad` function with *key* and length of *data* ( which is our input + flag ) as arguments and stores the result in *keystream*

Next, it passes the *keystream* and *data* to `xor` function

And, return the result

The `pad` function
```python
def pad(text, size):
    return text*(size//len(text)) + text[:size%len(text)]
```
What does this function do is make the length of *text* ( key ) equals to *size* ( length of our input + flag )

for example:
Let's *key* be 'abcd' and *flag* be 'zzzz'

If our input is 'aaaa', this function returns 'abcdabcd'

If our input is 'aa', then it returns 'abcdab'

The `xor` function:
```python

def xor(a, b):
    return bytes([i^j for i,j in zip(a,b)])
```
The function do xor operation *byte* by *byte* in two strings *a* ( keystream ) and *b* ( our input + flag )

So far we understand what the program does

One thing is if we *xor* the *key* with **NULL** ( \x00 in hex ), it gives the *key* back

So, if we send 32 '00' ( because the key length is 32 ), the program must give the key

And, because of the `pad` function, the flag will be **xored** from the start of the *key*

Finally, we have to decrypt *flag* with the *key* and we will get the flag

I will use a *python script* to do that

```python
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
```

Run it
```
$ python3 solve.py
[+] Opening connection to 104.199.9.13 on port 1338: Done
BSNoida{how_can_you_break_THE_XOR_?!?!}
[*] Closed connection to 104.199.9.13 port 1338
```

*flag*: `BSNoida{how_can_you_break_THE_XOR_?!?!}`
