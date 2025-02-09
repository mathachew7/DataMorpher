import pandas as pd
import logging
import os

def upload_all_xml_in_dir(engine):
    """
    Automatically uploads all XML files in /app/data to the database using SQLAlchemy.
    :param engine: SQLAlchemy engine object
    """
    directory_path = "/app/data"
    try:
        found_xml = False
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.xml'):
                found_xml = True
                file_path = os.path.join(directory_path, file_name)
                table_name = os.path.splitext(file_name)[0].replace(" ", "_").lower()
                print(f"Uploading file '{file_name}' to table '{table_name}'...")
                
                df = pd.read_xml(file_path, parser= 'etree')
                df.to_sql(table_name, engine, if_exists='replace', index=False)
                
                logging.info(f"Successfully uploaded '{file_name}' to table '{table_name}'")
                print(f"Successfully uploaded '{file_name}' to table '{table_name}'")
        
        if not found_xml:
            print("No XML files found in /app/data.")
    except Exception as e:
        logging.error(f"Failed to upload XML files: {e}")
        print(f"Failed to upload XML files: {e}")
