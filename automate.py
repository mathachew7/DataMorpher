import pandas as pd
from sqlalchemy import create_engine
import logging

# Step 1: Configure logging
logging.basicConfig(
    filename='/app/upload_log.txt',  # Log file path
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Step 2: Connect to SQL Server using pymssql
#if localhost doesnot work then
# try ifconfig | grep inet   or ipconfig 
# instead of localhost try using your system ip address 

engine = create_engine("mssql+pymssql://sa:password123@localhost:1433/sqlpractice")


# Step 3: Load the Excel file
excel_file = '/app/data.xlsx'  # Ensure this file is copied into the container
xls = pd.ExcelFile(excel_file)
logging.info(f"Available sheets: {xls.sheet_names}")

# Step 4: Loop through each sheet and upload it as a table in SQL Server
for sheet_name in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    table_name = sheet_name.replace(" ", "_").lower()
    logging.info(f"Attempting to upload sheet '{sheet_name}' as table '{table_name}'...")
    
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Successfully uploaded sheet '{sheet_name}' as table '{table_name}'")
    except Exception as e:
        logging.error(f"Error uploading sheet '{sheet_name}': {e}")

    print("All sheets have been processed. Check 'upload_log.txt' for details.")

print("Please verify the dataset. Check 'upload_log.txt' for details.")