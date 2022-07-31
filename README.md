# SOCKET MULTITHREADING

## Idea
Communication between clients, always that exists a new connections or instance, the server add the instance connection an a threading list. If the connections is down the instance is removed of thread list.

The client send a message into server and the server distribute for all devices connected on the thread list.

## Figure
<img src="https://3.bp.blogspot.com/-_h4s7PyjIjg/VgD9FP_Ch4I/AAAAAAAAH_g/T66Rh3bjNa0/w1200-h630-p-k-no-nu/Server-client-01.jpg" alt="communication between client and server">

The broadcast will distribute the message for devices of thread list minus the device that sending the message

### Starting the `server` and `client` example
After start, If server is already running, return a message

```python

python3 server/server.py

> listen

# Msg
# <<Server>> The server is already running

```

For client after connect input the client name

```python 

python3 client/client.py 

Device name> António

António> connected

On this section you can write your message for send to other devices

```
Preview of interaction per messages

```python

Device name> António

António> connected

Pedro> Hi, you are fine?
Pedro> news

```
Thread of server

```python
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

```

## License

The socket_multithreading is licensed under the MIT license.