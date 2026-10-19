from scapy.all import rdpcap, IP, TCP, UDP, ICMP
import time

filename = r"D:\wireshark\http-download20000-c_00000_20160112035146.pcapng"
packets = rdpcap(filename)

total_packets = len(packets)
print(f"Total packets: {total_packets}")

count = 1
protocol_counts = {}
source_ip_count = {}
destination_ip_count = {}

for packet in packets:
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if src_ip in source_ip_count:
            source_ip_count[src_ip] = source_ip_count[src_ip] + 1
        else:
            source_ip_count[src_ip] = 1

        if dst_ip in destination_ip_count:
            destination_ip_count[dst_ip] = destination_ip_count[dst_ip] + 1
        else:
            destination_ip_count[dst_ip] = 1

        pkt_time = time.ctime(float(packet.time))

        # Check the protocol
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "Other"

        if protocol in protocol_counts:
            protocol_counts[protocol] = protocol_counts[protocol] + 1
        else:
            protocol_counts[protocol] = 1

        packet_length = len(packet)

        # Print packet details
        print(
            f"Time: {pkt_time} | Packet: {count} | "
            f"Source IP: {src_ip} | Destination IP: {dst_ip} | "
            f"Protocol: {protocol} | Length: {packet_length} bytes"
        )

    else:
        print(f"Packet: {count} | No IP layer")

    count = count + 1

# Final protocol report
print("\n--- Final Protocol Tally ---")
for protocol_name, total in protocol_counts.items():
    print(f"{protocol_name}: {total}")

# Source IP report
print("\n--- Top Source IPs ---")
sorted_source_ips = sorted(
    source_ip_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for ip, total in sorted_source_ips:
    print(f"{ip}: {total}")

# Destination IP report
print("\n--- Top Destination IPs ---")
sorted_destination_ips = sorted(
    destination_ip_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for ip, total in sorted_destination_ips:
    print(f"{ip}: {total}")
