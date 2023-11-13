import socket
MAX_PACKET = 1024
QUEUE_LEN = 1

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

n = 0
try:
    my_socket.bind(('127.0.0.1', 5746))
    my_socket.listen(QUEUE_LEN)

    client_socket, client_address = my_socket.accept()


    try :

        while True:

            if n>1024:
                my_socket.listen(QUEUE_LEN)

                client_socket, client_address = my_socket.accept()
                n = 0
            request = client_socket.recv(MAX_PACKET).decode()

            print('server received ' + request)

            client_socket.send(request.encode())
            if request == '':
                n+=1




    except socket.error as err:

        print('received socket error on client socket' + str(err))

    finally:

        client_socket.close()

except socket.error as err:

    print('received socket error on server socket' + str(err))

finally:

    my_socket.close()