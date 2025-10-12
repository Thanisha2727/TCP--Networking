from scapy.all import *

target_ip = "192.168.0.103"
target_port = 80


ip = IP(dst=target_ip)
syn = TCP(dport=target_port, flags="S")
syn_ack = sr1(ip/syn)


ack = TCP(dport=target_port, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
send(ip/ack)


payload = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip)
push = TCP(dport=target_port, flags="PA", seq=syn_ack.ack, ack=syn_ack.seq + 1)
http_response = sr1(ip/push/payload, timeout=5)  


if http_response:
    print("Received HTTP Response:")
    print(http_response.show())

    if http_response.haslayer(Raw):
        print(http_response[Raw].load.decode(errors="ignore"))  # Print HTTP content
    else:
        print("No Raw payload found. The response might be an empty ACK or fragmented.")
else:
    print("No response received from the server.")
