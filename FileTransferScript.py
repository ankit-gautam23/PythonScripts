import socket

# create socket
s = socket.socket()

# bind socket to a address and port
s.bind(('localhost', 12345))

# put the socket into listening mode
s.listen(5)

print('Server listening...')

# forever loop to keep server running
while True:
    # establish connection with client
    client, addr = s.accept()
    print(f'Got connection from {addr}')

    # receive the file name
    file_name = client.recv(1024).decode()

    try:
        # open the file for reading in binary
        with open(file_name, 'rb') as file:
            # read the file in chunks
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                # send the chunk to the client
                client.sendall(chunk)

        print(f'File {file_name} sent successfully')
    except FileNotFoundError:
        # if file not found, send appropriate message
        client.sendall(b'File not found')
        print(f'File {file_name} not found')

    # close the client connection
    client.close()
