A Python CLI tool that lets you scan one or more targets for open TCP ports through a simple prompt-driven interface.
It demonstrates basic networking concepts using Python's built-in `socket` module.

## Project Structure

| File | Description |
|------|-------------|
| `network_scanner.py` | Main script. Handles input, validation, and scanning logic |
| `requirements.txt` | Python dependencies |
| `Makefile` | Shortcuts for common tasks |

## How It Works

On startup, the program prompts the user for targets and a port range, then attempts a TCP connection on each port and reports which ones are open.

### Input Prompts

| Prompt | Description |
|--------|-------------|
| Targets | One or more IPv4 addresses, comma-separated |
| Port count | Number of ports to scan, from `1` up to `65535` |

### Output

Each open port is reported as it is found. If no open ports are found on a target, the user is warned. 
All output is color-coded for readability.

## Functions Overview

### `is_ip_valid(ip)`
- Validates an IPv4 address using a regex pattern
- Checks that each octet is in the range `0–255`

### `is_ip_reachable(ip)`
- Attempts a reverse DNS lookup on the IP to confirm it is a real, reachable address
- Rejects IPs that cannot be resolved

### `get_valid_targets()`
- Prompts the user for one or more IPv4 addresses
- Accepts only IPs that are both valid in format and reachable
- Skips and warns about invalid or unreachable entries
- Repeats until at least one valid target is provided

### `get_valid_port_count()`
- Prompts the user for a number of ports to scan
- Validates the input is an integer between `1` and `65535`

### `scan(target, ports)`
- Iterates over ports `1` to `ports` and calls `scan_port` on each
- Warns the user if no open ports are found on the target

### `scan_port(ipaddress, port)`
- Attempts a TCP connection to the given port with a 1-second timeout
- Returns `True` if the port is open, `False` otherwise

## Building

No compilation needed. 
Install dependencies with:

### Windows
```bash
pip install -r requirements.txt
```

### Linux/macOS
```bash
make install
```

## Running

### Windows
```bash
python network_scanner.py
```

### Linux/macOS
```bash
make run
```

## Notes

- Input validation is handled throughout. Invalid or unreachable IPs are skipped and invalid port values prompt the user to try again without crashing.
- Only valid IPv4 addresses that pass reverse DNS resolution are accepted as targets.
- This tool is intended for **educational purposes** and for use only on networks and systems you own or have explicit permission to scan.
