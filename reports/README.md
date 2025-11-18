# 🛡️ Automated Network Scanner & Reporting Tool

This project provides an automated solution for local network vulnerability assessment using **Bash Scripting** and **Python 3**. It streamlines the process from aggressive Nmap scanning to generating analyst-ready reports.

## 🚀 Key Features

* **Automation:** Single Bash script execution (`scanner.sh`) handles the full workflow.
* **Deep Scanning:** Uses aggressive Nmap flags (`-A`, `-v`, `-sV`, `-sC`) for service version detection and script scanning.
* **Reporting:** Generates raw Nmap XML files, clean text summaries, and detailed, browser-viewable /home/kali/network-scanner-project/assets/html_report.png.

## 💻 Execution Command

To run the full scan and reporting process on a target subnet (e.g., your VM network):

```bash
sudo ./scripts/scanner.sh 172.20.10.0/28
--- Automated Nmap Vulnerability Summary ---
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
Scan Run Date: 2025-11-18 04:29:10

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
Scan Run Date: 2025-11-18 09:07:01

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
Scan Run Date: 2025-11-18 09:10:52

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
... [rest of the combined summary content] ...
