import pandas as pd
import logging
import os

def upload_all_csv_in_dir(engine):
    """
    Automatically uploads all CSV files in /app/data to the database using SQLAlchemy.
    :param engine: SQLAlchemy engine object
    """
    directory_path = "/app/data"
    try:
        found_csv = False
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.csv'):
                found_csv = True
                file_path = os.path.join(directory_path, file_name)
                table_name = os.path.splitext(file_name)[0].replace(" ", "_").lower()
                print(f"Uploading file '{file_name}' to table '{table_name}'...")
                
                df = pd.read_csv(file_path)
                df.to_sql(table_name, engine, if_exists='replace', index=False)
                
                logging.info(f"Successfully uploaded '{file_name}' to table '{table_name}'")
                print(f"Successfully uploaded '{file_name}' to table '{table_name}'")
        
        if not found_csv:
            print("No CSV files found in /app/data.")
    except Exception as e:
        logging.error(f"Failed to upload CSV files: {e}")
        print(f"Failed to upload CSV files: {e}")
