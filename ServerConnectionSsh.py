import paramiko
import socket


class ServerConnectionSsh:
    username = None
    password = None
    host = None
    remote_port = None
    server_connection = None
    result = ''

    def __init__(self, username, password, host, remote_port=22):
        """Initialize the class that executes commands through SSH

        :param username: SSH User
        :param password: SSH Password
        :param host: Remote equipment IP
        :param remote_port: Remote equipment port
        """
        self.username = username
        self.password = password
        self.host = host
        self.remote_port = remote_port

    def start_connection(self):
        """Start the connection to the remote equipment using SSH
        """
        self.server_connection = paramiko.SSHClient()
        self.server_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.server_connection.connect(self.host, username=self.username, password=self.password,
                                           port=self.remote_port, timeout=5)
        except paramiko.SSHException as error:
            exit(f'Error: {error}')
        except paramiko.ssh_exception.NoValidConnectionsError as error:
            exit(f'Error: {error}')
        except socket.gaierror as error:
            exit(f'Error: {error}')
        except socket.timeout as error:
            exit(f'Error: {error}')

    def close_connection(self):
        """End the connection with the remote equipment
        """
        self.server_connection.close()

    def run_command(self, remote_command):
        """Execute a command on the remote equipment

        :param remote_command: Command to be executed
        """
        (stdin, stdout, stderr) = self.server_connection.exec_command(remote_command)
        self.result = stdout.read().decode()

    def get_result(self):
        """Result of the command executed

        :return: Result of the command executed
        """
        return self.result
