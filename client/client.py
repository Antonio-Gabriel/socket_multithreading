from typing import Union
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


class Client:

    def __init__(self) -> None:
        # AF_INET: for use ipv4, SOCK_STREAM: for working with TCP
        self.__client = socket(AF_INET, SOCK_STREAM)

    def run(self) -> Union[bool, str]:
        """run and carrie the threadings"""
        
        try:

            self.__client.connect(('localhost', 7777))                        
        except:
            return f"<<Client>> An error occurred to connect, please try again"

        username = input('Device name> ')

        print(f"\n {username}> connected ")

        send_thread = Thread(target=self.__send_message, args=[self.__client, username])
        recive_thread = Thread(target=self.__recive_message, args=[self.__client])

        send_thread.start()        
        recive_thread.start()

    def __recive_message(self, client: socket):
        """always check responses"""
        
        while True:
            try:
                msg = client.recv(2048).decode('utf-8')
                print(f'{msg}\n')
            except:
                alert = """
                    Your connection is down! 

                    press <Enter> to continue
                """
                print(alert)

                client.close()
                break

    def __send_message(self, client: socket, username: str):
        """always capture the client req"""
        
        while True:
            try:
                msg = input('\n')
                client.send(f'{username}> {msg}'.encode('utf-8'))
            except:
                return


# Execution
client = Client()
print(client.run())