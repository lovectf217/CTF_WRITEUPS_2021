# in verilog 'h' is a prefix for hex
# So, we remove it in python and add 0x at the beginning
flag = 0x696374667b00000000000000000000000000000000000000000000000000007d

c1 = 0x44940e8301e14fb33ba0da63cd5d2739ad079d571d9f5b987a1c3db2b60c92a3
c2 = 0xd208851a855f817d9b3744bd03fdacae61a70c9b953fca57f78e9d2379814c21

# in verilog, the syntax nor n1 [255:0] (w1, in, c1) means do nor (not or) operation with in and c1 and store it in w1
w1 = ((flag | c1) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w2 = ((flag | w1) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w3 = ((c1 | w1) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w4 = ((w2 | w3) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w5 = ((w4 | w4) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w6 = ((w5 | c2) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w7 = ((w5 | w6) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
w8 = ((c2 | w6) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)

out = ((w7 | w8) ^ 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)

# Make flag in hex format
# [2:] to remove the 0x at the beginning
out = hex(out)[2:]

# Make the flag ascii readable and print it
print(bytes.fromhex(str(out)).decode("UTF-8"))
