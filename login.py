import tkinter as tk
from tkinter import *
from customtkinter import *
from tkinter import messagebox
import customtkinter as ct

import sqlite3


conn = sqlite3.connect("project.db")
print("Database Created Successfully.")
BLACK = "#303030"
YELLOW = "#EBD671"
BLUE = "#4D96FF"
FONT = ("Helvetica", 16)

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")


# conn.execute("""
# CREATE TABLE USER(USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT  NULL,
# USERNAME TEXT NOT NULL,
# PASSWORD TEXT NOT NULL)
# """)
# print("table created")

def login_logic():
    uname = username_entry.get()
    password = password_entry.get()
    print("...")
    if uname == '' or password == '':
        messagebox.askokcancel("fields cannot be empty")
    else:
        conn = sqlite3.connect("project.db")
        cursor = conn.execute(
            "SELECT * FROM USER WHERE USERNAME ='%s'AND PASSWORD ='%s'" % (uname, password))
        if cursor.fetchone():
            messagebox.askokcancel(title="Login Success",
                                   message="YOUR LOGIN IS SUCCESSFULL")
            login.destroy()
            import main

        else:
            messagebox.askokcancel("Wrong username or password")


def register_logic():
    uname = username_entry.get()
    password = password_entry.get()
    conn.execute('INSERT INTO USER(USERNAME,PASSWORD)VALUES (?,?)',
                 (uname, password))
    conn.commit()
    print("records inserted successfully")
    conn.close()
    messagebox.askokcancel(title="Registration", message="account created")
    register.destroy()


def register():
    global register
    register = Tk()
    register.title("Register")
    register.config(padx=40, pady=40, bg=BLACK)
    global username_entry
    global password_entry
    mainframe = Frame(
        master=register, width=400, corner_radius=12, height=400)
    mainframe.grid(row=0, column=0, padx=10, pady=10)

    username_label = Label(
        mainframe, text="Username or Email address", text_color="white", text_font=FONT)
    username_label.grid(row=0, column=0, padx=10, pady=10)

    username_entry = tk.StringVar()
    username_entry = Entry(
        mainframe, width=250, height=40, corner_radius=15, text_font=FONT, border_width=2, border_color=BLUE)
    username_entry.configure(highlightthickness=0)
    username_entry.grid(row=1, column=0, padx=10, pady=5)

    password_label = Label(
        mainframe, text="Password", text_color="white", text_font=FONT)
    password_label.grid(row=3, column=0, padx=10, pady=10)

    password_entry = tk.StringVar()
    password_entry = Entry(
        mainframe, width=250, height=40, corner_radius=15, border_width=2, border_color=BLUE, text_font=FONT)
    password_entry.configure(highlightthickness=0)
    password_entry.grid(row=4, column=0, padx=10, pady=10)

    signin_button = Button(
        mainframe, text="SIGN UP ", width=250, hover_color="green", fg_color="#238636", text_font=FONT, text_color="white", command=register_logic)
    signin_button.grid(row=5, column=0, pady=20, padx=20)

    register.mainloop()


def login_form():
    global login
    login = Tk()
    login.title("Login")
    login.config(height=300, width=300, bg=BLACK)
    global message
    global username_entry
    global password_entry

    # frame1 = ct.CTkFrame(width=600, height=600, corner_radius=10)
    # frame1.grid(row=0, column=0, padx=5, pady=5)

    

    # frame2 = ct.CTkFrame(width=450, height=800, corner_radius=10)
    # frame2.grid(row=0, column=1, padx=5, pady=5)

    mainframe = Frame(
        master=login, width=440, corner_radius=15, height=450,bg_color=BLACK)
    mainframe.grid(row=0, column=0, padx=10, pady=20)

    secondframe = Frame(
        master= login,width = 500, height= 450,corner_radius=15,bg_color=BLACK
    )
    secondframe.grid(row=0, column=1, padx=10, pady=10)

    canvas = Canvas(master=secondframe, height=450, width=350,bg=BLACK,highlightthickness =0)
    first_image = PhotoImage(file="images/image2.png")
    canvas.create_image(190,230,image=first_image)
    canvas.grid(row=0, column=0)

    welcome = Label(
        mainframe, text="Welcome to CoviMate", width=340, height=40, fg_color="red", font=FONT, text_color="white")
    welcome.grid(row=0, column=0, pady=15, padx=20)

    username_label = Label(
        mainframe, text="Username or Email address", font=FONT, text_color="white")
    username_label.grid(row=1, column=0, padx=10, pady=12)

    username_entry = Entry(
        mainframe, width=250, height=40, corner_radius=15, font=FONT, border_width=2, border_color=BLUE)
    username_entry.configure(highlightthickness=0)
    username_entry.grid(row=2, column=0, padx=10, pady=5)

    password_label = Label(
        mainframe, text="Password", text_font=FONT, text_color="white")
    password_label.grid(row=3, column=0, padx=10, pady=5)

    password_entry = Entry(
        mainframe, width=250, height=40, corner_radius=15, text_font=FONT, border_width=2, border_color=BLUE, show="*")
    password_entry.configure(highlightthickness=0)
    password_entry.grid(row=4, column=0, padx=10, pady=10)

    signin_button = Button(
        mainframe, text="Sign in ", width=150, height=35,corner_radius=15, text_font=FONT, hover_color="green", fg_color="#238636", text_color="white", command=login_logic)
    signin_button.grid(row=5, column=0, pady=10, padx=10)

    labelling = Label(
        master=mainframe, text="New to Covimate", text_font=FONT, text_color="white")
    labelling.grid(row=6, column=0, padx=10, pady=10)

    create_new_account_button = Button(
        mainframe, text="Create new Account", width=250, height=35, text_font=FONT, hover_color="green", fg_color="#238636", text_color="white", command=register)
    create_new_account_button.grid(row=7, column=0, pady=10)

    # frame3 = ct.CTkFrame(width=400, height=600, corner_radius=10)
    # frame3.grid(row=0, column=2, padx=5, pady=5)
    login.mainloop()


login_form()

