import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL)
""")

conn.commit()

# CREATE
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student added successfully."
    )

    clear_fields()
    display_students()

# READ
def display_students():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        tree.insert("", tk.END, values=student)

# UPDATE
def update_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student to update."
        )
        return

    student_id = tree.item(selected[0000])["values"][0000]

    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
        name=str(name)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number.Name should be in String Form"
        )
        return

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, course = ?
        WHERE id = ?
    """, (name, age, course, student_id))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student updated successfully."
    )

    clear_fields()
    display_students()

# DELETE
def delete_students():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student to delete."
        )
        return

    student_id = tree.item(selected[0000])["values"][0000]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )
        conn.commit()
        messagebox.showinfo(
            "Success",
            "Student deleted successfully."
        )

        clear_fields()
        display_students()
# CLEAR INPUTS
def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

# SELECT STUDENT
def select_student(event):
    selected = tree.selection()

    if selected:
        student = tree.item(selected[0])["values"]

        clear_fields()
        name_entry.insert(0, student[1])
        age_entry.insert(0, student[2])
        course_entry.insert(0, student[3])

root = tk.Tk()
root.title("student Management System")
root.geometry("700x500")

title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

#NAME
tk.Label(
    input_frame,
    text="Name:"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

#AGE
tk.Label(
    input_frame,
    text="Age:"
).grid(row=1, column=0, padx=5, pady=5)

age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=1, padx=5, pady=5)

#COURSE
tk.Label(
    input_frame,
    text="Course:"
).grid(row=2, column=0, padx=5, pady=5)

course_entry = tk.Entry(input_frame, width=30)
course_entry.grid(row=2, column=1, padx=5, pady=5)

#BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text = "Add",
    width = 10,
    command=add_student
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text = "Update",
    width = 10,
    command=update_student
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text = "Delete",
    width = 10,
    command=delete_students
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text = "Clear",
    width = 10,
    command=clear_fields
).grid(row=0, column=3, padx=5)

