# DataMorpher 🚀  
**DataMorpher** is an automated data ingestion tool that transforms multiple data formats (CSV, Excel, JSON, XML) into SQL Server tables. Designed with Python and Docker, it offers a stylish command-line interface, robust logging, and full automation.

---

## Features  
- 📂 **Supports multiple data formats**: CSV, Excel (all sheets), JSON, and XML  
- 📝 **Logs all operations**: Detailed logs for successful uploads and errors (`logs/upload_log.txt`)  
- 💻 **Stylish CLI Interface**: ASCII art, colorful menus, and friendly exit messages for an enhanced user experience.  
- 🐳 **Dockerized for Easy Deployment**: Build once and run anywhere.  

---

## Prerequisites  
- Docker and Docker Compose installed on your machine.  
- Python packages (`pandas`, `sqlalchemy`, `pymssql`, `pyfiglet`, `colorama`, etc.) included in the Docker build.

---

## How to Run  

### 1: Clone the Repository  
   ```bash
   git clone https://github.com/your-username/DataMorpher.git
   cd DataMorpher
   ```

### 2. Build the Docker image:  
   ```bash
   docker-compose build
   ```

### 3. Run the application:  
   ```bash
   docker-compose up
   ```

### 4: Use the Interactive Menu
Once the application starts, you’ll see an interactive menu:

```bash
   ____        __        __  ___                 __             
   / __ \____ _/ /_____ _/  |/  /___  _________  / /_  ___  _____
  / / / / __ `/ __/ __ `/ /|_/ / __ \/ ___/ __ \/ __ \/ _ \/ ___/
 / /_/ / /_/ / /_/ /_/ / /  / / /_/ / /  / /_/ / / / /  __/ /    
/_____/\__,_/\__/\__,_/_/  /_/\____/_/  / .___/_/ /_/\___/_/     
                                       /_/                       

   Welcome to DataMorpher! The Ultimate Data Ingestion Tool.

   Main Menu:
   1. Connect to Database
   2. Upload Files
   3. Exit
   Choose an option (1/2/3): 
```

### 5. Follow the interactive menu to connect to your database

You will be prompted to enter your database IP address and database name.

- If you’re running SQL Server locally in a Docker container, use localhost as the IP address.
- Otherwise, enter the network IP of your SQL Server instance.

```bash
   Enter database IP address: localhost  
   Enter database name: test_db  
```

## 6. How to Upload Files  
Once the application starts, choose the file type from the `/app/data` directory:  

1. **CSV Files**  
2. **JSON Files**  
3. **XML Files**  
4. **Excel Files (All Sheets)**  

## 7. Logs  
All operations (successful uploads and errors) are logged in `logs/upload_log.txt`.  
To view logs:  
```bash
cat logs/upload_log.txt
```

## 8. Directory Structure  
```
DataMorpher/
├── automate.py           # Main script with interactive menu
├── Dockerfile            # Docker build instructions
├── docker-compose.yml    # Docker Compose configuration
├── handlers/             # Handlers for CSV, JSON, XML, and Excel files
├── database/             # Database connection module
├── logs/                 # Log directory for upload logs
└── data/                 # Directory for input files
```

 
## 9. Future Enhancements  
- Support for additional databases (PostgreSQL, MySQL)  
- Data validation and preprocessing before upload  
- Database R integration  
- Referential integrity checks (currently not supported)  
- Web-based interface for managing data uploads  


## License  
MIT License. Feel free to use and contribute!

## Author  
**Subash Yadav** – Developer of DataMorpher  
[GitHub Profile](https://github.com/mathachew7)
