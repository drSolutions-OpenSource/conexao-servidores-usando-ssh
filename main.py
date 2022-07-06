from ServerConnectionSsh import *


if __name__ == '__main__':
    scssh = ServerConnectionSsh('root', 'mypass', '192.168.1.20')
    scssh.start_connection()

    scssh.run_command('hostname')
    print(scssh.get_result())

    scssh.close_connection()
