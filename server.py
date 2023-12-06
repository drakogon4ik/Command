"""
Author:
Date:
Description
"""
import socket
from datetime import datetime
import random

MAX_PACKET = 1024

QUEUE_LEN = 1

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
n = 0
try:

    # Set up server
    my_socket.bind(('127.0.0.1', 5746))

    my_socket.listen(QUEUE_LEN)

    client_socket, client_address = my_socket.accept()

    try:

        while True:

            # If server see that we dont put nothing a lot of time, reconnecting it
            if n > 1024:

                client_socket, client_address = my_socket.accept()
                n = 0

            # Getting request
            request = client_socket.recv(MAX_PACKET).decode()
            print('server received ' + request)

            # Calculating every time we skip
            if request == '':
                n += 1

            # Making commands and sending them
            elif request == "TIME":
                response = str(datetime.now().time())
                client_socket.send(response.encode())

            elif request == "NAME":
                response = "The name of server is ObnS's server"
                client_socket.send(response.encode())

            elif request == "RAND":
                response = str(random.randint(1, 10))
                client_socket.send(response.encode())

            elif request == "EXIT":
                response = "bye"
                client_socket.send(response.encode())

            else:
                response = 'Command was written not right. Please try again.'
                client_socket.send(response.encode())

    # If we have any errors
    except socket.error as err:

        print('received socket error on client socket' + str(err))

    # Closing client
    finally:

        client_socket.close()

# If we have any errors
except socket.error as err:

    print('received socket error on server socket' + str(err))

# Closing the program any way
finally:

    my_socket.close()
