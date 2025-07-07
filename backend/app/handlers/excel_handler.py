import pandas as pd
import logging

def upload_uploaded_excel_files(engine, uploaded_files):
    """
    Uploads all sheets from uploaded Excel files to the SQL database.
    :param engine: SQLAlchemy engine object
    :param uploaded_files: list of FileStorage objects (from Flask)
    """
    try:
        if not uploaded_files:
            print("No Excel files received.")
            return {"status": "error", "message": "No Excel files uploaded."}

        for file in uploaded_files:
            filename = file.filename
            if not filename.endswith('.xlsx'):
                continue

            print(f"Processing Excel file '{filename}'...")

            # Load all sheets
            excel_data = pd.read_excel(file, sheet_name=None)

            for sheet_name, df in excel_data.items():
                table_name = (os.path.splitext(filename)[0] + "_" + sheet_name).replace(" ", "_").lower()
                print(f"Uploading sheet '{sheet_name}' to table '{table_name}'...")

                df.to_sql(table_name, engine, if_exists='replace', index=False)

                logging.info(f"Successfully uploaded sheet '{sheet_name}' from '{filename}' to table '{table_name}'")
                print(f"✅ Uploaded sheet '{sheet_name}' to table '{table_name}'")

        return {"status": "success", "message": "All Excel files uploaded successfully."}

    except Exception as e:
        logging.error(f"Excel upload failed: {e}")
        print(f"❌ Excel upload failed: {e}")
        return {"status": "error", "message": str(e)}
