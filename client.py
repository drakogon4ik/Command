"""
Author: Oleg Shkolnik יא9.
Description: Client that receive input commands from cmd, send them to the server, receive result and print it.
Date: 6/12/23
"""
import socket

IP = "127.0.0.1"
PORT = 5746
PROMPT = 'Please enter a command(NAME/TIME/RAND/EXIT): '
COMMANDS = ['NAME', 'TIME', 'RAND', 'EXIT']


def validate_command(cmd: str):
    """
    validates that the user input is valid
    :param cmd: the user command
    :return: true if the command is valid
    """
    return cmd in COMMANDS


def main():
    """
    main function that connect client to server
    """
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        """
        connecting
        """
        my_socket.connect((IP, PORT))
        request = input(PROMPT)

        while request != COMMANDS[3]:
            """
            loop until getting EXIT
            """

            if validate_command(request):
                """
                if command exist - continue
                if not - send message with available functions and go to loop from the start
                """

                if request != '':
                    """
                    sending request to the server end receive answer
                    """
                    my_socket.send(request.encode())
                    data = my_socket.recv(1024).decode()
                    print(data)

            else:
                print('invalid command. available commands are: NAME/TIME/RAND/EXIT:')

            request = input(PROMPT)

        """
        after the loop send message and go to finally closing socket
        """
        print('bye bye')

    except socket.error as err:
        """
        for errors
        """
        print('received socket error ' + str(err))

    finally:
        """
        close the socket anyway
        """
        my_socket.close()


if __name__ == '__main__':
    assert validate_command('EXIT')
    assert validate_command('NAME')
    assert validate_command('RAND')
    assert validate_command('TIME')
    assert not validate_command('Oleg')
    main()
