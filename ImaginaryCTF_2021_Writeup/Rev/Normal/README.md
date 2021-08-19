# Normal 150 points

# Description
Norse senor snorts spores, abhors non-nors, adores s'mores, and snores.

# Attachments
- https://imaginaryctf.org/r/70E7-normal.v
- https://imaginaryctf.org/r/B484-Makefile

# Solution
We are given with a **verilog** source file (normal.v) and a Makefile to compile it.

[Verilog](https://en.wikipedia.org/wiki/Verilog) is a hardware description language (HDL) used to model electronic systems.

I highly recommend you to do quick *google search*, follow some tutorials and try to write a 'Hello World' program in verilog to understand it better.

For now, let's look at the **source**
```
module normal(out, in);
    output [255:0] out;
    input [255:0] in;
    wire [255:0] w1, w2, w3, w4, w5, w6, w7, w8; 

    wire [255:0] c1, c2;
    assign c1 = 256'h44940e8301e14fb33ba0da63cd5d2739ad079d571d9f5b987a1c3db2b60c92a3;
    assign c2 = 256'hd208851a855f817d9b3744bd03fdacae61a70c9b953fca57f78e9d2379814c21;
    
    nor n1 [255:0] (w1, in, c1);
    nor n2 [255:0] (w2, in, w1);
    nor n3 [255:0] (w3, c1, w1);
    nor n4 [255:0] (w4, w2, w3);
    nor n5 [255:0] (w5, w4, w4);
    nor n6 [255:0] (w6, w5, c2);
    nor n7 [255:0] (w7, w5, w6);
    nor n8 [255:0] (w8, c2, w6);
    nor n9 [255:0] (out, w7, w8);
endmodule

module main;
    wire [255:0] flag = 256'h696374667b00000000000000000000000000000000000000000000000000007d;
    wire [255:0] wrong;

    normal flagchecker(wrong, flag);

    initial begin
        #10;
        if (wrong) begin
            $display("Incorrect flag...");
            $finish;
        end
        $display("Correct!");
    end
endmodule
```
If you run *make* command `make` to compile and run it, it always print "Incorrect flag..."

It is because module *normal* (the first module) always returns non-zero (*true*) and `if (wrong) begin` is always triggered

But, in this challenge, we can use **$display** to print out the content of the *flag* and *wrong*.**$display** is just like a **printf** function in *ANSI C*.

```
...
module main;
    wire [255:0] flag = 256'h696374667b00000000000000000000000000000000000000000000000000007d;
    wire [255:0] wrong;

    normal flagchecker(wrong, flag);

    initial begin
        #10;
        if (wrong) begin
            $display("%s", flag);
            $display("%s", wrong);
            $display("Incorrect flag...");
            $finish;
        end
        $display("Correct!");
    end
endmodule
```
Now, run `make` command and the flag will be printed out
```bash
$ make
iverilog -o normal.vvp -s main normal.v
vvp normal.vvp
ictf{                          }
     A11_ha!1_th3_n3w_n0rm_n0r! 
Incorrect flag...
```
*flag*: `ictf{A11_ha!1_th3_n3w_n0rm_n0r!}`

# Another way to solve
If you take a look at the module *normal*, there are some [nor](https://en.wikipedia.org/wiki/NOR_gate) (not or) operations.

The flag is passed as second argument *in*,the first argument *out* is empty and there are some variables assigned with hex values before **nor** operations.

We can guess that the final output of all the *nor* operations must be the flag.

So, I wrote the python script called (solve.py) that does the same thing as the module *normal* and prints out the flag

If you don't know how to do nor operation in python, I recommend you to read [this stackoverflow question](https://stackoverflow.com/questions/19197495/how-to-do-a-bitwise-nor-gate-in-python-editing-python-maths-to-work-for-me).
```python
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
```

Now, run the script, add "ictf{}" and you will get the flag
```
$ python3 solve.py
A11_ha!1_th3_n3w_n0rm_n0r!
```
*flag*: `ictf{A11_ha!1_th3_n3w_n0rm_n0r!}`
