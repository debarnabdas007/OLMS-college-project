from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------- DATABASE CONNECTION ----------
def get_db():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------- CREATE TABLES ----------
def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        quantity INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        user_type TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user_id INTEGER,
        status TEXT,
        FOREIGN KEY(book_id) REFERENCES books(book_id),
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------- BOOK MODULE ----------
@app.route("/books", methods=["GET", "POST"])
def books():
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        quantity = int(request.form["quantity"])

        # Check if book already exists
        cur.execute(
        "SELECT * FROM books WHERE title=? AND author=?",
        (title, author)
        )
        existing_book = cur.fetchone()

        if existing_book:
        # Update quantity
            cur.execute(
            "UPDATE books SET quantity = quantity + ? WHERE book_id=?",
            (quantity, existing_book["book_id"])
            )
        else:
        # Insert new book
            cur.execute(
            "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
            (title, author, quantity)
            )

        conn.commit()

    # This runs for BOTH GET and POST
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    conn.close()
    return render_template("books.html", books=books)

@app.route("/delete_book/<int:id>")
def delete_book(id):
    conn = get_db()
    conn.execute("DELETE FROM books WHERE book_id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/books")

# ---------- USER MODULE ----------
@app.route("/users", methods=["GET", "POST"])
def users():
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        cur.execute(
            "INSERT INTO users (name, user_type) VALUES (?, ?)",
            (request.form["name"], request.form["type"])
        )
        conn.commit()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()
    return render_template("users.html", users=users)

# ---------- ISSUE / RETURN MODULE ----------
@app.route("/issue", methods=["GET", "POST"])
def issue():
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        book_id = request.form["book_id"]
        user_id = request.form["user_id"]

        cur.execute("SELECT quantity FROM books WHERE book_id=?", (book_id,))
        book = cur.fetchone()

        if book and book["quantity"] > 0:
            cur.execute("INSERT INTO transactions (book_id, user_id, status) VALUES (?, ?, 'ISSUED')",
                        (book_id, user_id))
            cur.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id=?", (book_id,))
            conn.commit()

    cur.execute("""
    SELECT t.txn_id, b.title, u.name, t.status
    FROM transactions t
    JOIN books b ON t.book_id = b.book_id
    JOIN users u ON t.user_id = u.user_id
    """)
    txns = cur.fetchall()

    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    conn.close()
    return render_template("issue.html", txns=txns, books=books, users=users)

@app.route("/")
def home():
    return redirect("/books")



#--------- RETURN BOOK MODULE -------------

@app.route("/return/<int:txn_id>")
def return_book(txn_id):
    conn = get_db()
    cur = conn.cursor()

    # Get book_id from transaction
    cur.execute(
        "SELECT book_id FROM transactions WHERE txn_id=?",
        (txn_id,)
    )
    txn = cur.fetchone()

    if txn:
        book_id = txn["book_id"]

        # Update transaction status
        cur.execute(
            "UPDATE transactions SET status='RETURNED' WHERE txn_id=?",
            (txn_id,)
        )

        # Increase book quantity
        cur.execute(
            "UPDATE books SET quantity = quantity + 1 WHERE book_id=?",
            (book_id,)
        )

        conn.commit()

    conn.close()
    return redirect("/issue")




if __name__ == "__main__":
    app.run(debug=True)
