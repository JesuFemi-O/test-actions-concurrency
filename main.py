import time
import signal
import sys

# Signal handler function
def handle_signal(signum, frame):
    print("Received signal:", signum)
    sys.exit(1)

# Register the signal handler for SIGTERM
signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

def main():
    print("doing some work!")
    start_time = time.time()
    
    while time.time() - start_time < 27:
        print("Monitoring...")
        time.sleep(1)  # Add a small delay to prevent excessive looping - check in
    print("done...")

if __name__ == "__main__":
    main()
