import socket

sock: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', 9090))
sock.listen(1)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print('Server successfully!')

conn, addr = sock.accept()
print('-- Connected ', addr)
msg = b'Welcome to server!'
conn.sendall(msg)

while True:
    data = conn.recv(1024)
    if not data:
        print('Client disconnected.')
        break
    print('CLIENT: ', data.decode())

    msg = input()
    if msg == 'exit':
        sock.close()
        quit()
    conn.sendall(msg.encode())