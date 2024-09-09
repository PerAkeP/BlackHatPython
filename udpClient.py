import socket

target_host = "127.0.0.1"
target_port = 9998

def main():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind the same client to the receiving end
    client.bind((target_host, target_port))

    # send some data
    client.sendto(b"Halloj!", (target_host, target_port))

    # receive the data
    data, addr = client.recvfrom(4096)

    print(data.decode())

if __name__ == "__main__":
    main()