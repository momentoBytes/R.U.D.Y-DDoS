# R.U.D.Y-DDoS
RUDY Tool Overview

RUDY (R-U-Dead-Yet) is a powerful and customizable stress-testing tool designed to send multiple HTTP requests to a target server, often used for penetration testing, stress testing, or educational purposes in ethical hacking. The primary focus of this tool is to simulate traffic to test the target server's resilience under high load conditions.

This customized version of the RUDY tool has been enhanced with additional features and improvements to make it more user-friendly and effective, particularly for Termux users.


---

Features of the RUDY Tool

1. Proxy Support with Tor:

The tool uses the Tor network to anonymize traffic.

Proxies are configured through SOCKS5 for secure and private testing.



2. Multi-threaded Requests:

Supports multi-threading to send a large number of requests simultaneously.

Customizable thread count for tailored performance.



3. Interactive User Input:

Accepts target IP/URL and port directly from the user.

Clear prompts to guide the user through the setup process.

# Installation 

### Step 1: Update Termux
```bash
pkg update && pkg upgrade

```
### Step 2: Install Python and Dependencies

Install Python and the required libraries for the script.

```

pkg install python  
pkg install python3  
pip install requests stem pysocks

```
### Step 3: Install Tor

Install the Tor service to route traffic through the SOCKS5 proxy.
```
pkg install tor
```
### Step 4: Start Tor Service

Run the Tor service and keep it active in the background.

```
tor
```
### Step 5: Download the Script

Clone the repository from GitHub or save the script locally.

```

git clone https://github.com/momentoBytes/R.U.D.Y-DDoS

```
### Step 6: Step 6: Run the Script

Execute the script using Python.

```
python3 R.U.D.Y-DDoS.py
```
The script will prompt you to input the target IP/URL and port number.




