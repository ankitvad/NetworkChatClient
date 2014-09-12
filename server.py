"""
Creating a Chat Programming
Using Python Socket Programming,
Has a working server, and a client to mod
chat/message content.

Uses the TCP techinque in python Socket library.
"""
#Server Design
import socket, select
 
#Message structure to facilitate Broadasting of Message to all connected Clients.
#After receiving Message from a client, don't send it back to him. Redundant Message.
def push_data (sock, broadcast_message):
    #Do not send the broadcast_message to master temp_socket and the client who has send us the broadcast_message
    for temp_socket in connection_list:
        if temp_socket != server_socket and temp_socket != sock :
            try :
                temp_socket.send(broadcast_message)
            except :
                '''
                If for some reason the socket connection fails, 
                because of port problems or so...
                We need to close socket, or port gets jammed.
                '''
                temp_socket.close()
                connection_list.remove(temp_socket)

'''
starting a __name__ = "main" function
so that when client.py interacts with the
server.py program, it tells where it got imported from..
just random modules stuff, Gotta Love Python :P
'''
 
if __name__ == "__main__":
     
    #Array to store all new sockets and stuff one by one.
    connection_list = [] 
    message_buffer = 4096 # setting an upper limit on the amount of character per message.
    PORT = 5500
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT)) 
    #sort of a istening timer. Polling for new messages.
    #also as server is part of the connections, add it to the ist of clients ^^
    server_socket.listen(10)
 
    # Add server temp_socket to the list of readable connections
    connection_list.append(server_socket)
 
    print "LAN Server is Running on PORT :" + str(PORT)
 
    while 1:
        '''
        The select function aows us to get all the socket of clients that
        are ready to be read and push/broadcast data.
        '''
        read_sockets,write_sockets,error_sockets = select.select(connection_list,[],[])
 
        for sock in read_sockets:
            #New Client connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                connection_list.append(sockfd)
                #This wil be visible on the server screen.
                print "Client (%s, %s) connected" % addr
                #This will be pushed subsequently to all clients running at the moment.
                #connected to the main server.py file. 
                push_data(sockfd, "[%s:%s] entered room\n" % addr)
             
            #If message is recieved..
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(message_buffer)
                    if data:
                        push_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)   #Gets the IP.            
                 
                except:
                    #Pushed to all clients console.
                    push_data(sock, "Client (%s, %s) is offline" % addr)
                    #Displayed on Server screen.
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    connection_list.remove(sock)
                    continue
     
    server_socket.close()