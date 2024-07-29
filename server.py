import time, socket, sys

print("\nWelcome to the chat room")
print("Initializing...")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234

try:
    s.bind(("0.0.0.0", port))  # Bind to all interfaces
    print(f"Server started at {host} ({ip}) on port {port}\n")
except socket.error as e:
    print(f"Error binding to socket: {e}")
    sys.exit()

name = input(str("Enter your name: "))
s.listen(1)
print("\nWaiting for incoming connection...")
conn, addr = s.accept()
print("\nReceived connection from ", addr[0], "(", addr[1], ")")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")
conn.send(name.encode())

while True:
    message = input(str("Me: "))
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
