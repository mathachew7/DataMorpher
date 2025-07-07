import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging for this module if not already
logging.basicConfig(
    filename='logs/upload_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p %Z'
)

def connect_to_database(host, db_name, user, password, port, db_type):
    try:
        logging.info(f"🔌 Attempting DB connection → host={host}, port={port}, db={db_name}, user={user}, type={db_type}")
        
        if db_type.lower() == "mysql":
            url = URL.create(
                drivername="mysql+pymysql",
                username=user,
                password=password,
                host=host,
                port=int(port),
                database=db_name,
            )
        elif db_type.lower() == "mssql":
            url = URL.create(
                drivername="mssql+pymssql",
                username=user,
                password=password,
                host=host,
                port=int(port),
                database=db_name,
            )
        else:
            raise ValueError(f"❌ Unsupported database type: {db_type}")

        engine = create_engine(url)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        logging.info("✅ Database connection successful.")
        return engine

    except Exception as e:
        logging.error(f"❌ Database connection failed: {e}")
        return None
