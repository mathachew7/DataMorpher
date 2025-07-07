import os
import logging
import time
import pyfiglet
from colorama import Fore, init

# Initialize colorama for colored output
init(autoreset=True)

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/upload_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p %Z'
)

def display_intro():
    ascii_art = pyfiglet.figlet_format("DataMorpher", font="slant")
    print(Fore.CYAN + ascii_art)
    print(Fore.YELLOW + "Welcome to DataMorpher Web Edition - Logs and Automation Setup Ready!\n")
    logging.info("🚀 DataMorpher Web Edition launched.")

def main():
    display_intro()
    print(Fore.GREEN + "Web-based data ingestion system is running. No CLI interaction required.")
    print(Fore.GREEN + "Logs will be recorded as data uploads happen via the frontend interface.")
    logging.info("✅ Web backend initialized. Waiting for frontend interactions.")
    while True:
        time.sleep(300)  # Keeps script alive for container environments if needed

if __name__ == "__main__":
    main()
