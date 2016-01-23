EZ TCP Messenger
========================

**Author:** Jayden Navarro

**Email:** jdndeveloper@gmail.com

**LinkedIn:** [Jayden Navarro](https://www.linkedin.com/in/jaydennavarro)

**Twitter:** [@JaydenNavarro](https://twitter.com/JaydenNavarro)

**Google+:** [Jayden Navarro](https://plus.google.com/u/0/+JaydenNavarro/posts)

**GitHub:** [JDNdeveloper](http://www.github.com/JDNdeveloper)

## Description:
A simple TCP Instant Messaging app that allows for real time communication using TCP.

Start up `ezTCPapp.py`, enter your name, a target IP address, a target port (ex. 5005), 
and a local port (ex. 5005). Then do the same on the target computer and you're ready 
to start chatting! Once you get the `CONNECTED` message, you can start typing and use 
enter to send. To stop the connection hit enter three times.

Make sure to have both `ezTCPapp.py` and `ezTCPlib.py` downloaded and in the same 
directory.

It is best to start the app from commandline rather than in Python's IDLE.

There are Python 2 and Python 3 versions of the program. For the Python 2 version 
go to `src-python2`, for the Python 3 version go to `src-python3`.

**NOTE:** This will only work on Local Area Networks using internal IP addresses. To find 
your internal IP address go to commmandline and type "ipconfig" on Windows and "ifconfig" 
on a Mac or Linux machine. The address should start with 192.168.

##Example:
Let's say that Bob at IP address 192.168.0.104 wants to talk to Kate at IP address 
192.168.0.105. 

Bob starts up `./ezTCPapp.py` and types the following:

`Enter your first name:` Bob

`Enter target IP address:` 192.168.0.105

`Enter target port:` 5005

`Enter local port:` 5003

`Waiting for remote connection...`

Now on Kate's end, she starts `./ezTCPapp.py` and types the following:

`Enter your first name:` Kate

`Enter target IP address:` 192.168.0.104

`Enter target port:` 5003

`Enter local port:` 5005

`Waiting for remote connection...`

`CONNECTED`

Now just start typing and hit enter! Pressing enter three times quits the shell.
