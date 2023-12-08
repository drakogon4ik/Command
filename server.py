"""
Author: Oleg Shkolnik יא9.
Description: Server that makes one of available commands (NAME/TIME/RAND/EXIT) and sends result to client
Date: 7/12/23
"""

import socket
from datetime import datetime
import random

MAX_PACKET = 1024
QUEUE_LEN = 1
IP = "127.0.0.1"
PORT = 5746

COMMANDS = ['NAME', 'TIME', 'RAND', 'EXIT']


def do_functions(request: str):
    """
    Return action that user wants
    :param request: the user command
    :return: action depending on the command goal
    """
    if request == COMMANDS[0]:
        result = "The name of server is ObnS's server"

    elif request == COMMANDS[1]:
        result = datetime.now().time()

    elif request == COMMANDS[2]:
        result = random.randint(1, 10)
    else:
        result = False
    return result


def main():
    """
    Setting ip and port
    """
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        """
        Set upping server
        """
        my_socket.bind((IP, PORT))
        my_socket.listen(QUEUE_LEN)

        while True:
            """
            Server is always ready to connect new client
            """
            client_socket, client_address = my_socket.accept()

            try:

                while True:
                    """
                    Getting request
                    Making command
                    Sending result of command execution
                    """

                    request = client_socket.recv(MAX_PACKET).decode()
                    print('server received ' + request)

                    if request == 'EXIT':
                        break

                    else:
                        response = str(do_functions(request))

                    client_socket.send(response.encode())

            except socket.error as err:
                """
                Send the name of error in error situation
                """
                print('received socket error on client socket' + str(err))

            finally:
                """
                Close the socket anyway
                """
                client_socket.close()

    except socket.error as err:
        """
        Send the name of error in error situation
        """
        print('received socket error on server socket' + str(err))

    finally:
        """
        Close the socket anyway
        """
        my_socket.close()


if __name__ == '__main__':
    """
    checking function situations and launching the main
    """

    assert do_functions('NAME')
    assert do_functions('RAND')
    assert do_functions('TIME')
    assert not do_functions('EXIT')
    main()