#TABLE
tree = ttk.Treeview(
    root,
    columns=("ID", "Name", "Age", "Course"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")

tree.column("ID", width=50)
tree.column("Name", width=200)
tree.column("Age", width=80)
tree.column("Course", width=100)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

#GUI

root = tk.Tk()
root.title("Student Management System")
root.geometry("700x550")
root.configure(bg="#EAF4FB")

# COLORS

BG_COLOR = "#EAF4FB"
TITLE_COLOR = "#154360"
LABEL_COLOR = "#1F618D"
ENTRY_BG = "#FFFFFF"
ADD_COLOR = "#27AE60"
UPDATE_COLOR = "#F39C12"
DELETE_COLOR = "#E74C3C"
CLEAR_COLOR = "#7F8C8D"
BUTTON_TEXT = "white"

# TITLE

title_label = tk.Label(
 root,
 text="Student Management System",
 font=("Arial", 20, "bold"),
 bg=BG_COLOR,
 fg=TITLE_COLOR
)
title_label.pack(pady=15)

# INPUT FRAME

input_frame = tk.Frame(
 root,
 bg="white",
 bd=2,
 relief="groove"
)
input_frame.pack(
 pady=5,
 padx=20,
 fill="x"
)

# NAME

tk.Label(
 input_frame,
 text="Name:",
 font=("Arial", 11, "bold"),
 bg="white",
 fg=LABEL_COLOR
).grid( row=0,
 column=0,
 padx=10,
 pady=8,
 sticky="e"
)
name_entry = tk.Entry(
 input_frame,
 width=35,
 font=("Arial", 11),
 bg=ENTRY_BG,
 fg="#212121",
 relief="solid",
 bd=1
)
name_entry.grid(
 row=0,
 column=1,
 padx=10,
 pady=8
)

# AGE

tk.Label(
 input_frame,
 text="Age:",
 font=("Arial", 11, "bold"),
 bg="white",
 fg=LABEL_COLOR
).grid(
 row=1,
 column=0,
 padx=10,
 pady=8,
 sticky="e"
)
age_entry = tk.Entry(
 input_frame,
 width=35,
 font=("Arial", 11),
 bg=ENTRY_BG,
 fg="#212121",
 relief="solid",
 bd=1
)
age_entry.grid(
 row=1,
 column=1,
 padx=10,
 pady=8
)

# COURSE

tk.Label(
 input_frame,
 text="Course:",
 font=("Arial", 11, "bold"),
 bg="white",
 fg=LABEL_COLOR
).grid(
 row=2,
 column=0,
 padx=10,
 pady=8,
 sticky="e"
)

course_entry = tk.Entry(
 input_frame,
 width=35,
 font=("Arial", 11),
 bg=ENTRY_BG,
 fg="#212121",
 relief="solid",
 bd=1
)
course_entry.grid(
 row=2,
 column=1,
 padx=10,
 pady=8
)

# BUTTON FRAME

button_frame = tk.Frame(
 root,
 bg=BG_COLOR )
button_frame.pack(pady=15)

# ADD BUTTON

tk.Button(
 button_frame,
 text="Add",
 width=12,
 font=("Arial", 10, "bold"),
 bg=ADD_COLOR,
 fg=BUTTON_TEXT,
 activebackground="#1E8449",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=add_student
).grid(
 row=0,
 column=0,
 padx=5
)
# UPDATE BUTTON

tk.Button(
 button_frame,
 text="Update",
 width=12,
 font=("Arial", 10, "bold"),
 bg=UPDATE_COLOR,
 fg=BUTTON_TEXT,
 activebackground="#D68910",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=update_student
).grid(
 row=0,
 column=1,
 padx=5
)

# DELETE BUTTON

tk.Button(
 button_frame,
 text="Delete",
 width=12,
 font=("Arial", 10, "bold"),
 bg=DELETE_COLOR, fg=BUTTON_TEXT,
 activebackground="#C0392B",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=delete_students
).grid(
 row=0,
 column=2,
 padx=5
)

# CLEAR BUTTON

tk.Button(
 button_frame,
 text="Clear",
 width=12,
 font=("Arial", 10, "bold"),
 bg=CLEAR_COLOR,
 fg=BUTTON_TEXT,
 activebackground="#626567",
 activeforeground="green",
 relief="flat",
 cursor="hand2",
 command=clear_fields ).grid(
 row=0,
 column=3,
 padx=5
)

# TREEVIEW STYLE

style = ttk.Style()
style.theme_use("clam")

# Table heading

style.configure(
 "Treeview.Heading",
 background="#1F618D",
 foreground="white",
 font=("Arial", 10, "bold"),
 padding=8
)
# Table body
style.configure( "Treeview",
 background="white",
 foreground="#212121",
 rowheight=30,
 fieldbackground="white",
 font=("Arial", 10)
)
# Selected row

style.map(
 "Treeview",
 background=[
 ("selected", "#5DADE2")
 ],
 foreground=[
 ("selected", "white")
 ]
)

# TABLE

tree = ttk.Treeview(
 root, columns=("ID", "Name", "Age", "Course"),
 show="headings"
)
tree.heading(
 "ID",
 text="ID"
)
tree.heading(
 "Name",
 text="Name"
)
tree.heading(
 "Age",
 text="Age"
)
tree.heading(
 "Course",
 text="Course"
)
# Column widths

tree.column(
 "ID",
 width=60,
 anchor="center"
)
tree.column(
 "Name",
 width=200
)
tree.column(
 "Age",
 width=80,
 anchor="center"
)
tree.column(
 "Course",
 width=220
)
# Alternating row colors

tree.tag_configure(
 "evenrow", background="#F4F9FC"
)
tree.tag_configure(
 "oddrow",
 background="#D6EAF8"
)
tree.pack(
 fill="both",
 expand=True,
 padx=20,
 pady=10
)

# SELECT EVENT

tree.bind(
 "<<TreeviewSelect>>",
 select_student
)

# DISPLAY EXISTING RECORDS

display_students()

# START APPLICATION

root.mainloop()

# CLOSE DATABASE

conn.close()
