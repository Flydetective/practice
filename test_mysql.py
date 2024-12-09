import tkinter
from tkinter import messagebox
import mysql.connector

# MySQL connection setup
con = mysql.connector.connect(host="localhost", user="root", password="Faheem18!")
cur = con.cursor(buffered=True)

# Database and table setup
try:
    cur.execute("USE registration")
except:
    cur.execute("CREATE DATABASE registration")
    cur.execute("USE registration")

try:
    cur.execute("DESCRIBE persons")
except:
    cur.execute("""
        CREATE TABLE persons (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(20),
            age INT(3),
            gender VARCHAR(6),
            email VARCHAR(30) UNIQUE,
            mobile VARCHAR(15)
        )
    """)

# Function to handle registration
def Registration():
    try:
        # Attempt to insert the data into the table
        cur.execute(
            "INSERT INTO persons (name, age, gender, email, mobile) "
            "VALUES (%s, %s, %s, %s, %s)",
            (e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
        )
        con.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except mysql.connector.IntegrityError as e:
        # Handle duplicate email error
        if "Duplicate entry" in str(e) and "email" in str(e):
            messagebox.showerror("Error", "This email is already registered. Please enter another email ID.")
        else:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Tkinter GUI setup
win = tkinter.Tk()
win.geometry("500x500")
win.title("Person Registration Portal")

l1 = tkinter.Label(win, text="Person Details")
l2 = tkinter.Label(win, text="Name")
l3 = tkinter.Label(win, text="Age")
l4 = tkinter.Label(win, text="Gender")
l5 = tkinter.Label(win, text="Email")
l6 = tkinter.Label(win, text="Mobile Number")
l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=5, column=1)
l6.grid(row=6, column=1)

e1 = tkinter.Entry(win)
e2 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e4 = tkinter.Entry(win)
e5 = tkinter.Entry(win)
e1.grid(row=2, column=2)
e2.grid(row=3, column=2)
e3.grid(row=4, column=2)
e4.grid(row=5, column=2)
e5.grid(row=6, column=2)

b = tkinter.Button(win, text="Submit Here", command=Registration)
b.grid(row=7, column=2)

# Close MySQL connection when the window is closed
def on_close():
    cur.close()
    con.close()
    win.destroy()

win.protocol("WM_DELETE_WINDOW", on_close)
win.mainloop()


