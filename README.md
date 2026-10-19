# Network Traffic Analyzer

A beginner-friendly network traffic analysis tool built with Python and Scapy. It reads PCAP/PCAPNG capture files and summarizes packet details, protocols, and IP address activity.

## Features

- Reads PCAP and PCAPNG files.
- Displays the total number of captured packets.
- Extracts packet timestamps.
- Displays source and destination IP addresses.
- Identifies TCP, UDP, ICMP, and other IP protocols.
- Displays packet lengths in bytes.
- Counts packets by protocol.
- Counts packets by source IP address.
- Counts packets by destination IP address.
- Sorts source and destination IP reports by packet count in descending order.
- Identifies packets that do not contain an IP layer.

## Requirements

- Python 3
- Scapy

## Installation

Install Python 3 from [python.org](https://www.python.org/downloads/).

Install Scapy using pip:

```bash
python -m pip install scapy
```

## Usage

1. Clone or download this repository.
2. Open `network-traffic-analyzer.py`.
3. Update the `filename` variable with the path to your PCAP or PCAPNG file.
4. Run the script:

```bash
python network-traffic-analyzer.py
```

## Example Output

```text
Total packets: 20000

Time: Tue Jan 12 09:21:46 2016 | Packet: 1 | Source IP: 192.168.1.10 | Destination IP: 192.168.1.20 | Protocol: TCP | Length: 74 bytes

--- Protocol Tally ---
TCP: 14500
UDP: 3200
ICMP: 100
Other: 50

--- Top Source IPs ---
192.168.1.10: 450
192.168.1.20: 230

--- Top Destination IPs ---
192.168.1.20: 500
192.168.1.30: 180
```

*Note: The output above is illustrative. Actual results depend on the capture file.*

## How It Works

The analyzer uses Scapy to load captured packets and inspect their network layers. It identifies IP packets, classifies their protocols, extracts timestamps and IP addresses, and maintains dictionaries to calculate packet counts.

The final reports summarize protocol distribution and the most frequently observed source and destination IP addresses.

## Limitations

- This is a basic offline packet analyzer; it does not capture live network traffic.
- Protocol classification and statistics are limited to the implemented logic.
- Packet counts alone do not establish whether traffic is malicious.
- The analyzer currently requires the capture file path to be configured in the Python script.
- Large capture files may require substantial memory because Scapy loads packets into memory.

## Future Improvements

- Add command-line arguments for selecting capture files.
- Add TCP and UDP port statistics.
- Add protocol and IP address filters.
- Add improved error handling and input validation.
- Export analysis reports to CSV.
- Add more advanced traffic-analysis indicators.

## Disclaimer

This project is intended for educational purposes and authorized network analysis only. Use packet captures only when you have permission to analyze and share them. Do not upload captures containing private or sensitive information without appropriate authorization.

## License

Choose a license before publishing if you want others to reuse, modify, or distribute this project. For example, you can use the MIT License.
