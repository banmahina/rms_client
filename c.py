import socket

from colorama import init, Fore, Back, Style

init(autoreset=True)

HOST = "46.146.231.207"
PORT = 5000
connection_check = 1
HEARTBEAT_INTERVAL = 5 # seconds
TIMEOUT_INTERVAL = 10 # seconds

login = "VAMG"
passwd = 1212

#client_socket.connect((HOST, PORT))
print(Fore.GREEN + "| Starting...")
#client_socket.settimeout(25)



def main():
    
    while True:

   

        send_data = input(Fore.MAGENTA + "| Enter: ")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        client_socket.send(send_data.encode())

       
        data = client_socket.recv(1024)
        
        #client_socket.sendall(bytes(send_data, "utf-8"))
       
       

        #print(Fore.RED + "~$ " + Fore.WHITE + 'Recived: ', data.decode())
        print(Fore.RED + "~$", data.decode())
        if send_data == "exit":
            print(Fore.LIGHTBLACK_EX + "------EXIT------")
            exit()

        client_socket.close()
        

def on_start():
   check = 0
   try:
       print(Fore.GREEN + "| Check connection...")
       test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       test_socket.connect((HOST, PORT)) 
        # originally, it was 
        # except Exception, e: 
        # but this syntax is not supported anymore. 
   except Exception as e: 
        print(Fore.RED + "| something's wrong with %s:%d. Exception is %s" % (HOST, PORT, e))
        print(Fore.RED + '| Socket is not readable')
   else:
        print(Fore.GREEN + "| Server is online")
        test_socket.close()
        main()



if connection_check == 1 :
    on_start()
    
    
