'''
The Client Module to handle all the 
connected clients.

USAGE: $> python client.py <IP_ADDRESS> <Port_No.>
eg:
$> python client.py localhost 1500

'''
import socket, select, string, sys
 
def throw_message() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()
 
#Loading The Main Function :
if __name__ == "__main__":

    #Condition to check i/p from terminal is in correct syntax.
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py server_hostname server_port'
        sys.exit()
     
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    #starting socket on client to connect to the server port.
    #TCP
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    #Connecting to the server Host:
    try :
        s.connect((server_host, server_port))
    except :
        print 'Unable To Connect To the serer. Some problem occured. Exiting.'
        sys.exit()
     
    print 'You are connected to the Server. Please Start Sending Messages.'
    throw_message()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
         #getting all messages now:
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096) #Here the length should be same as that of the server port polling: 4096
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #Throw data for printing.
                    sys.stdout.write(data)
                    throw_message()
             
            #User Entering Message...
            else :
                brdcst_msg = sys.stdin.readline()
                s.send(brdcst_msg)
                throw_message()