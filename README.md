Scapy TCP → HTTP GET Script

A small, educational Python script that demonstrates how to manually perform a TCP three-way handshake with a target host and send a raw HTTP GET request using Scapy.
This is useful for learning how TCP and HTTP work at the packet level, debugging low-level network behavior, and for controlled network testing.
Important — Read Before Running

Use only on systems and networks you own or are explicitly authorized to test.

Running raw packet code typically requires administrator/root privileges.

Misuse can be considered malicious activity (scanning, spoofing, or DoS). Always follow applicable laws and your organization’s policies.

Features

Performs a manual TCP three-way handshake (SYN → SYN-ACK → ACK).

Sends a manually crafted HTTP GET payload using a TCP packet with PSH+ACK.

Receives and prints the server response (packet summary and raw HTTP body if present).

Simple, minimal footprint — great for learning and demonstrations.

Requirements

Python 3.x

Scapy

Install Scapy with pip:

pip install scapy

How it works (step-by-step)

SYN — the script sends a TCP SYN to the target IP:port to request a connection.

SYN-ACK — waits for the server’s SYN-ACK using sr1().

ACK — sends a plain ACK to complete the three-way handshake.

HTTP GET — crafts a PSH+ACK TCP packet containing an HTTP request (plain text) and sends it; waits for a response.

Display — prints Scapy’s packet summary and the raw HTTP payload if present.
Usage

Edit target_ip and target_port variables to point at the server you are authorized to test.

Run as root/administrator:

Received HTTP Response:
###[ IP ]###
  version   = 4
  src       = 192.168.0.103
  dst       = 192.168.0.105
###[ TCP ]###
  sport     = 80
  dport     = 51932
  flags     = PA
###[ Raw ]###
  load      = b'HTTP/1.1 200 OK\r\nServer: nginx\r\n...\r\n\r\n<html>...</html>'
<html>...</html>
Troubleshooting

No response received

Ensure the target host is up and listening on the specified port.

Confirm network routing/firewall rules allow your packets.

If the server employs protections (SYN cookies, connection limits, or requires TLS), it may not respond to raw HTTP GET over plaintext TCP.

sr1() hangs or times out

Increase the timeout argument, or confirm the target is reachable.

Use sr() with timeout and retry options for more control.

Permission errors

Run the script with sudo/Administrator privileges — raw sockets require elevated access.

Fragmented or missing Raw payload

HTTP responses may be split across multiple packets. sr1() receives only the first matching packet. Consider using sr() to capture multiple responses or use a sniffing approach (e.g., sniff() with a filter) to assemble the full payload.

Server uses TLS (HTTPS)

Plaintext HTTP requests to port 443 or HTTPS endpoints will not return valid responses. Use a TLS-capable tool or library instead.

Improvements & Extensions

Use proper sequence and acknowledgement tracking (manage seq/ack correctly across multiple packets).

Collect multiple response packets (sr() or sniff()) and reassemble TCP stream to handle larger responses.

Add randomized source ports and delays for more realistic client behavior (only for benign testing).

Add support for HTTP headers (User-Agent, Accept, Connection) and HTTP/1.1 Connection: close to encourage the server to close the connection after response.

Use Scapy’s TCP() sport parameter to set a client-side source port and track seq values you set yourself.

Security & Ethics

This script should be used for educational and authorized testing only. Unauthorized scanning or probing of networks you don’t own may be illegal and harmful. Always obtain written permission before testing systems you do not control.

License

You can add an open-source license to your repository. A minimal MIT license is common for small scripts:

MIT License

Copyright (c) YEAR Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
...


On some platforms you may need additional system packages (libpcap, WinPcap/Npcap on Windows). Run the script as root/administrator.
