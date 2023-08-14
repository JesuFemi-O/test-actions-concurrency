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
    print("Sleeping for 3 minutes...")
    time.sleep(180)  # Sleep for 3 minutes (180 seconds)
    print("Done sleeping!")

if __name__ == "__main__":
    main()
