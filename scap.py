from scapy.all import ip,icmp,srl

target_ip = "www.google.com"
packet = ip(dst=target_ip) / icmp()
response = srl(packet, timeout=2, verbose=False)

if response:
    print(f"revecived response from {response.src}")

else:
    print("no response received")