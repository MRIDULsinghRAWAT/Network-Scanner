reports."
Networking,ip a / DHCP,Confirmed network configuration (172.20.10.3/28) and host discovery on the subnet.3. Key Findings>
172.20.10.1,UP,"21, 53, 49152, 62078","Port 53 (DNS) showed an unrecognized service, and ports 21, 49152, and 62078 were>
20.10.2,UP,None Found,"All 1000 ports were filtered (no-response)
# 🛡️ Automated Network Scanner & Reporting Tool

This project provides an automated solution for local network vulnerability assessment using **Bash Scripting** and **Python 3**. It customizes the process from aggressive Nmap scanning to generating analyst-ready reports.

## 🚀 Key Features

* **Automation:** A single Bash script (`scanner.sh`) handles host discovery, Nmap execution, and file management.
* **Deep Scanning:** Uses aggressive Nmap flags (`-A`, `-v`, `-sV`, `-sC`) for service version detection and vulnerability scripting.
* **Reporting:** Generates raw Nmap XML files, clean text summaries, and detailed, browser-viewable **=================================================
Starting Automated Vulnerability Scan on 172.20.10.0/28...
=================================================
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-11-18 09:09 EST
Nmap scan report for 172.20.10.1
Host is up (0.017s latency).
Not shown: 996 closed tcp ports (reset)
PORT      STATE SERVICE    VERSION
21/tcp    open  tcpwrapped
53/tcp    open  domain     (generic dns response: NOTIMP)
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|     bind
|     root-servers
|     nstld
|_    verisign-grs
49152/tcp open  tcpwrapped
62078/tcp open  tcpwrapped
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.94SVN%I=7%D=11/18%Time=691C7E38%P=x86_64-pc-linux-gnu%r(
SF:DNSVersionBindReqTCP,6B,"\0i\0\x06\x81\x83\0\x01\0\0\0\x01\0\0\x07versi
SF:on\x04bind\0\0\x10\0\x01\0\0\x06\0\x01\0\0\x0e\x10\0@\x01a\x0croot-serv
SF:ers\x03net\0\x05nstld\x0cverisign-grs\x03com\0x\xb4\xc0\xf8\0\0\x07\x08
SF:\0\0\x03\x84\0\t:\x80\0\x01Q\x80")%r(DNSStatusRequestTCP,E,"\0\x0c\0\0\
SF:x90\x04\0\0\0\0\0\0\0\0");
MAC Address: 2A:2D:7F:16:9A:64 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=11/18%OT=53%CT=1%CU=41676%PV=Y%DS=1%DC=D%G=Y%M=2A2D
OS:7F%TM=691C7E6A%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10D%TI=Z%CI=RI
OS:%II=RI%TS=21)OPS(O1=M4ECNW6NNT11SLL%O2=M4ECNW6NNT11SLL%O3=M4ECNW6NNT11%O
OS:4=M4ECNW6NNT11SLL%O5=M4ECNW6NNT11SLL%O6=M4ECNNT11SLL)WIN(W1=FFFF%W2=FFFF
OS:%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)ECN(R=Y%DF=N%T=40%W=FFFF%O=M4ECNW6SLL%C
OS:C=Y%Q=)T1(R=Y%DF=N%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=N%
OS:T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=N%T=40%W=0%S=Z%A=S+%F=AR%O=%RD
OS:=0%Q=)T6(R=Y%DF=N%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=4
OS:0%IPL=38%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=0%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop

TRACEROUTE
HOP RTT      ADDRESS
1   16.78 ms 172.20.10.1

Nmap scan report for 172.20.10.2
Host is up (0.00089s latency).
All 1000 scanned ports on 172.20.10.2 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)
MAC Address: 38:D5:7A:D1:BB:A7 (Cloud Network Technology Singapore PTE.)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.89 ms 172.20.10.2

Nmap scan report for 172.20.10.3
Host is up (0.000090s latency).
All 1000 scanned ports on 172.20.10.3 are in ignored states.
Not shown: 1000 closed tcp ports (reset)
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 16 IP addresses (3 hosts up) scanned in 73.84 seconds

--- Generating Detailed HTML Report ---
HTML Report saved: /home/kali/network-scanner-project/reports/report-172.20.10.0_28-2025-11-18_09:09:38.html

--- Generating Clean Text Summary ---

Writing clean summary to /home/kali/network-scanner-project/reports/summary-172.20.10.0_28-2025-11-18_09:09:38.txt...
Summary generated successfully: /home/kali/network-scanner-project/reports/summary-172.20.10.0_28-2025-11-18_09:09:38.txt
=================================================
PROCESS COMPLETE: Check the 'reports/' folder.
=================================================
** (the primary deliverable).

---

## 💻 Execution Command

To run the full scan and reporting process on a target subnet (replace the CIDR with your target):

```bash
sudo ./scripts/scanner.sh 172.20.10.0/28
// /home/kali/network-scanner-project/assets/html_report.png //
Scan Run Date: 2025-11-18 03:31:37

=================================================
HOST: 172.20.10.1 | Status: UP
=================================================
OPEN PORTS FOUND:
  - 21/tcp (tcpwrapped) | Version: N/A
  - 53/tcp (domain) | Version: N/A
  - 49152/tcp (tcpwrapped) | Version: N/A
  - 62078/tcp (tcpwrapped) | Version: N/A

=================================================
HOST: 172.20.10.2 | Status: UP
=================================================
No open ports found.

=================================================
HOST: 172.20.10.3 | Status: UP
=================================================
No open ports found.

--- Automated Nmap Vulnerability Summary ---
Scan Run Date: 2025-11-18 03:46:05

=================================================
HOST: 172.20.10.1 | Status: UP
