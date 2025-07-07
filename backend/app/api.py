from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.exc import SQLAlchemyError
from database.db_connection import connect_to_database
from handlers.csv_handler import upload_uploaded_csv_files
from handlers.json_handler import upload_uploaded_json_files
from handlers.xml_handler import upload_uploaded_xml_files
from handlers.excel_handler import upload_uploaded_excel_files
import logging
import json
import os

app = Flask(__name__)
CORS(app)

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Setup logging
log_path = 'logs/upload_log.txt'
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p %Z'
)
logger = logging.getLogger(__name__)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running"})

@app.route("/connect", methods=["POST"])
def connect():
    data = request.json
    try:
        engine = connect_to_database(
            data.get("host"),
            data.get("database"),
            data.get("user"),
            data.get("password"),
            data.get("port"),
            data.get("dbType")
        )
        if engine:
            logger.info("✅ Connection established.")
            return jsonify({"status": "success", "message": "Connected successfully."}), 200
        else:
            logger.warning("❌ Connection failed.")
            return jsonify({"status": "error", "message": "Connection failed."}), 500
    except Exception as e:
        logger.error(f"❌ Connection error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/upload/csv", methods=["POST"])
def upload_csv():
    try:
        if "db_connection" not in request.form:
            return jsonify({"error": "Missing db_connection"}), 400

        db_info = json.loads(request.form["db_connection"])
        engine = connect_to_database(
            db_info["host"], db_info["database"], db_info["user"],
            db_info["password"], int(db_info["port"]), db_info["dbType"]
        )
        if not engine:
            return jsonify({"error": "Database not connected."}), 500

        files = request.files.getlist("file")
        result = upload_uploaded_csv_files(engine, files)
        return jsonify(result)

    except Exception as e:
        logger.error(f"CSV upload error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/upload/json", methods=["POST"])
def upload_json():
    try:
        if "db_connection" not in request.form:
            return jsonify({"error": "Missing db_connection"}), 400

        db_info = json.loads(request.form["db_connection"])
        engine = connect_to_database(
            db_info["host"], db_info["database"], db_info["user"],
            db_info["password"], int(db_info["port"]), db_info["dbType"]
        )
        if not engine:
            return jsonify({"error": "Database not connected."}), 500

        files = request.files.getlist("file")
        result = upload_uploaded_json_files(engine, files)
        return jsonify(result)

    except Exception as e:
        logger.error(f"JSON upload error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/upload/xml", methods=["POST"])
def upload_xml():
    try:
        if "db_connection" not in request.form:
            return jsonify({"error": "Missing db_connection"}), 400

        db_info = json.loads(request.form["db_connection"])
        engine = connect_to_database(
            db_info["host"], db_info["database"], db_info["user"],
            db_info["password"], int(db_info["port"]), db_info["dbType"]
        )
        if not engine:
            return jsonify({"error": "Database not connected."}), 500

        files = request.files.getlist("file")
        result = upload_uploaded_xml_files(engine, files)
        return jsonify(result)

    except Exception as e:
        logger.error(f"XML upload error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/upload/excel", methods=["POST"])
def upload_excel():
    try:
        if "db_connection" not in request.form:
            return jsonify({"error": "Missing db_connection"}), 400

        db_info = json.loads(request.form["db_connection"])
        engine = connect_to_database(
            db_info["host"], db_info["database"], db_info["user"],
            db_info["password"], int(db_info["port"]), db_info["dbType"]
        )
        if not engine:
            return jsonify({"error": "Database not connected."}), 500

        files = request.files.getlist("file")
        result = upload_uploaded_excel_files(engine, files)
        return jsonify(result)

    except Exception as e:
        logger.error(f"Excel upload error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/logs", methods=["GET"])
def get_logs():
    try:
        with open(log_path, "r") as f:
            lines = f.readlines()[-100:]
        logs = [{"line": line.strip()} for line in lines]
        return jsonify({"logs": logs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
