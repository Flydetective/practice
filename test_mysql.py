import tkinter
import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="Faheem18!")
cur=con.cursor(buffered=True)

try:
   cur.execute("use registration")
except:
    cur.execute("create database registration")
    cur.execute("use registration")

try:
    cur.execute("describe persons")
except:    
    cur.execute("create table persons( id int primary key auto_increment, name varchar(20), age int, gender varchar(6), email varchar(30), mobile varchar(15))")
    
def Registration():
    cur.execute(f"insert into persons(name, age, gender, email, mobile) values ('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}')")
    con.commit()
win=tkinter.Tk()
win.geometry("500x500")
win.title("Person registeration portal")
l1=tkinter.Label(win, text="Person details")
l2=tkinter.Label(win, text="Name")
l3=tkinter.Label(win, text="Age")
l4=tkinter.Label(win, text="Gender")
l5=tkinter.Label(win, text="Email")
l6=tkinter.Label(win, text="Mobile Number")
l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=5, column=1)
l6.grid(row=6, column=1)
e1=tkinter.Entry(win)
e2=tkinter.Entry(win)
e3=tkinter.Entry(win)
e4=tkinter.Entry(win)
e5=tkinter.Entry(win)
e1.grid(row=2, column=2)
e2.grid(row=3, column=2)
e3.grid(row=4, column=2)
e4.grid(row=5, column=2)
e5.grid(row=6, column=2)
b=tkinter.Button(win, text="Submit Here", command=Registration)
b.grid(row=7, column=2)
win.mainloop()
