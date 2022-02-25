# CorsDetector
Detect CORS misconfiguration on subdomains.
Pass your list of subdomains and wait for the results :)

You can also pass command line subdomain list.

#Usage
```
corsdetec.py [-h] [--subdomain SUBDOMAIN [SUBDOMAIN ...]] [--list LIST] [--out OUT] [--N]

optional arguments:
  -h, --help            show this help message and exit
  --subdomain SUBDOMAIN [SUBDOMAIN ...]
                        Single or Multiple Subdomains with spaces
  --list LIST           Provide list of subdomains with --out file
  --out OUT             Provide a output file name
  --N                   Check for NULL origin

```

#Options

- --list: Provide a list of subdomain as a *.txt* file
- --out: Out file to store results with *--list*
```
corsdetec.py --list subs.txt --out results.txt
```
- --subdomain: Pass command line list of subdomain with spaces
```
corsdetec.py --subdomain evil.com example.com lol.com
```
- --N: To check for *null* origin for both modes

```
Subdomain list:
corsdetec.py --N --list subs.txt --out results.txt

Command line list:
corsdetec.py --N --subdomain evil.com example.com lol.com

```

Enjoy!!!!
