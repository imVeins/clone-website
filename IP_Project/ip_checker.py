import os
import platform
from datetime import datetime

INPUT_FILE = "C:/Users/write/IP_Project/ips.txt"
OUTPUT_FILE = "C:/Users/write/IP_Project/inactive_ips.txt"

def ping(ip):
    system_name = platform.system().lower()

    if system_name == "windows":
       
        command = f"ping -n 1 -w 500 {ip} > nul"
    else:
        
        command = f"ping -c 1 -W 1 {ip} > /dev/null"

    return os.system(command) == 0

def main():
    inactive_ips = []

    print("IP STATUS CHECK")
    print("Time:", datetime.now())
    print("-" * 40)

    try:
        with open(INPUT_FILE, "r") as file:
            ip_list = file.readlines()
    except FileNotFoundError:
        print("Input file not found.")
        return

    for ip in ip_list:
        ip = ip.strip()

        if ip == "":
            continue

        if ping(ip):
            print(f"ACTIVE     : {ip}")
        else:
            print(f"NON-ACTIVE : {ip}")
            inactive_ips.append(ip)

    print("-" * 40)

    with open(OUTPUT_FILE, "w") as file:
        for ip in inactive_ips:
            file.write(ip + "\n")

    print("Non-active IPs saved to:", OUTPUT_FILE)
    print("Total non-active IPs:", len(inactive_ips))


if __name__ == "__main__":
    main()
