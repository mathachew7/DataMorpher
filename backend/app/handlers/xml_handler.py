import pandas as pd
import logging
import os

def upload_uploaded_xml_files(engine, uploaded_files):
    """
    Uploads all uploaded XML files to the database using SQLAlchemy.
    :param engine: SQLAlchemy engine object
    :param uploaded_files: list of FileStorage objects (from Flask)
    """
    try:
        if not uploaded_files:
            print("No XML files received.")
            return {"status": "error", "message": "No XML files uploaded."}

        for file in uploaded_files:
            filename = file.filename
            if not filename.endswith(".xml"):
                continue

            table_name = os.path.splitext(filename)[0].replace(" ", "_").lower()
            print(f"Uploading file '{filename}' to table '{table_name}'...")

            df = pd.read_xml(file, parser="etree")
            df.to_sql(table_name, engine, if_exists="replace", index=False)

            logging.info(f"Uploaded '{filename}' to table '{table_name}'")
            print(f"✅ Uploaded '{filename}' to table '{table_name}'")

        return {"status": "success", "message": "All XML files uploaded successfully."}

    except Exception as e:
        logging.error(f"XML upload failed: {e}")
        print(f"❌ XML upload failed: {e}")
        return {"status": "error", "message": str(e)}
