from typing import Optional
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


class Server:

    def __init__(self) -> None:
        self.__clients = []

    def run(self) -> Optional[str]:
        """run and connect"""
        
        # AF_INET: for use ipv4, SOCK_STREAM: for working with TCP
        server = socket(AF_INET, SOCK_STREAM)

        try:
            server.bind(('localhost', 7777))

            # limit 10 connections
            server.listen(10)

        except:
            return f"<<Server>> The server is already running"

        while True:
            client, addr = server.accept()
            self.__clients.append(client)

            msg_thread = Thread(target=self.__msg_treatment, args=[client])
            msg_thread.start()

    def __msg_treatment(self, client: socket):
        """msg treatment"""
        while True:
            try:

                msg = client.recv(2048)

                # broadcast
                self.__broadcast(msg, client)
            except:
                self.__remove_client_thread(client)
                break

    def __broadcast(self, msg: str, client: socket):
        """send message for all devices of network minus the client that send the message"""
        for device in self.__clients:
            if device != client:
                try:

                    device.send(msg)
                except:
                    self.__remove_client_thread(device)                    

    def __remove_client_thread(self, client: socket):
        """remove the client disconected into thread list"""

        self.__clients.remove(client)


# Execution
server = Server()
print(server.run())