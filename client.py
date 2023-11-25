import socket


def main():

    try:
        # Connecting
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect(("127.0.0.1", 5746))
        request = input()

        # Loop until getting EXIT
        while request != "EXIT":

            # Doesnt do nothing when we pull enter
            if request == '':
                request = input()

            # Sends to the server our request
            else:
                my_socket.send(request.encode())
                data = my_socket.recv(1024).decode()
                print(data)
                request = input()
        print('bye')
    # If we have any errors
    except socket.error as err:
        print('recieved socket error ' + str(err))

    # Closing the programm any way
    finally:
        my_socket.close()

if __name__ == '__main__':
    main()
