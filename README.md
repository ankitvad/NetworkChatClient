NetworkChatClient
=================

A Network/LAN chat client using Socket programming in Python.

:So, untested on Windows, but might work. <br>
-Contains 2 Files:
<ul>
<li>server.py<br>The main file that needs to be started on a console first.<br>Contains a variable called "PORT" which can be individually modified based on<br>whatever PORT on the server is free.</li>
<li>client.py<br>This file needs to be startes on any and all the clients which want to connect to the server running the Polling-Chat client<br>Usage:<br>:~$ python client.py <IP_ADDRESS_OF_SERVER> <PORT_NUMBER_AT_SERVER><br>EG: :$ python client.py localhost 5500<br>
PS: default port is 5500.
</li>
</ul>
<br>
To End: Either Disconnect each client individually, and they will leave the server connection list<br>
To terminate the whole setup, on the Server machine enter "Ctrl+c" it sends an interrupt that<br> disconnects the whole service.

