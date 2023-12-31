import time
import signal
import sys

# Signal handler function
def handle_signal(signum, frame):
    print("Received signal:", signum)
    sys.exit(1)

# Register the signal handler for SIGTERM
# https://github.com/orgs/community/discussions/26311#discussioncomment-6231898
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

def main():
    try:
        print("doing some work!")
        start_time = time.time()
        
        while time.time() - start_time < 100:
            print("Monitoring...")
            time.sleep(1)  # Add a small delay to prevent excessive looping - check in / test exec...!
        print("done...")
    except Exception as e:
        print("except block: {e}")

if __name__ == "__main__":
    main()
