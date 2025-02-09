import pandas as pd
import logging
import os

def upload_all_excel_in_dir(engine):
    """
    Automatically uploads all sheets from all Excel (.xlsx) files in /app/data to the SQL database.
    :param engine: SQLAlchemy engine object
    """
    directory_path = "/app/data"
    try:
        found_excel = False
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.xlsx'):
                found_excel = True
                file_path = os.path.join(directory_path, file_name)
                print(f"Processing Excel file '{file_name}'...")
                
                # Load all sheets into a dictionary of DataFrames
                excel_data = pd.read_excel(file_path, sheet_name=None)
                
                for sheet_name, df in excel_data.items():
                    table_name = (os.path.splitext(file_name)[0] + "_" + sheet_name).replace(" ", "_").lower()
                    print(f"Uploading sheet '{sheet_name}' to table '{table_name}'...")
                    
                    # Upload each sheet to the database
                    df.to_sql(table_name, engine, if_exists='replace', index=False)
                    
                    logging.info(f"Successfully uploaded sheet '{sheet_name}' from '{file_name}' to table '{table_name}'")
                    print(f"Successfully uploaded sheet '{sheet_name}' to table '{table_name}'")
        
        if not found_excel:
            print("No Excel (.xlsx) files found in /app/data.")
    except Exception as e:
        logging.error(f"Failed to upload Excel files: {e}")
        print(f"Failed to upload Excel files: {e}")
