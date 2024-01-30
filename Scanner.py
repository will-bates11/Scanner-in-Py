import socket
import argparse
import threading
import logging
from queue import Queue

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

# Function to scan a single port
def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                logger.info(f"Port: {port} Open")
    except socket.error:
        pass

# Thread worker function
def threader(q):
    while True:
        worker = q.get()
        scan_port(target_ip, worker)
        q.task_done()

# Main function
def main(target_ip, start_port, end_port, num_threads=100):
    print("*" * 40)
    print(f"* Scanning: {target_ip} *")
    print("*" * 40)

    q = Queue()

    # Start threads
    for x in range(num_threads):
        t = threading.Thread(target=threader, args=(q,))
        t.daemon = True
        t.start()

    # Put ports in queue
    for port in range(start_port, end_port + 1):
        q.put(port)

    q.join()

# Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("ip", help="Target IP address to scan")
    parser.add_argument("-s", "--start", help="Start port", type=int, default=1)
    parser.add_argument("-e", "--end", help="End port", type=int, default=1024)
    args = parser.parse_args()

    target_ip = args.ip
    start_port = args.start
    end_port = args.end

    main(target_ip, start_port, end_port)
