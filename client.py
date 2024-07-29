import socket, time, sys

print("\nWelcome to the chat room")
print("\nInitializing...")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")

host = input(str("Enter the server address to connect: "))
name = input(str("Enter your name: "))
port = 1234
print("\nTrying to connect to ", host)
time.sleep(1)

try:
    s.connect((host, port))
    print("Connected...\n")
    s.send(name.encode())
    s_name = s.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has joined the chat room")

    while True:
        message = s.recv(1024)
        message = message.decode()
        print(s_name, ":", message)
        message = input(str("Me: "))
        s.send(message.encode())
except socket.error as e:
    print(f"Connection error: {e}")
