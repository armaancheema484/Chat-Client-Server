import socket
import threading
import sys

SERVER_HOST = '127.0.0.1'  # change if connecting to a remote server
SERVER_PORT = 5555

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if msg:
                print(msg)
            else:
                print("[Disconnected from server]")
                break
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
    except:
        print("Unable to connect to the server.")
        return

    # start background thread to receive messages
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            client_socket.send("exit".encode('utf-8'))
            break
        try:
            client_socket.send(msg.encode('utf-8'))
        except:
            print("[Error sending message]")
            break

    client_socket.close()
    print("Disconnected from chat.")

if __name__ == "__main__":
    start_client()
