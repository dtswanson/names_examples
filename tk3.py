import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from cryptography.fernet import Fernet

# Generate and store the encryption key (run only once, then save the key)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Original student data (now used to populate the encrypted database)
student_names = [
    ['Owen', 10, 100], ['Oliver', 9, 100], ['Mrs. Swanson', 11, 83],
    ['Mr. Swanson', 12, 82], ['Doug', 12, 22], ['Mr. Kurbis', 12, 73],
    ['Dr. Petry', 12, 59], ['Scott', 9, 42], ['Ms. Berkman', 12, 53],
    ['Mr. Collier', 12, 84]
]


# Encrypting and decrypting functions
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode()).decode()


def decrypt_data(data):
    return cipher_suite.decrypt(data.encode()).decode()


# Setup encrypted databases
def setup_databases():
    # Create login database
    conn_login = sqlite3.connect("encrypted_login.db")
    cursor_login = conn_login.cursor()
    cursor_login.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    ''')
    conn_login.commit()
    conn_login.close()

    # Create student scores database
    conn_scores = sqlite3.connect("encrypted_student_data.db")
    cursor_scores = conn_scores.cursor()
    cursor_scores.execute('''
        CREATE TABLE IF NOT EXISTS students (
            name TEXT,
            grade TEXT,
            score TEXT
        )
    ''')
    # Insert all student data, encrypted
    for name, grade, score in student_names:
        cursor_scores.execute("INSERT INTO students (name, grade, score) VALUES (?, ?, ?)",
                              (encrypt_data(name), encrypt_data(str(grade)), encrypt_data(str(score))))
    conn_scores.commit()
    conn_scores.close()


# Function to validate login with encrypted database
def validate(username, password):
    conn = sqlite3.connect("encrypted_login.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (encrypt_data(username), encrypt_data(password)))
    result = cursor.fetchone()
    conn.close()
    return result is not None


# Function to register a new user in encrypted login database
def signup(username, password):
    conn = sqlite3.connect("encrypted_login.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   (encrypt_data(username), encrypt_data(password)))
    conn.commit()
    conn.close()


# GUI classes (keeping original code structure with modifications for encrypted database)

class LoginPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x200")
        self.title("Login")

        # Username and Password fields
        tk.Label(self, text="Username").pack(pady=5)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="Password").pack(pady=5)
        self.entry_pw = tk.Entry(self, show="*")
        self.entry_pw.pack()

        # Login and Register buttons
        login_btn = ttk.Button(self, text="Login", command=self.get_login)
        login_btn.pack(pady=5)

        register_btn = ttk.Button(self, text="Register", command=self.get_signup)
        register_btn.pack()

    def get_login(self):
        username = self.entry_user.get()
        password = self.entry_pw.get()
        if validate(username, password):
            tk.messagebox.showinfo("Login Successful", f"Welcome {username}")
        else:
            tk.messagebox.showerror("Login Failed", "Incorrect Username or Password")

    def get_signup(self):
        SignupPage()


class SignupPage(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("400x200")
        self.title("Register")

        # Username and Password fields
        tk.Label(self, text="New Username").pack(pady=5)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="New Password").pack(pady=5)
        self.entry_pw = tk.Entry(self, show="*")
        self.entry_pw.pack()

        # Create Account button
        register_btn = ttk.Button(self, text="Create Account", command=self.signup)
        register_btn.pack(pady=5)

    def signup(self):
        username = self.entry_user.get()
        password = self.entry_pw.get()
        signup(username, password)
        tk.messagebox.showinfo("Account Created", "Account successfully created.")
        self.destroy()


class StudentScoresPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x400")
        self.title("Student Scores")

        # Frame for student scores
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview for displaying data
        self.tree = ttk.Treeview(frame, columns=("Name", "Grade", "Score"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Grade", text="Grade")
        self.tree.heading("Score", text="Score")
        self.tree.pack(fill="both", expand=True)

        # Load data
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("encrypted_student_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        encrypted_data = cursor.fetchall()
        conn.close()

        # Decrypt each row and insert into the Treeview
        for name, grade, score in encrypted_data:
            self.tree.insert("", "end", values=(decrypt_data(name), decrypt_data(grade), decrypt_data(score)))


# Setup databases and launch the main pages
setup_databases()

# Launch the login and student scores pages
LoginPage().mainloop()
StudentScoresPage().mainloop()
