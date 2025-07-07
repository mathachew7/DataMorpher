# 🚀 DataMorpher

**DataMorpher** is a fullstack data ingestion tool built by **Josla Tech**. It allows you to upload multiple file formats—CSV, Excel, JSON, XML—directly into your connected database using a modern web interface.

The tool provides real-time logs of all operations and is fully Dockerized for easy setup and deployment. Its tech stack includes Next.js 14 for the frontend, FastAPI and SQLAlchemy with Python for the backend, and Docker for DevOps. The project aims to reduce manual ETL burden and support local and enterprise database workflows with minimal configuration.
---

## 🔥 Key Features
DataMorpher provides a robust set of features tailored for seamless data ingestion:

 - Multi-File Uploads: Easily upload multiple files simultaneously, supporting popular formats such as CSV, JSON, Excel (.xls and .xlsx), and XML.

 - Database Connectivity: Establish direct connections to MySQL and SQL Server databases from your web browser. The architecture is designed to be extensible, allowing for future database integrations.

 - Intuitive Web Interface: The tool boasts a modern web user interface built with Next.js 14, featuring drag-and-drop file upload capabilities for enhanced usability.

 - Real-time Operational Logs: Monitor all data ingestion operations with real-time logs, providing insights into upload statuses, database events, and error details.

 - Dockerized Deployment: DataMorpher is fully Dockerized, encompassing both the frontend and backend, ensuring easy setup and consistent performance across different environments. It's designed to work locally out-of-the-box.


---

## 🧠 Tech Stack

| Layer      | Tech                                |
| ---------- | ----------------------------------- |
| Frontend   | Next.js 14, Tailwind CSS, shadcn/ui |
| Backend    | FastAPI, SQLAlchemy, Python         |
| DB Support | SQL Server, MySQL (extensible)      |
| DevOps     | Docker, Docker Compose              |

---

## 🛆 Directory Structure

```
DataMorpher/
├── backend/                # FastAPI backend
│   ├── app/                # Application logic
│   ├── database/           # DB connection helpers
│   ├── handlers/           # Upload handlers
│   ├── logs/               # Upload logs
│   └── Dockerfile
├── web/                    # Next.js frontend
│   ├── src/                # All frontend logic
│   └── Dockerfile
├── docker-compose.yml      # Spins up everything
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/DataMorpher.git
cd DataMorpher
```

### 2️⃣ Start All Services

```bash
docker-compose up --build
```

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend API: [http://localhost:5050](http://localhost:5050)

---

## 🧪 How to Use

### 🔗 Step 1: Connect to Your Database

* Go to [http://localhost:3000](http://localhost:3000)
* Choose **Connect MySQL Server**
* Enter:

  * Hostname/IP
  * Port (e.g., `3306` for MySQL, `1433` for SQL Server)
  * Username & Password
  * Database name

> If successful, the connection is saved temporarily in frontend memory

---

### 📄 Step 2: Upload Files

* Navigate to your desired file type (CSV, JSON, Excel, XML)
* Upload multiple files of the same type
* Click **Upload Now**
* Files will be parsed and inserted into your connected database as new tables

---

### 📄 Step 3: View Logs

* Go to `/logs` in frontend
* You’ll see latest 50 log entries from `upload_log.txt`
* Log includes timestamps, DB events, upload statuses, and error details

---

## 🩵 Logs

All operations are logged into:

```bash
backend/app/logs/upload_log.txt
```

To view logs manually:

```bash
cat backend/app/logs/upload_log.txt
```

Or see them at `/logs` in the frontend UI.

---

## ✅ Supported File Types

| File Type | Notes                                          |
| --------- | ---------------------------------------------- |
| CSV       | Standard CSV parser                            |
| JSON      | Expects array of objects                       |
| Excel     | `.xls` and `.xlsx` supported                   |
| XML       | Auto-parses elements using `pandas.read_xml()` |

---

## 🧹 Extending the Project

You can add more databases or file formats by:

* Adding new handlers under `backend/app/handlers/`
* Mapping routes in `main.py`
* Adding upload UI pages in `web/src/app/ingestion/`

---

## 🚀 Roadmap
The future development of DataMorpher includes:
* [ ] PostgreSQL support
* [ ] File content preview before upload
* [ ] AI-powered schema suggestions
* [ ] Voice command ingestion (experimental)

---

## 📜 License

MIT License.
Use freely, fork safely, and contribute generously.

---

## 👨‍💼 Author

**Subash Yadav**
Founder @ Josla Tech
GitHub: [@mathachew7](https://github.com/mathachew7)

---

## 🧠 Inspiration

This project was built to simplify data ingestion across common file types, reduce manual ETL burden, and support local/enterprise database workflows with minimal setup.

> Built with ❤️ by Josla Tech | 2025
