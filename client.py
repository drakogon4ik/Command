import socket
from datetime import datetime
import random

MAX_PACKET = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    my_socket.connect(('127.0.0.1', 5746))
    n = input()
    if n == "EXIT":
        my_socket.send('bye'.encode())

        response = my_socket.recv(MAX_PACKET).decode()
        print(response)
    while n != "EXIT":
        if n == "TIME":
            time = str(datetime.now().time())
            my_socket.send(time.encode())

            response = my_socket.recv(MAX_PACKET).decode()

        elif n == "NAME":
            my_socket.send("The name of server is ObnS's server".encode())

            response = my_socket.recv(MAX_PACKET).decode()

        elif n == "RAND":
            num = str(random.randint(1, 10))
            my_socket.send(num.encode())

            response = my_socket.recv(MAX_PACKET).decode()

        else:
            my_socket.send('Command was written not right. Please try again.'.encode())

            response = my_socket.recv(MAX_PACKET).decode()

        print(response)
        n = input()

        if n == "EXIT":
            my_socket.send('bye'.encode())

            response = my_socket.recv(MAX_PACKET).decode()
            print(response)


except socket.error as err:

    print('received socket error ' + str(err))

finally:

    my_socket.close()