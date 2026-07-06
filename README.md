# 🏦 Bank Management System

🌐 **Live App:** [https://bank-management7.streamlit.app](https://bank-management7.streamlit.app)

---

## 📌 About

A simple **Bank Management System** built in Python while learning Object-Oriented Programming (OOP) concepts. It supports basic banking operations like creating accounts, depositing/withdrawing money, and managing user details.

A **Streamlit web frontend** was added on top to make it usable through a browser instead of the terminal.

---

## ✨ Features

- 📝 **Create Account** — Register a new bank account with name, age, email, and a 4-digit PIN
- 💰 **Deposit Money** — Add funds to your account (max ₹10,000 per transaction)
- 🏧 **Withdraw Money** — Withdraw funds (checks for sufficient balance)
- 👁️ **View Account** — See your account details (with optional PIN reveal)
- ✏️ **Update Account** — Change your name, email, or PIN
- 🗑️ **Delete Account** — Permanently delete your bank account

---

## 🗂️ Project Structure

```
Bank_Management/
│
├── main.py        # Original OOP code (CLI-based, uses input())
├── main2.py       # Same logic adapted for import (used by app.py)
├── app.py         # Streamlit frontend
├── .gitignore     # Excludes data.json, venv, pycache
└── README.md      # This file
```

> **Note:** `data.json` (where account data is stored) is excluded from the repo via `.gitignore` as it may contain sensitive information like PINs.

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/madhavsingla944/Bank_Management.git
cd Bank_Management
```

### 2. Install dependencies
```bash
pip install streamlit
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3 |
| OOP | Classes, class methods, static methods |
| Data Storage | JSON file (`data.json`) |
| Frontend | Streamlit |
| Deployment | Streamlit Community Cloud |

---

## 📚 Concepts Practised

- Object-Oriented Programming (OOP)
- Python Classes and Methods
- File I/O with JSON
- Building a simple web UI with Streamlit
- Deploying a Python app online

---

## ⚠️ Limitations

- Data is stored in a local `data.json` file (not a real database)
- No session management or proper authentication
- Built for learning purposes only — not production-ready
