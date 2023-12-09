"""
Author: Oleg Shkolnik יא9.
Description: Client that receives input commands from cmd, sends them to the server, receives result and prints it
Date: 7/12/23
"""

import socket

IP = "127.0.0.1"
PORT = 5746
MAX_PACKET = 1024

PROMPT = 'Please enter a command(NAME/TIME/RAND/EXIT): '
ERR = 'Invalid command. Available commands are: NAME/TIME/RAND/EXIT:'
COMMANDS = ['NAME', 'TIME', 'RAND', 'EXIT']


def validate_command(cmd: str):
    """
    Validates that the user input is valid
    :param cmd: the user command
    :return: true if the command is valid
    """
    return cmd in COMMANDS


def main():
    """
    Main function that connect client to server
    """
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        """
        Connecting
        """
        my_socket.connect((IP, PORT))
        request = input(PROMPT)

        while request != COMMANDS[3]:
            """
            Loop until getting EXIT
            """

            if validate_command(request):
                """
                If command exist - continue
                If not - send message with available functions and go to loop from the start
                """

                my_socket.send(request.encode())
                data = my_socket.recv(MAX_PACKET).decode()
                print(data)

            else:
                print(ERR)

            request = input(PROMPT)

        """
        After the loop send message and go to finally closing socket
        """
        print('bye bye')

    except socket.error as err:
        """
        Send the name of error in error situation
        """
        print('received socket error ' + str(err))

    finally:
        """
        Close the socket anyway
        """
        my_socket.close()


if __name__ == '__main__':
    """
    checking function situations and launching the main
    """
    assert validate_command('EXIT')
    assert validate_command('NAME')
    assert validate_command('RAND')
    assert validate_command('TIME')
    assert not validate_command('Oleg')
    main()
