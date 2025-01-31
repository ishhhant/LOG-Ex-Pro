import sys
import os
import mmap

# Define directories
LOGS_DIR = "logs"
OUTPUT_DIR = "output"

def extract_logs(target_date):
    """
    Extracts log entries for a specific date from a large log file efficiently using mmap.
    
    Args:
        target_date (str): The date (YYYY-MM-DD) to filter logs.
    """
    log_file_path = os.path.join(LOGS_DIR, "test_logs.log")
    output_file_path = os.path.join(OUTPUT_DIR, f"output_{target_date}.txt")

    # Ensure directories exist
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        with open(log_file_path, "r+b") as file, open(output_file_path, "w", encoding="utf-8") as output:
            with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
                for line in iter(mmapped_file.readline, b""):  # Read line-by-line using mmap
                    decoded_line = line.decode("utf-8")  # Decode bytes to string
                    if decoded_line.startswith(target_date):
                        output.write(decoded_line)

        print(f"✅ Logs for {target_date} saved to: {output_file_path}")

    except FileNotFoundError:
        print(f"❌ Error: Log file {log_file_path} not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    target_date = sys.argv[1]
    extract_logs(target_date)
