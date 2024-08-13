import psutil
import socket

# 获取所有网络接口的地址信息
addrs = psutil.net_if_addrs()

# 存储所有绑定的 IP 地址
ip_addresses = set()

for interface, addr_info in addrs.items():
    for addr in addr_info:
        if addr.family == socket.AF_INET:  # 只考虑IPv4地址
            ip_addresses.add(addr.address)

print("All IP addresses bound to the server:")
for ip in ip_addresses:
    print(ip)

