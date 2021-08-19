# Missing Tools 250 Points

# Description
My Challenge instance: `193.57.159.27:21477` (Yours may be different)

Man, my friend broke his linux install pretty darn bad. He can only use like, 4 commands. Can you take a look and see if you can recover at least some of his data?

Username: `ractf`<br>
Password: `8POlNixzDSThy`

Note: it may take a minute or more for your container to start depending on load

# Solution
**Username** and **Password** are given.So, I used **ssh** to connect to the target host.

`ssh ractf@193.57.159.27 -p 21477`

As I connect, I am greeted with a message.
```sh
Linux restricted shell
$ 
```
From the message, I knew I had to *bypass* **restricted shell**.

Let's try some commands first.

```sh
$ ls
This command has been disabled by your administrator.
$ pwd
/home/ractf
$ whoami
ractf
$
```

I am in `/home/ractf` directory and I can't list the directory because `ls` is blocked.

But, I can use **echo** ( which prints back whatever we give as argument ) and **asterisk** [wildcard](https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/) `*` trick to list the *directory*

```sh
$ echo *
flag.txt
$ cat flag.txt
This command has been disabled by your administrator.
```

I can see the `flag.txt` file but I can't execute `cat` command to see what's in it.

We can't also use [reading file with bash](https://linuxhint.com/read_file_line_by_line_bash/) trick because there is no `read` command in our target

```sh
$ while read line; do echo $line; done < *
-sh: read: No such file or directory
```

I decided to check what are in `/usr/bin/` and `/bin/` because they are **directories** that contains most of the executable files

```sh
$ echo /usr/bin/*
/usr/bin/cal /usr/bin/dirname /usr/bin/eject /usr/bin/file /usr/bin/lsof /usr/bin/mkpasswd /usr/bin/sha256sum /usr/bin/split /usr/bin/test /usr/bin/time /usr/bin/wc /usr/bin/whoami /usr/bin/yes
$ echo /bin/*
/bin/[ /bin/bash /bin/cat /bin/date /bin/dir /bin/echo /bin/false /bin/grep /bin/head /bin/help /bin/less /bin/ls /bin/more /bin/pwd /bin/sh /bin/sleep /bin/sync /bin/tail /bin/toysh /bin/true /bin/vi /bin/vim
```

I searched all these programs in [GTFOBins](https://gtfobins.github.io/) to find how to read files with them.

But, that didn't help.

I tried some [built in bash commands](https://manpages.ubuntu.com/manpages/bionic/man7/bash-builtins.7.html) that can give me the informations about the *flag* file

And, in the end I found the flag with `source` command

```sh
$ source *
source: ractf{std0ut_1s_0v3rr4ted_spl1t_sha}: No such file or directory
```

*flag*: `ractf{std0ut_1s_0v3rr4ted_spl1t_sha}`
