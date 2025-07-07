import pandas as pd
import logging
import os

def upload_uploaded_json_files(engine, uploaded_files):
    """
    Uploads all uploaded JSON files to the database using SQLAlchemy.
    :param engine: SQLAlchemy engine object
    :param uploaded_files: list of FileStorage objects (from Flask)
    """
    try:
        if not uploaded_files:
            print("No JSON files received.")
            return {"status": "error", "message": "No JSON files uploaded."}

        for file in uploaded_files:
            filename = file.filename
            if not filename.endswith(".json"):
                continue

            print(f"Uploading file '{filename}'...")

            table_name = os.path.splitext(filename)[0].replace(" ", "_").lower()
            df = pd.read_json(file)
            df.to_sql(table_name, engine, if_exists='replace', index=False)

            logging.info(f"Uploaded '{filename}' to table '{table_name}'")
            print(f"✅ Uploaded '{filename}' to table '{table_name}'")

        return {"status": "success", "message": "All JSON files uploaded successfully."}

    except Exception as e:
        logging.error(f"JSON upload failed: {e}")
        print(f"❌ JSON upload failed: {e}")
        return {"status": "error", "message": str(e)}
