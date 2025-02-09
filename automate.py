import sys
import os
import logging
import time
import pyfiglet
from colorama import Fore, Style, init
from database.db_connection import connect_to_database
from handlers.csv_handler import upload_all_csv_in_dir
from handlers.json_handler import upload_all_json_in_dir
from handlers.xml_handler import upload_all_xml_in_dir
from handlers.excel_handler import upload_all_excel_in_dir

# Initialize colorama for color support
init(autoreset=True)

# Ensure logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/upload_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p %Z'
)

def display_intro():
    """
    Display the introductory ASCII art and welcome message.
    """
    ascii_art = pyfiglet.figlet_format("DataMorpher", font="slant")
    print(Fore.CYAN + ascii_art)
    print(Fore.YELLOW + "Welcome to DataMorpher! The Ultimate Data Ingestion Tool.\n")
    time.sleep(1)

def main():
    """
    Main function to provide a menu-driven interface for DataMorpher.
    """
    display_intro()
    engine = None
    while True:
        print(Fore.GREEN + "\nMain Menu:")
        print(Fore.BLUE + "1. Connect to Database")
        print(Fore.BLUE + "2. Upload Files")
        print(Fore.BLUE + "3. Exit")
        
        choice = input(Fore.CYAN + "Choose an option (1/2/3): ")
        
        if choice == '1':
            engine = connect_to_db()
        elif choice == '2':
            if engine:
                file_upload_menu(engine)
            else:
                print(Fore.RED + "Please connect to the database first.")
        elif choice == '3':
            goodbye_message()
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

def connect_to_db():
    """
    Connect to the SQL database using SQLAlchemy and return the engine.
    """
    print(Fore.CYAN + "\n--- Connect to Database ---")
    ip = input(Fore.YELLOW + "Enter database IP address: ")
    db_name = input(Fore.YELLOW + "Enter database name: ")
    
    engine = connect_to_database(ip, db_name)
    if engine:
        print(Fore.GREEN + "Connected successfully!")
        logging.info(f"Connected to database at {ip}/{db_name}")
        return engine
    else:
        print(Fore.RED + "Failed to connect. Please check your details and try again.")
        logging.error(f"Failed to connect to database at {ip}/{db_name}")
        return None

def file_upload_menu(engine):
    """
    Provides a menu for uploading different file formats.
    """
    print(Fore.CYAN + "\n--- File Upload Menu ---")
    print(Fore.BLUE + "1. Upload all CSV files in /app/data")
    print(Fore.BLUE + "2. Upload all JSON files in /app/data")
    print(Fore.BLUE + "3. Upload all XML files in /app/data")
    print(Fore.BLUE + "4. Upload all Excel (.xlsx) files in /app/data")
    print(Fore.BLUE + "5. Return to Main Menu")
    
    choice = input(Fore.CYAN + "Choose a file type to upload (1/2/3/4/5): ")
    
    if choice == '1':
        upload_all_csv_in_dir(engine)
    elif choice == '2':
        upload_all_json_in_dir(engine)
    elif choice == '3':
        upload_all_xml_in_dir(engine)
    elif choice == '4':
        upload_all_excel_in_dir(engine)
    elif choice == '5':
        print(Fore.YELLOW + "Returning to Main Menu...")
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        file_upload_menu(engine)

def goodbye_message():
    """
    Display a goodbye message with a loading animation for a polished exit.
    """
    print(Fore.YELLOW + "\nThank you for using DataMorpher!")
    print(Fore.CYAN + "Exiting...")
    for i in range(3):
        time.sleep(0.5)
        print(Fore.CYAN + "." * (i + 1), end='', flush=True)
    print(Fore.GREEN + "\nGoodbye!\n")

if __name__ == "__main__":
    main()
