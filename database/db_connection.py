from sqlalchemy import create_engine, text
import logging

def connect_to_database(ip, db_name):
    """
    Connect to SQL Server database using SQLAlchemy.
    :param ip: IP address of the SQL Server
    :param db_name: Name of the database to connect to
    :return: SQLAlchemy engine object if successful, None otherwise
    """
    try:
        connection_string = f"mssql+pymssql://sa:password123@{ip}:1433/{db_name}"
        engine = create_engine(connection_string)
        
        # Test the connection with a valid query
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        
        logging.info(f"Connected to database at {ip}/{db_name}")
        print(f"Connected successfully to database: {db_name} at {ip}")
        return engine
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        print(f"Database connection failed: {e}")
        return None
