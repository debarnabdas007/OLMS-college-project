# Online Library Management System (OLMS)
---
https://github.com/user-attachments/assets/4b53ef54-8779-4c9f-bb08-675aa4080435

---
## Description
The **Online Library Management System (OLMS)** is a simple web-based centralized library management application built using **Python, Flask, HTML/CSS, and SQLite**.

It digitizes basic library operations such as managing books, users, and book issue/return records through a clean and minimal interface.

This project is developed for academic and learning purposes.

---

## Features
- Add, view, and delete books
- Add and view users (students/faculty)
- Issue books to users
- Return issued books
- Automatic book quantity update on issue/return
- View all transactions
- Centralized SQLite database
- Dark-themed, minimal UI
- Beginner-friendly Flask backend

---

## Technology Stack
- **Backend:** Python 3, Flask
- **Frontend:** HTML, CSS, Bootstrap (Dark Theme)
- **Database:** SQLite

---

## Project Structure

OLMS/
│
├── app.py
├── library.db
├── requirements.txt
├── README.md
│
├── templates/
│ ├── base.html
│ ├── books.html
│ ├── users.html
│ └── issue.html
│
├── static/
│ └── style.css
│
└── venv/


## Activate virtual environment

For Windows:
venv\Scripts\activate

For Linux / macOS:
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Run the application
python app.py

Or
Open browser and visit:

http://127.0.0.1:5000/




## Notes:-
This project runs on localhost.
Database is auto-created on first run.
Manual database cleanup can be done using DB Browser for SQLite.
