import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        # receive data stream
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()


if __name__ == '__main__':
    server_program()