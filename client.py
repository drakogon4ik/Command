"""
Author:
Description:
Date:
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

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connecting
        my_socket.connect((IP, PORT))
        request = input(PROMPT)

        # Loop until getting EXIT
        while request != "EXIT":
            if validate_command(request):
                # Doesnt do nothing when we pull enter
                if request == '':
                    request = input()

                # Sends to the server our request
                else:
                    my_socket.send(request.encode())
                    data = my_socket.recv(1024).decode()
                    print(data)
                    request = input()
            else:
                print('invalid command')
        my_socket.send(request.encode())
        data = my_socket.recv(1024).decode()
        print(data)
        
    # If we have any errors
    except socket.error as err:
        print('recieved socket error ' + str(err))

    # Closing the program any way
    finally:
        my_socket.close()


if __name__ == '__main__':
    assert validate_command('EXIT')
    assert validate_command('NAME')
    assert validate_command('RAND')
    assert validate_command('TIME')
    assert not validate_command('Oleg')
    main()
