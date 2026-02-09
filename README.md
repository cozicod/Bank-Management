# 🏦 Bank Management System (Flask)

A simple **Bank Management Web Application** built using **Python (Flask)** and **Bootstrap**.  
This project is created for learning backend development concepts and building real-world CRUD functionality.

---

## 📌 Project Overview

This application allows users to perform basic banking operations such as:
- Creating a bank account
- Depositing money
- Withdrawing money
- Viewing account details
- Updating account information
- Deleting an account

All data is stored persistently using a **JSON file**, making it easy to understand data handling without using a database.

---

## 🚀 Features

- Account creation with validation
- Deposit and withdrawal with balance checks
- Update user details (name, email, PIN)
- Delete account functionality
- Flash messages for success and error handling
- Clean UI using Bootstrap 5
- Beginner-friendly project structure

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, Bootstrap 5  
- **Data Storage:** JSON file  

---

## 📂 Project Structure
```base
Bank-App/
│
├── app.py
├── bank.py
├── data.json
├── templates/
│ ├── index.html
│ ├── create.html
│ ├── deposit.html
│ ├── withdraw.html
│ ├── details.html
│ ├── update.html
│ ├── delete.html
│ └── navbar.html
│
├── static/
│ └── (optional CSS / assets)
│
└── README.md
```
