import socket
import ssl
import threading
import sys
import handle_req

# sudo python3 server.py localhost 443 cert.pem key.pem

# Function to handle incoming connections
def handler(conn, cert_path, key_path, port, address):
    try:
        # Checking the port and setting up SSL if necessary
        if port == 443 and cert_path and key_path:
            # context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.verify_mode=ssl.CERT_NONE
            context.load_cert_chain(cert_path, key_path)
            s_conn = context.wrap_socket(conn, server_side=True)
        elif port == 80:
            s_conn = conn
        else:
            raise Exception("Invalid port")

        # Receiving the request and handling it
        request = s_conn.recv(1024).decode('utf-8')
        print("Started request handler...")
        response = handle_req.requestHandler(request, address)
        s_conn.sendall(response)
        s_conn.close()

    except Exception as e:
        print(f"Error: {e}")
        conn.close()

def main():
    # Checking command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python3 server.py <ip_address> <port> [cert_path] [key_path]")
        sys.exit(1)

    ip_address = sys.argv[1]
    port = int(sys.argv[2])
    cert_path = sys.argv[3] if len(sys.argv) > 3 else None
    key_path = sys.argv[4] if len(sys.argv) > 4 else None

    # Handling certificate and key paths
    if cert_path and not key_path:
        print("Private key path provided without certificate path. Please provide both or none.")
        sys.exit(1)

    print(f"Server listening on {ip_address} port {port}")

    # Setting up the socket and starting to listen
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((ip_address, port))
    srv.listen(5)
    print("Listening..." )

    # Handling incoming connections in a loop using threading
    while True:
        connection, address = srv.accept()
        t = threading.Thread(target=handler, args=(connection, cert_path, key_path, port, address))
        t.start()

if __name__ == "__main__":
    main()
