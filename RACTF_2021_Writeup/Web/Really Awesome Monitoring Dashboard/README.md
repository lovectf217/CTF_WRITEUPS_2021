# Really Awesome Monitoring Dashboard 250 points

# Description
My Challenge instance: `193.57.159.27:25776` (Yours may be different)

`🌟 Perfect infrastructure 🌟`

# Solution
I navigated to the given *address* in web browser.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info1.png">

The website uses really awesome *Grafana* dashboard.

There are *login* page, *search* page,etc and I tried XSS,Sqli,... in there but nothing worked.

But, when I opened *network* tab, I found an interesting *post* request to **query**.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info2.png">

In the body of the request, I found a **sqlite query**.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info3.png">

There must be a database in the backend!!!

I tried to edit the *query* with the one that could give me the list of *tables* in the database and sent it.

*payload*: `SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';`

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info4.png">

In the response, there were list of tables ( **logs** and **flags** ).

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info5.png">

There must be **flag** in `flags` table.

So, I used `SELECT * FROM flags;` payload to get everything in `flags` table;

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info6.png">

Response

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Web/Really%20Awesome%20Monitoring%20Dashboard/info7.png">

And, there was the flag!

*flag*: `ractf{BringBackNagios}`
