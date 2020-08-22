import subprocess
from datetime import datetime
import validators
import os

class Ping():
    def __init__(self, num_bytes, time, ttl, timestamp, failure=None):
        self.bytes = num_bytes
        self.time = time
        self.ttl = ttl
        self.timestamp = datetime.now()
        self.failure = False

    def __repr__(self):
        if self.failure:
            return "Failed ping at " + str(self.timestamp)
        else:
            return "Timestamp: " + str(self.timestamp) + "\nBytes: " + str(self.bytes) + "\nTime: " + str(self.time) + "\nTTL: " + str(self.ttl)

# tokenize ping output
# correlate with timestamp from datetime.datetime.now()

def ping(dest: str):
    if os.name == "nt":
        # check user input
        if validators.ip_address.ipv4(dest) or validators.domain(dest):
            result = subprocess.check_output(["ping", "-n", "1", dest]).decode("utf-8")
            parse(result)
        else:
            print("invalid input")

    else:
        print("Unsupported operating system")

def parse(ping) -> Ping:
    return Ping(ping.split(' ')[9].split("=")[1], ping.split(' ')[10].split("=")[1], ping.split(' ')[11].split("=")[1], datetime.now())


def process_results(ping):
    successful_pings = []
    failed_pings = []

    if ping.failure == False:
        successful_pings.append(ping)
    else:
        failed_pings.append(ping)

def main():
    ping("1.1.1.1")
    # ping("google.com")

if __name__ == "__main__":
    main()