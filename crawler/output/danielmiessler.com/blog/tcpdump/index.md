<!-- Source: https://danielmiessler.com/blog/tcpdump -->

# A tcpdump Tutorial with Examples 
150 ways to isolate traffic for cybersecurity, network administration, and other technical roles
January 5, 2004
[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #tutorial](https://danielmiessler.com/archives/?tag=tutorial)[ #top](https://danielmiessler.com/archives/?tag=top)
 Infinite-fun-spacing…
16 reading now 
`tcpdump` is the world's premier network analysis tool—combining both power and simplicity into a single command-line interface. This guide will show you how to use it.
tcpdump is a powerful command-line packet analyzer. It allows you to capture and inspect network traffic in real-time. This tool is invaluable for network administrators, security professionals, and anyone who needs to understand network behavior.
In this tutorial, we'll explore 150 practical examples of using `tcpdump`. These examples will cover a wide range of use cases, from basic traffic capture to advanced filtering and analysis.
## Basic Syntax [​](https://danielmiessler.com/blog/tcpdump#basic-syntax)
The basic syntax of `tcpdump` is:
bash
```
tcpdump [options] [expression]
```

  * `options`: Modify the behavior of `tcpdump`, such as specifying the interface to capture on or the output format.
  * `expression`: Defines what kind of traffic to capture. This is where you specify hostnames, IP addresses, ports, protocols, and other criteria.


## Capturing Traffic on an Interface [​](https://danielmiessler.com/blog/tcpdump#capturing-traffic-on-an-interface)
To capture all traffic on a specific interface, use the `-i` flag followed by the interface name. For example, to capture traffic on the `eth0` interface:
bash
```
tcpdump -i eth0
```

To see a list of all available interfaces, use the command:
bash
```
tcpdump -D
```

## Capturing Traffic to/from a Specific Host [​](https://danielmiessler.com/blog/tcpdump#capturing-traffic-to-from-a-specific-host)
To capture traffic to or from a specific host, use the `host` keyword followed by the hostname or IP address:
bash
```
tcpdump host 192.168.1.100
```

This will capture all traffic to and from the host with the IP address `192.168.1.100`.
## Capturing Traffic on a Specific Port [​](https://danielmiessler.com/blog/tcpdump#capturing-traffic-on-a-specific-port)
To capture traffic on a specific port, use the `port` keyword followed by the port number:
bash
```
tcpdump port 80
```

This will capture all traffic on port 80 (HTTP).
## Combining Filters [​](https://danielmiessler.com/blog/tcpdump#combining-filters)
You can combine filters using `and`, `or`, and `not` operators. For example, to capture all traffic to or from host `192.168.1.100` on port 80, use:
bash
```
tcpdump host 192.168.1.100 and port 80
```

To capture traffic from `192.168.1.100` on either port 80 or 443, use:
bash
```
tcpdump src host 192.168.1.100 and \( port 80 or port 443 \)
```

## Advanced Filtering [​](https://danielmiessler.com/blog/tcpdump#advanced-filtering)
### Filtering by Protocol [​](https://danielmiessler.com/blog/tcpdump#filtering-by-protocol)
To filter by protocol, use the `ip`, `tcp`, `udp`, or other protocol keywords. For example, to capture only TCP traffic:
bash
```
tcpdump tcp
```

To capture only UDP traffic:
bash
```
tcpdump udp
```

### Filtering by Source or Destination [​](https://danielmiessler.com/blog/tcpdump#filtering-by-source-or-destination)
To filter by source or destination host or port, use the `src` or `dst` keywords:
bash
```
tcpdump src host 192.168.1.100
```

This will capture all traffic from the host `192.168.1.100`.
bash
```
tcpdump dst port 443
```

This will capture all traffic destined for port 443.
### Filtering by Network [​](https://danielmiessler.com/blog/tcpdump#filtering-by-network)
To capture traffic within a specific network, use the `net` keyword:
bash
```
tcpdump net 192.168.1.0/24
```

This will capture all traffic within the 192.168.1.0/24 network.
## Saving Captured Traffic to a File [​](https://danielmiessler.com/blog/tcpdump#saving-captured-traffic-to-a-file)
To save captured traffic to a file, use the `-w` flag followed by the filename:
bash
```
tcpdump -w capture.pcap -i eth0
```

This will save all captured traffic on the `eth0` interface to the file `capture.pcap`.
You can later analyze this file using `tcpdump` or another packet analyzer like Wireshark.
## Reading Captured Traffic from a File [​](https://danielmiessler.com/blog/tcpdump#reading-captured-traffic-from-a-file)
To read captured traffic from a file, use the `-r` flag followed by the filename:
bash
```
tcpdump -r capture.pcap
```

This will read and display the traffic from the file `capture.pcap`.
## Verbosity [​](https://danielmiessler.com/blog/tcpdump#verbosity)
You can control the verbosity of `tcpdump` output using the `-v`, `-vv`, or `-vvv` flags.
  * `-v`: Verbose output.
  * `-vv`: More verbose output.
  * `-vvv`: Most verbose output.


For example:
bash
```
tcpdump -vv -i eth0
```

## 150 tcpdump Examples [​](https://danielmiessler.com/blog/tcpdump#_150-tcpdump-examples)
Here are 150 `tcpdump` examples to help you isolate traffic in various situations:
### Basic Capture [​](https://danielmiessler.com/blog/tcpdump#basic-capture)
  1. **Capture all traffic on interface`eth0` :**
bash
```
tcpdump -i eth0
```

  2. **Capture all traffic on interface`wlan0` :**
bash
```
tcpdump -i wlan0
```

  3. **Capture all traffic on all interfaces:**
bash
```
tcpdump -i any
```

  4. **Capture only the first 100 packets:**
bash
```
tcpdump -c 100
```

  5. **List all available capture interfaces:**
bash
```
tcpdump -D
```



### Output Formatting [​](https://danielmiessler.com/blog/tcpdump#output-formatting)
  1. **Don't resolve hostnames:**
bash
```
tcpdump -n -i eth0
```

  2. **Don't resolve hostnames or port names:**
bash
```
tcpdump -nn -i eth0
```

  3. **Show packet contents in ASCII:**
bash
```
tcpdump -A -i eth0
```

  4. **Show packet contents in hex and ASCII:**
bash
```
tcpdump -X -i eth0
```

  5. **Show human-readable timestamps:**
bash
```
tcpdump -tttt -i eth0
```

  6. **Increase verbosity:**
bash
```
tcpdump -v -i eth0
```

  7. **Maximum verbosity:**
bash
```
tcpdump -vvv -i eth0
```

  8. **Capture full packets (no truncation):**
bash
```
tcpdump -s 0 -i eth0
```

  9. **Line-buffered output (useful for piping):**
bash
```
tcpdump -l -i eth0 | tee capture.txt
```



### Host Filters [​](https://danielmiessler.com/blog/tcpdump#host-filters)
  1. **Capture traffic to or from a specific IP:**
bash
```
tcpdump host 192.168.1.100
```

  2. **Capture traffic to or from a hostname:**
bash
```
tcpdump host example.com
```

  3. **Capture traffic from a specific source host:**
bash
```
tcpdump src host 192.168.1.100
```

  4. **Capture traffic to a specific destination host:**
bash
```
tcpdump dst host 192.168.1.100
```

  5. **Capture traffic between two specific hosts:**
bash
```
tcpdump host 192.168.1.100 and host 192.168.1.200
```



### Port Filters [​](https://danielmiessler.com/blog/tcpdump#port-filters)
  1. **Capture traffic on port 80 (HTTP):**
bash
```
tcpdump port 80
```

  2. **Capture traffic on port 443 (HTTPS):**
bash
```
tcpdump port 443
```

  3. **Capture traffic on port 22 (SSH):**
bash
```
tcpdump port 22
```

  4. **Capture traffic on port 53 (DNS):**
bash
```
tcpdump port 53
```

  5. **Capture traffic on port 25 (SMTP):**
bash
```
tcpdump port 25
```

  6. **Capture traffic on port 21 (FTP):**
bash
```
tcpdump port 21
```

  7. **Capture traffic from a specific source port:**
bash
```
tcpdump src port 80
```

  8. **Capture traffic to a specific destination port:**
bash
```
tcpdump dst port 443
```

  9. **Capture traffic on a range of ports:**
bash
```
tcpdump portrange 8000-9000
```



### Protocol Filters [​](https://danielmiessler.com/blog/tcpdump#protocol-filters)
  1. **Capture all TCP traffic:**
bash
```
tcpdump tcp
```

  2. **Capture all UDP traffic:**
bash
```
tcpdump udp
```

  3. **Capture all ICMP traffic:**
bash
```
tcpdump icmp
```

  4. **Capture all ARP traffic:**
bash
```
tcpdump arp
```

  5. **Capture all IPv6 traffic:**
bash
```
tcpdump ip6
```



### Network Filters [​](https://danielmiessler.com/blog/tcpdump#network-filters)
  1. **Capture traffic to or from a network:**
bash
```
tcpdump net 192.168.1.0/24
```

  2. **Capture traffic from a specific network:**
bash
```
tcpdump src net 192.168.1.0/24
```

  3. **Capture traffic to a specific network:**
bash
```
tcpdump dst net 192.168.1.0/24
```



### Combination Filters [​](https://danielmiessler.com/blog/tcpdump#combination-filters)
  1. **Capture traffic to a host on a specific port:**
bash
```
tcpdump dst host 192.168.1.100 and dst port 80
```

  2. **Capture traffic from a host on a specific port:**
bash
```
tcpdump src host 192.168.1.100 and src port 443
```

  3. **Capture traffic to or from a host on port 80 or 443:**
bash
```
tcpdump host 192.168.1.100 and \( port 80 or port 443 \)
```

  4. **Capture all traffic except ICMP:**
bash
```
tcpdump not icmp
```

  5. **Capture all traffic except SSH (port 22):**
bash
```
tcpdump not port 22
```

  6. **Exclude your own SSH session while capturing:**
bash
```
tcpdump -i eth0 not \( src host 192.168.1.50 and dst port 22 \)
```

  7. **Capture HTTP or HTTPS traffic:**
bash
```
tcpdump port 80 or port 443
```

  8. **Capture non-HTTP and non-HTTPS traffic:**
bash
```
tcpdump not port 80 and not port 443
```



### TCP Flag Filters [​](https://danielmiessler.com/blog/tcpdump#tcp-flag-filters)
  1. **Capture TCP SYN packets:**
bash
```
tcpdump 'tcp[tcpflags] & tcp-syn != 0'
```

  2. **Capture TCP ACK packets:**
bash
```
tcpdump 'tcp[tcpflags] & tcp-ack != 0'
```

  3. **Capture TCP RST packets:**
bash
```
tcpdump 'tcp[tcpflags] & tcp-rst != 0'
```

  4. **Capture TCP FIN packets:**
bash
```
tcpdump 'tcp[tcpflags] & tcp-fin != 0'
```

  5. **Capture TCP URG packets:**
bash
```
tcpdump 'tcp[tcpflags] & tcp-urg != 0'
```

  6. **Capture TCP PSH packets:**
bash
```
tcpdump 'tcp[tcpflags] & tcp-push != 0'
```

  7. **Capture SYN-only packets (new connection attempts):**
bash
```
tcpdump 'tcp[tcpflags] = tcp-syn'
```

  8. **Capture SYN/ACK packets (connection accepted):**
bash
```
tcpdump 'tcp[tcpflags] = 0x12'
```

  9. **Capture RST/ACK packets (connection refused or reset):**
bash
```
tcpdump 'tcp[tcpflags] = 0x14'
```

  10. **Capture FIN/ACK packets (connection closing):**
bash
```
tcpdump 'tcp[tcpflags] = 0x11'
```

  11. **Capture PSH/ACK packets (data transfer):**
bash
```
tcpdump 'tcp[tcpflags] = 0x18'
```

  12. **Capture null scan packets (no flags set):**
bash
```
tcpdump 'tcp[tcpflags] = 0x00'
```

  13. **Capture Xmas tree scan packets (FIN+PSH+URG):**
bash
```
tcpdump 'tcp[tcpflags] & 0x29 = 0x29'
```



### Saving and Reading Captures [​](https://danielmiessler.com/blog/tcpdump#saving-and-reading-captures)
  1. **Write captured traffic to a file:**
bash
```
tcpdump -w capture.pcap -i eth0
```

  2. **Read captured traffic from a file:**
bash
```
tcpdump -r capture.pcap
```

  3. **Read from a file with a filter applied:**
bash
```
tcpdump -r capture.pcap tcp port 80
```

  4. **Rotate capture files every 100MB:**
bash
```
tcpdump -w capture.pcap -C 100 -i eth0
```

  5. **Rotate capture files every hour:**
bash
```
tcpdump -w capture-%Y%m%d%H%M%S.pcap -G 3600 -i eth0
```

  6. **Keep only the last 10 rotated capture files:**
bash
```
tcpdump -w capture.pcap -C 100 -W 10 -i eth0
```



### IP Header Filters [​](https://danielmiessler.com/blog/tcpdump#ip-header-filters)
  1. **Capture IP fragments:**
bash
```
tcpdump 'ip[6:2] & 0x1fff != 0'
```

  2. **Capture packets with TTL of 128 (typical Windows default):**
bash
```
tcpdump 'ip[8] = 128'
```

  3. **Capture packets with TTL of 64 (typical Linux default):**
bash
```
tcpdump 'ip[8] = 64'
```

  4. **Capture packets with DSCP value EF (46):**
bash
```
tcpdump 'ip[1] & 0xfc = 0xb8'
```

  5. **Capture packets with ECN Congestion Experienced:**
bash
```
tcpdump 'ip[1] & 0x03 = 3'
```

  6. **Capture packets larger than 500 bytes:**
bash
```
tcpdump greater 500
```

  7. **Capture packets smaller than 100 bytes:**
bash
```
tcpdump less 100
```



### Payload and Content Inspection [​](https://danielmiessler.com/blog/tcpdump#payload-and-content-inspection)
  1. **Capture HTTP GET requests:**
bash
```
tcpdump -s 0 -A 'tcp dst port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'
```

  2. **Capture HTTP POST requests:**
bash
```
tcpdump -s 0 -A 'tcp dst port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354'
```

  3. **Capture DNS query traffic:**
bash
```
tcpdump -n 'udp dst port 53'
```

  4. **Capture DHCP discover and request packets:**
bash
```
tcpdump -n 'udp port 67 or udp port 68'
```

  5. **Capture TLS Client Hello packets (new HTTPS connections):**
bash
```
tcpdump 'tcp port 443 and tcp[((tcp[12:1] & 0xf0) >> 2)] = 0x16 and tcp[((tcp[12:1] & 0xf0) >> 2)+5] = 0x01'
```



### Security Engineer Use Cases [​](https://danielmiessler.com/blog/tcpdump#security-engineer-use-cases)
  1. **Capture cleartext FTP credentials:**
bash
```
tcpdump -nn -A -i eth0 'port 21'
```

  2. **Capture HTTP Basic Authentication headers:**
bash
```
tcpdump -nn -A -s 0 -i eth0 'tcp dst port 80'
```

  3. **Capture cleartext SMTP authentication:**
bash
```
tcpdump -nn -A -i eth0 'tcp port 25 or tcp port 587'
```

  4. **Capture cleartext POP3/IMAP credentials:**
bash
```
tcpdump -nn -A -i eth0 'tcp port 110 or tcp port 143'
```

  5. **Detect ARP spoofing (excessive ARP replies):**
bash
```
tcpdump -nn -e -i eth0 'arp[6:2] = 2'
```

  6. **Identify DNS exfiltration (unusually large DNS packets):**
bash
```
tcpdump -nn -i eth0 'udp port 53 and greater 512'
```

  7. **Detect DNS tunnel responses (oversized replies):**
bash
```
tcpdump -nn -i eth0 'udp src port 53 and greater 300'
```

  8. **Detect rogue DHCP servers:**
bash
```
tcpdump -nn -e -i eth0 'udp src port 67'
```

  9. **Detect brute force attacks on authentication services:**
bash
```
tcpdump -nn -i eth0 'tcp[tcpflags] = tcp-syn and (dst port 22 or dst port 3389 or dst port 445)'
```

  10. **Capture SSH connection attempts with timestamps:**
bash
```
tcpdump -nn -tttt -i eth0 'tcp dst port 22 and tcp[tcpflags] = tcp-syn' -c 200
```

  11. **Capture LDAP authentication traffic:**
bash
```
tcpdump -nn -A -i eth0 'tcp port 389 or tcp port 636'
```

  12. **Capture Kerberos authentication traffic:**
bash
```
tcpdump -nn -i eth0 'tcp port 88 or udp port 88'
```

  13. **Detect cleartext Telnet sessions:**
bash
```
tcpdump -nn -A -i eth0 'tcp port 23'
```

  14. **Capture TLS handshake records for certificate analysis:**
bash
```
tcpdump -nn -s 0 -w tls-handshakes.pcap -i eth0 'tcp port 443 and (tcp[((tcp[12:1] & 0xf0) >> 2)] = 0x16)'
```

  15. **Spot VLAN tagging anomalies:**
bash
```
tcpdump -nn -e -i eth0 'vlan'
```

  16. **Monitor outbound connections to non-standard ports:**
bash
```
tcpdump -nn -i eth0 'tcp[tcpflags] = tcp-syn and dst portrange 1-1023 and not (dst port 80 or dst port 443 or dst port 22 or dst port 53 or dst port 25)'
```

  17. **Detect unauthorized external DNS usage:**
bash
```
tcpdump -nn -i eth0 'udp dst port 53 and not dst host 10.0.0.1'
```

  18. **Detect lateral movement via SMB:**
bash
```
tcpdump -nn -i eth0 'tcp dst port 445 and src net 10.0.0.0/8 and dst net 10.0.0.0/8'
```

  19. **Detect lateral movement via WinRM:**
bash
```
tcpdump -nn -i eth0 'tcp dst port 5985 or tcp dst port 5986'
```

  20. **Detect lateral movement via RDP between internal hosts:**
bash
```
tcpdump -nn -i eth0 'tcp dst port 3389 and src net 192.168.0.0/16 and dst net 192.168.0.0/16'
```



### Security Red Team / Blue Team Operations [​](https://danielmiessler.com/blog/tcpdump#security-red-team-blue-team-operations)
  1. **Detect outbound reverse shell connections:**
bash
```
tcpdump -nn -i eth0 'tcp[tcpflags] = tcp-syn and (dst port 4444 or dst port 1234 or dst port 5555 or dst port 9001)'
```

  2. **Find C2 beaconing patterns (periodic HTTPS connections):**
bash
```
tcpdump -nn -tttt -i eth0 'tcp dst port 443 and tcp[tcpflags] = tcp-syn' -c 500
```

  3. **Detect ICMP tunneling (oversized ping packets):**
bash
```
tcpdump -nn -i eth0 'icmp and greater 100'
```

  4. **Detect DNS over HTTPS (DoH) bypassing corporate DNS:**
bash
```
tcpdump -nn -i eth0 'tcp dst port 443 and (dst host 1.1.1.1 or dst host 8.8.8.8 or dst host 8.8.4.4 or dst host 9.9.9.9)'
```

  5. **Find unauthorized OpenVPN tunnels:**
bash
```
tcpdump -nn -i eth0 'udp port 1194 or tcp port 1194'
```

  6. **Find unauthorized WireGuard tunnels:**
bash
```
tcpdump -nn -i eth0 'udp port 51820'
```

  7. **Detect cryptocurrency mining traffic (Stratum protocol):**
bash
```
tcpdump -nn -i eth0 'tcp dst port 3333 or tcp dst port 8333 or tcp dst port 9999'
```

  8. **Monitor for NTLM credential theft over SMB:**
bash
```
tcpdump -nn -s 0 -w ntlm-traffic.pcap -i eth0 'tcp port 445 or tcp port 139'
```

  9. **Detect data exfiltration (large outbound packets):**
bash
```
tcpdump -nn -i eth0 'src net 10.0.0.0/8 and not dst net 10.0.0.0/8 and greater 1000'
```

  10. **Monitor for unauthorized SOCKS proxy usage:**
bash
```
tcpdump -nn -i eth0 'tcp dst port 1080'
```

  11. **Detect ICMP ping sweep (host enumeration):**
bash
```
tcpdump -nn -i eth0 'icmp[0] = 8' -c 500
```

  12. **Detect C2 traffic to a specific suspected host:**
bash
```
tcpdump -nn -tttt -i eth0 'tcp dst port 443 and tcp[tcpflags] = tcp-syn and dst host 192.0.2.100'
```

  13. **Monitor for LDAP enumeration (Active Directory recon):**
bash
```
tcpdump -nn -i eth0 'tcp dst port 389' -c 1000
```

  14. **Detect PowerShell remoting via WinRM:**
bash
```
tcpdump -nn -A -s 0 -i eth0 'tcp dst port 5985'
```

  15. **Capture DNS traffic for C2 frequency analysis:**
bash
```
tcpdump -nn -i eth0 'udp port 53' -c 5000 -w dns-baseline.pcap
```

  16. **Detect HTTP tunneling (non-browser traffic):**
bash
```
tcpdump -nn -A -s 0 -i eth0 'tcp dst port 80 and src host 10.0.1.50'
```

  17. **Hunt for exfiltration via ICMP payload data:**
bash
```
tcpdump -nn -X -i eth0 'icmp[0] = 8 and greater 64'
```

  18. **Detect port knocking sequences:**
bash
```
tcpdump -nn -tttt -i eth0 'tcp[tcpflags] = tcp-syn and dst host 10.0.1.100'
```

  19. **Monitor for DNS rebinding attack responses:**
bash
```
tcpdump -nn -v -i eth0 'udp src port 53' -c 200
```

  20. **Capture covert channel traffic over permitted DNS:**
bash
```
tcpdump -nn -i eth0 'udp dst port 53 and src host 10.0.1.50' -c 1000
```



### Security Incident Response Team Operations [​](https://danielmiessler.com/blog/tcpdump#security-incident-response-team-operations)
  1. **Full packet capture from a compromised host:**
bash
```
tcpdump -nn -s 0 -w evidence-$(date +%Y%m%d-%H%M%S).pcap -i eth0 'host 10.0.1.50'
```

  2. **Time-windowed capture for incident timeline:**
bash
```
tcpdump -nn -s 0 -G 300 -w incident-%Y%m%d-%H%M%S.pcap -i eth0 'host 10.0.1.50'
```

  3. **Quick-triage packet capture with count limit:**
bash
```
tcpdump -nn -s 0 -c 10000 -w triage.pcap -i eth0 'host 10.0.1.50'
```

  4. **Capture HTTP response payloads for malware analysis:**
bash
```
tcpdump -nn -s 0 -A -i eth0 'tcp src port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
```

  5. **Log all DNS queries for IOC matching:**
bash
```
tcpdump -nn -i eth0 'udp dst port 53' -l | tee dns-queries.log
```

  6. **Capture traffic to known malicious IPs:**
bash
```
tcpdump -nn -s 0 -w malicious.pcap -i eth0 'host 203.0.113.10 or host 198.51.100.20 or host 192.0.2.30'
```

  7. **Capture only new TCP connections during an incident:**
bash
```
tcpdump -nn -tttt -i eth0 'tcp[tcpflags] = tcp-syn'
```

  8. **Long-running evidence capture with size rotation:**
bash
```
tcpdump -nn -s 0 -C 100 -W 50 -w evidence.pcap -i eth0 'host 10.0.1.50'
```

  9. **Capture ICMP error messages during an incident:**
bash
```
tcpdump -nn -v -i eth0 'icmp[0] = 3 or icmp[0] = 11'
```

  10. **Monitor for data exfiltration over email:**
bash
```
tcpdump -nn -A -s 0 -i eth0 'tcp dst port 25 or tcp dst port 587 or tcp dst port 465'
```

  11. **Ring-fence a compromised subnet:**
bash
```
tcpdump -nn -s 0 -w subnet-capture.pcap -i eth0 'net 10.0.1.0/24'
```

  12. **Detect internal scanning from a compromised host:**
bash
```
tcpdump -nn -i eth0 'tcp[tcpflags] = tcp-syn and src host 10.0.1.50 and dst net 10.0.0.0/8'
```

  13. **Capture evidence of internal data staging:**
bash
```
tcpdump -nn -i eth0 'src host 10.0.1.50 and dst net 10.0.0.0/8 and greater 1000'
```

  14. **Time-limited capture for legal evidence hold:**
bash
```
timeout 3600 tcpdump -nn -s 0 -w legal-hold-$(date +%Y%m%d).pcap -i eth0 'host 10.0.1.50'
```

  15. **Capture outbound traffic excluding known-good destinations:**
bash
```
tcpdump -nn -i eth0 'src net 10.0.0.0/8 and not dst net 10.0.0.0/8 and not (dst port 80 or dst port 443 or dst port 53)'
```



### Network Engineer / SysAdmin Use Cases [​](https://danielmiessler.com/blog/tcpdump#network-engineer-sysadmin-use-cases)
  1. **Monitor TCP zero window events (flow control problems):**
bash
```
tcpdump -nn -i eth0 'tcp[14:2] = 0 and tcp[tcpflags] & tcp-ack != 0'
```

  2. **Detect ICMP "need to fragment" messages (MTU issues):**
bash
```
tcpdump -nn -v -i eth0 'icmp[0] = 3 and icmp[1] = 4'
```

  3. **Capture packets with Don't Fragment bit set:**
bash
```
tcpdump -nn -i eth0 'ip[6] & 0x40 != 0'
```

  4. **Monitor BGP sessions:**
bash
```
tcpdump -nn -i eth0 'tcp port 179'
```

  5. **Check NTP synchronization traffic:**
bash
```
tcpdump -nn -i eth0 'udp port 123'
```

  6. **Debug DHCP lease problems (full handshake):**
bash
```
tcpdump -nn -e -vv -i eth0 'udp port 67 or udp port 68'
```

  7. **Monitor VRRP failover traffic:**
bash
```
tcpdump -nn -i eth0 'ip proto 112'
```

  8. **Monitor HSRP failover traffic:**
bash
```
tcpdump -nn -i eth0 'udp dst port 1985'
```

  9. **Capture SNMP trap notifications:**
bash
```
tcpdump -nn -i eth0 'udp port 162'
```

  10. **Detect duplicate IP addresses via ARP:**
bash
```
tcpdump -nn -e -i eth0 'arp'
```

  11. **Troubleshoot DNS resolution failures:**
bash
```
tcpdump -nn -v -i eth0 'udp port 53'
```

  12. **Capture SIP/VoIP signaling traffic:**
bash
```
tcpdump -nn -A -s 0 -i eth0 'tcp port 5060 or udp port 5060'
```

  13. **Capture RTP voice/video streams:**
bash
```
tcpdump -nn -i eth0 'udp portrange 16384-32767'
```

  14. **Monitor RADIUS authentication:**
bash
```
tcpdump -nn -i eth0 'udp port 1812 or udp port 1813'
```

  15. **Monitor TACACS+ authentication:**
bash
```
tcpdump -nn -i eth0 'tcp port 49'
```

  16. **Check GRE tunnel traffic:**
bash
```
tcpdump -nn -i eth0 'ip proto 47'
```

  17. **Debug OSPF neighbor issues:**
bash
```
tcpdump -nn -i eth0 'ip proto 89'
```

  18. **Monitor EIGRP routing updates:**
bash
```
tcpdump -nn -i eth0 'ip proto 88'
```

  19. **Capture multicast traffic:**
bash
```
tcpdump -nn -i eth0 'dst net 224.0.0.0/4'
```

  20. **Verify QoS/DSCP markings on traffic:**
bash
```
tcpdump -nn -v -i eth0 'ip[1] & 0xfc != 0'
```



These examples should provide a solid foundation for using `tcpdump` to analyze network traffic.
Happy hunting!
_-Daniel_
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Ftcpdump&title=A%20tcpdump%20Tutorial%20with%20Examples%20 "Share on Hacker News")
Follow
## supporting = loving
For 29.5583 years I've been creating ad-free technical tutorials and essays here. 3.047 pieces and counting. 
It's a one-person effort that's also my livelihood. If it makes your day easier or more pleasant in any way, please consider supporting the work with a monthly or one-time donation. 
It helps me make more content, and is deeply appreciated as well. 🫶🏼 
### Monthly Support
[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)
### One-Time Support
[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)
Search
This post was tagged with:
cybersecuritytechnologytutorialtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
