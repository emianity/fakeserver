import socket

def start_server(host='0.0.0.0', port=2222):
    # 创建一个TCP/IP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定套接字到主机和端口
    server_socket.bind((host, port))
    
    # 监听传入的连接
    server_socket.listen(1)
    
    print(f"Server started on {host}:{port}. Waiting for connections...")
    
    while True:
        # 接受连接
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # 发送确认信息
        client_socket.sendall(b"Connection established successfully!")
        
        # 关闭连接
        client_socket.close()

if __name__ == "__main__":
    start_server()
