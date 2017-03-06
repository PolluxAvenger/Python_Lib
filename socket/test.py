
import socket
import struct

source_ip = '192.168.1.101'
dest_ip = '192.168.1.1'  # or socket.gethostbyname('www.google.com')

# ip header fields
ip_ihl = 5
ip_ver = 4
ip_tos = 0
ip_tot_len = 0  # kernel will fill the correct total length
ip_id = 54321  # Id of this packet
ip_frag_off = 0
ip_ttl = 255
ip_proto = socket.IPPROTO_TCP
ip_check = 0  # kernel will fill the correct checksum
ip_saddr = socket.inet_aton(source_ip)  # Spoof the source ip address if you want to
ip_daddr = socket.inet_aton(dest_ip)

ip_ihl_ver = (version << 4) + ihl

# the ! in the pack format string means network order
ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                 ip_saddr, ip_daddr)