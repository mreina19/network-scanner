import socket
import termcolor
import re

#Checks if the IPV4 address is valid
def is_ip_valid(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    if re.match(pattern, ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))

    return False


#Checks if the IP is reachable/exists via DNS resolution
def is_ip_reachable(ip):
    try:
        socket.gethostbyaddr(ip)
        return True

    except socket.herror:
        return False


#Gets the valid input IP addresses
def get_valid_targets():
    while True:
        raw_input = input("[?] Enter targets to scan (separate multiple IPs with commas): ")

        #Removes white spaces and ignores empty values
        targets = [t.strip() for t in raw_input.split(',') if t.strip()]

        if not targets:
            print(termcolor.colored("[!!] No targets entered. Try again.\n", 'red'))
            continue

        valid_targets = []

        for item in targets:

            #Accepts only valid and reachable IPs
            if is_ip_valid(item) and is_ip_reachable(item):
                valid_targets.append(item)

            else:
                print(termcolor.colored(f"[!] Invalid or unreachable target skipped: {item}.", 'magenta'))

        if valid_targets:
            return valid_targets

        else:
            print(termcolor.colored("[!] No valid targets found. Try again.\n", 'magenta'))


#Gets how many ports the user wants to scan
def get_valid_port_count():
    while True:
        try:
            ports = int(input("[?] Enter how many ports you want to scan (1 to 65535): "))

            if 1 <= ports <= 65535:
                return ports

            else:
                print(termcolor.colored("[!] Invalid range. Please enter a number between 1 and 65535.\n", 'magenta'))

        except ValueError:
            print(termcolor.colored("[!!] Invalid input. Please enter a numeric value.\n", 'red'))


#Scans all ports and warns if none are open
def scan(target, ports):
    print('\n' + termcolor.colored(f"[i] Starting scan for {target}", 'cyan'))

    open_ports = 0

    for port in range(1, ports + 1):
        if scan_port(target, port):
            open_ports += 1

    if open_ports == 0:
        print(termcolor.colored(f"[-] No open ports found on {target}.\n", 'yellow'))


#Scans a specific port, returns True if open
def scan_port(ipaddress, port):
    try:
        with socket.socket() as sock:
            sock.settimeout(1)
            sock.connect((ipaddress, port))
            print(termcolor.colored(f"[+] Port {port} is open on {ipaddress}.", 'green'))
            return True

    except socket.error:
        return False


def main():
    targets = get_valid_targets()
    ports = get_valid_port_count()

    if len(targets) > 1:
        print(termcolor.colored("\n[i] Scanning multiple targets...\n", 'cyan'))

    for ip_addr in targets:
        scan(ip_addr, ports)

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print(termcolor.colored("\n[!!] Scan interrupted by user.", 'red'))
