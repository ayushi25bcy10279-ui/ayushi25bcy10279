# 📘 Event Management System

A simple, interactive **Streamlit-based Event Manager** with CRUD operations, date search, and budget trend analytics.

---

## 📌 **Overview**

This project is a lightweight **Event Management System** built using Python, Streamlit, SQLite, and Matplotlib.
Users can:

* Add events
* View all events
* Update event details
* Delete events
* Search events by date
* Visualize monthly budget trends

All event data is stored in a local SQLite database (`events.db`).

---

## 🧩 **Project Structure**

```
├── app.py               → Main Streamlit application
├── database.py          → Database connection + CRUD operations
├── utils.py             → Helper utilities (search by date)
├── analytics.py         → Budget trend visualization
├── events.db            → SQLite database file
```

---

## 🛠 **Features**

### ✔ Add New Events

Users can add events with ID, name, organizer, type, budget, and date.

### ✔ View Events

Displays all stored events in a neat table.

### ✔ Search by Date

Find events occurring on a selected date.

### ✔ Update Events

Modify any event field dynamically.

### ✔ Delete Events

Remove unwanted records.

### ✔ Monthly Analytics

Plots monthly total budget trends using Matplotlib
(from **analytics.py** )

---

## 📂 **File Descriptions**

### **1. app.py** – Main Application

Handles the UI, menu navigation, and connects all modules.
Uses Streamlit for an interactive interface.


---

### **2. database.py** – Database Handler

* Connects to SQLite
* Creates event table
* Implements Add, View, Update, Delete operations


---

### **3. utils.py** – Helper Functions

Contains `search_by_date()` used for date-based filtering.


---

### **4. analytics.py** – Data Visualization

Generates the “Monthly Budget Trend” line chart using Matplotlib.


---

## 🚀 **How to Run the Project**

### **1️⃣ Install Dependencies**

```bash
pip install streamlit pandas matplotlib
```

### **2️⃣ Run Streamlit App**

```bash
streamlit run app.py
```

### **3️⃣ The app opens on:**

`http://localhost:8501`

---

## 📊 **Database**

The project uses a lightweight SQLite database (`events.db`) created automatically by `database.py`.

---

## 🔮 **Future Enhancements**

* Event reminders via email
* Export reports to PDF
* Add attendee management
* Add authentication for organizers
* Dashboard with advanced analytics

Licence - Open source
Author - Ayushi Sharma
---

Lic
