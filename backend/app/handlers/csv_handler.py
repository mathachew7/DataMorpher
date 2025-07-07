import pandas as pd
import logging

def upload_uploaded_csv_files(engine, uploaded_files):
    """
    Uploads multiple in-memory CSV files received via Flask's request.files to the database.
    :param engine: SQLAlchemy engine object
    :param uploaded_files: list of FileStorage objects (from Flask)
    """
    try:
        if not uploaded_files:
            print("No CSV files received.")
            return {"status": "error", "message": "No CSV files uploaded."}

        for file in uploaded_files:
            filename = file.filename
            if not filename.endswith('.csv'):
                continue

            table_name = filename.rsplit(".", 1)[0].replace(" ", "_").lower()
            print(f"Uploading file '{filename}' to table '{table_name}'...")

            df = pd.read_csv(file)
            df.to_sql(table_name, engine, if_exists='replace', index=False)

            logging.info(f"Successfully uploaded '{filename}' to table '{table_name}'")
            print(f"✅ Uploaded '{filename}' to table '{table_name}'")

        return {"status": "success", "message": "All CSV files uploaded successfully."}

    except Exception as e:
        logging.error(f"CSV upload failed: {e}")
        print(f"❌ CSV upload failed: {e}")
        return {"status": "error", "message": str(e)}
