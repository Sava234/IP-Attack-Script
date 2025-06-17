# IP-Attack-Script
This is a basic Python script that sends multiple TCP connection requests to a specified IP address on port 80. It is intended for educational or testing purposes only.  Use this script only on systems you own or have permission to test. Unauthorized use may be illegal.

Features
Connects to a given IP using TCP
Displays status messages with colored output
Sends multiple requests with a delay between each

Requirements
Python 3.x

Usage

Run the script using Python:

    python3 main.py

You will be prompted to enter an IP address. The script will then start sending connection attempts.
Configuration

You can change the following settings directly in the script:

    port = 80           # Target port
    num_requests = 100  # Number of requests to send
    time.sleep(1)       # Delay between each request in seconds

Disclaimer
This script is provided for educational and legal testing purposes only. Use it responsibly.
