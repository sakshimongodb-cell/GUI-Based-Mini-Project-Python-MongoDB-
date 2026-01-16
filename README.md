# GUI-Based-Mini-Project-Python-MongoDB-
# Lumina Library Management System 📚

A professional Python-based desktop application for managing library inventory, integrated with a MongoDB NoSQL database. This project was built to demonstrate CRUD operations, data validation, and business reporting (CSV export) within a GUI environment.

## 🚀 Features

* **Secure Admin Login**: Gatekeeper access using a dedicated login window.
* **Full CRUD Operations**:
    * **Create**: Add new books with Title, Author, and ISBN.
    * **Read**: Real-time synchronization with MongoDB to display inventory in a table.
    * **Delete**: Remove records with a single click and confirmation prompt.
* **Advanced Search**: Live search functionality to filter books by ISBN using MongoDB Regex.
* **Data Validation**: Prevents empty entries and ensures data integrity at the database level.
* **Export to CSV**: One-click generation of inventory reports for use in Excel or Google Sheets.
* **Modern UI**: Built with Python's Tkinter (TTK) for a clean, professional user experience.

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **Database**: MongoDB (Local Instance)
* **GUI Framework**: Tkinter / TTK
* **Database Driver**: PyMongo
* **Reporting**: CSV Module

## 📋 Prerequisites

Before running the application, ensure you have the following installed:
1.  **Python**: [Download Python](https://www.python.org/downloads/)
2.  **MongoDB Community Server**: [Download MongoDB](https://www.mongodb.com/try/download/community)
3.  **MongoDB Compass**: (Optional but recommended for visual data management)

## 🔧 Installation & Setup

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Lumina-Library-System.git](https://github.com/YOUR_USERNAME/Lumina-Library-System.git)
    cd Lumina-Library-System
    ```

2.  **Install Dependencies**:
    ```bash
    pip install pymongo
    ```

3.  **Database Configuration**:
    * Open MongoDB Compass and connect to your local server (`localhost:27017`).
    * Create a database named `SakshiMongoDB`.
    * Create a collection named `Library`.

4.  **Run the Application**:
    ```bash
    python library_app.py
    ```

## 🔐 Login Credentials
* **Username**: `admin`
* **Password**: `123`

## 📸 Screenshots

| Login Page | Main Dashboard |
| :--- | :--- |
| ![Login Screenshot](Screenshots/login.png) | ![Dashboard Screenshot](Screenshots/dashboard.png) |

## 📂 Project Structure

* `library_app.py` - Main application code.
* `Library_Report.csv` - Sample exported data.
* `requirements.txt` - Project dependencies.
* `README.md` - Project documentation.

## 📄 License
This project is open-source and available under the MIT License.
