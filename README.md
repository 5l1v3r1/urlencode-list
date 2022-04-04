# urlencode-list

**Advisory**

All the binaries/scripts/code of urlencode-list should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it on your own networks and/or with the network owner's permission.
* * *

**Update**

Just a small update that now includes a new version for Python 3. I have kept the old version as part of the project for now.

**What is this script?**

This was a quick Python script I put together to URL encode / decode lists.

**Why did I create it?**

This can have a lot of uses not just in pentesting / CTF exercises. The reason I made this in particular was because I was in a situation where I could not use a tool such as sqlmap to detect sql injection and instead of manually testing everything off my sql injection cheatsheet I could automate it with a tool like wfuzz.

**Where have I used it?**

I recommend checking out [bootlesshackers](https://twitter.com/bootlesshacker) [Insanity Hosting](https://www.vulnhub.com/entry/insanity-1,536/) machine on Vulnhub for an example box of where this may be useful.

Using Burp Intruder, you can upload a list and there is a tickbox option to automatically URL encode specific characters under **Intruder >> Payloads >> Payload Encoding**.

Now if you have the free version of Burp, using Intruder like this can take a long time especially if you have a large list. It is simple enough to recreate the request for wfuzz (or similar) and use the output of this tool as your input file for wfuzz.

**How else may it help?**

[Insanity Hosting](https://www.vulnhub.com/entry/insanity-1,536/) is just one example - this can be used for many types of attack such as SQL Injection, LFI, RFI, Command Injection, XSS and more.

This script will just URL encode or decode a list but as mentioned above you can see the reasons why I created it and maybe it can help someone else out.

**Notes**

You may not need to URL encode a list every time you want to do an attack like this but having the ability to quickly convert a list so that it is URL encoded or decoded is really useful.

In the near future I will demonstrate how this is achieved using tools such as wfuzz and bypassing the use of fully automated tools such as sqlmap.

**Usage**

Encode a list - print to screen
```
python urlencode-list.py -f sql-cheatsheet.txt
```

Encode a list - output to file
```
python urlencode-list.py -f sql-cheatsheet.txt -o outputfile.txt
```

Decode a list - print to screen
```
python urlencode-list.py -f sql-cheatsheet.txt -d
```

Decode a list - output to file
```
python urlencode-list.py -f sql-cheatsheet.txt -o outputfile.txt -d
```

