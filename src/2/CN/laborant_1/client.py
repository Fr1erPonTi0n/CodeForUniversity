import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

ipAdr = input('Enter ip adress: ')

sock.connect((ipAdr, 9090))

print('Connection to server...')

data = sock.recv(1024)
print(data.decode('UTF-8'))

while True:
    msg = input()
    if msg == 'exit':
        sock.close()
        quit()
    
    sock.sendall(msg.encode())
    
    data = sock.recv(1024)
    if not data:
        print('Server closed connection.')
        break
    print('SERVER: ', data.decode())