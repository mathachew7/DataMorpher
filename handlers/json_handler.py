import pandas as pd
import logging
import os

def upload_all_json_in_dir(engine):
    """
    Automatically uploads all JSON files in /app/data to the database using SQLAlchemy.
    :param engine: SQLAlchemy engine object
    """
    directory_path = "/app/data"
    try:
        found_json = False
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.json'):
                found_json = True
                file_path = os.path.join(directory_path, file_name)
                table_name = os.path.splitext(file_name)[0].replace(" ", "_").lower()
                print(f"Uploading file '{file_name}' to table '{table_name}'...")
                
                df = pd.read_json(file_path)
                df.to_sql(table_name, engine, if_exists='replace', index=False)
                
                logging.info(f"Successfully uploaded '{file_name}' to table '{table_name}'")
                print(f"Successfully uploaded '{file_name}' to table '{table_name}'")
        
        if not found_json:
            print("No JSON files found in /app/data.")
    except Exception as e:
        logging.error(f"Failed to upload JSON files: {e}")
        print(f"Failed to upload JSON files: {e}")
