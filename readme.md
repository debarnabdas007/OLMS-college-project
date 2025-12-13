# Online Library Management System (OLMS)

## Description
The OLMS is a web-based centralized library management system built with Python, Flask, HTML/CSS, and SQLite.  
It allows librarians to manage books, users, and book issue/return operations efficiently.  

## Features
- Add, view, and delete books
- Add and view users
- Issue books to users
- View transactions
- Centralized database with SQLite
- Simple web interface (HTML + CSS)
- Beginner-friendly Flask backend

## Technology Stack
- Python 3.x
- Flask
- SQLite
- HTML / CSS

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