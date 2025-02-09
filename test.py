if __name__ == "__main__":
    ip = "192.168.1.131"  # Replace with your server IP
    db_name = "sqlpractice"
    
    conn = connect_to_database(ip, db_name)
    if conn:
        print("Connection test successful!")
    else:
        print("Connection test failed.")
