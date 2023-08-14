import time
import signal
import sys

# Signal handler function
def handle_signal(signum, frame):
    print("Received signal:", signum)
    sys.exit(1)

# Register the signal handler for SIGTERM
signal.signal(signal.SIGTERM, handle_signal)

def main():
    print("doing some work!")
    start_time = time.time()
    # time.sleep(50)  # Sleep for 3 minutes (180 seconds) or get stopped
    while time.time() - start_time < 27:
        print("Monitoring...")
        time.sleep(1)  # Add a small delay to prevent excessive looping

if __name__ == "__main__":
    main()
