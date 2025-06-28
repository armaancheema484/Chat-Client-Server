import socket
import threading

HOST = '0.0.0.0'
PORT = 5555

clients = {}  # socket -> username

def broadcast(message, sender_socket=None):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                client_socket.close()
                del clients[client_socket]

def handle_client(client_socket):
    try:
        # get username
        client_socket.send("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8').strip()
        welcome_message = f"{username} has joined the chat!"
        print(welcome_message)
        broadcast(welcome_message, client_socket)
        clients[client_socket] = username

        while True:
            msg = client_socket.recv(1024)
            if not msg:
                break
            msg = msg.decode('utf-8').strip()
            if msg.lower() == "exit":
                break
            full_msg = f"{username}: {msg}"
            print(full_msg)
            broadcast(full_msg, client_socket)
    except:
        pass
    finally:
        if client_socket in clients:
            left_msg = f"{clients[client_socket]} has left the chat."
            print(left_msg)
            broadcast(left_msg)
            del clients[client_socket]
        client_socket.close()

def start_server():
    print("[STARTING] Chat server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is running on {HOST}:{PORT}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[NEW CONNECTION] {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
