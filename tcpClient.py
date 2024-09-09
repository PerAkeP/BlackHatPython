import socket

target_host = "127.0.0.1"
target_port = 9998

def main():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client to the sever
    client.connect((target_host, target_port))

    # send some data
    client.send(b"ABCDEF")

    # receive some data
    response = client.recv(4096)

    print(response.decode())
    client.close()

if __name__ == "__main__":
    main()