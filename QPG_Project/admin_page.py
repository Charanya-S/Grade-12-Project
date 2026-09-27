import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql_connector

# Lists for dropdowns
classes_list = ["Select Class", "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", 
                "Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
subjects_list = ["Select Subject", "Math", "Science", "English"]
marks_list = ["Select Marks", 1, 2, 3, 4, 5, 10]

# Database Connection Function
def connect_to_db():
    return mysql_connector.connect(host='localhost',
                                   user='root',
                                   passwd='',
                                   database='')

# Add Question Function
def add_question():
    Classs = selected_class.get()
    Subject = selected_subject.get()
    Marks = selected_marks.get()
    Question = question_entry.get("1.0", tk.END).strip()

    if Classs == "Select Class" or Subject == "Select Subject" or Marks == "Select Marks" or not Question:
        messagebox.showerror("Error", "All fields are required")
        return

    #Insert command
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "insert into Questions (Class, Subject, Question, Marks) values (%s, %s, %s, %s)"
    cursor.execute(query, (Classs, Subject, Question, Marks))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Question added successfully!")

    #Reset
    selected_class.set("Select Class")
    selected_subject.set("Select Subject")
    selected_marks.set("Select Marks")
    question_entry.delete("1.0", tk.END)

#Tkinter Setup
root = tk.Tk()
root.title("Admin Page")
root.geometry("500x550")
root.configure(bg="#ADD8E6")

label_font = ("Comic Sans MS", 12, "bold")
dropdown_font = ("Comic Sans MS", 12)

#Class Dropdown
tk.Label(root, text="Class:", bg="#ADD8E6", font=label_font).pack(pady=5)
selected_class = tk.StringVar(root)
selected_class.set("Select Class")
class_dropdown = tk.OptionMenu(root, selected_class, *classes_list)
class_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
class_dropdown.pack(pady=5)

#Subject Dropdown
tk.Label(root, text="Subject:", bg="#ADD8E6", font=label_font).pack(pady=5)
selected_subject = tk.StringVar(root)
selected_subject.set("Select Subject")
subject_dropdown = tk.OptionMenu(root, selected_subject, *subjects_list)
subject_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
subject_dropdown.pack(pady=5)

#Marks Dropdown
tk.Label(root, text="Marks:", bg="#ADD8E6", font=label_font).pack(pady=5)
selected_marks = tk.StringVar(root)
selected_marks.set("Select Marks")
marks_dropdown = tk.OptionMenu(root, selected_marks, *marks_list)
marks_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
marks_dropdown.pack(pady=5)

#Question Textbox
tk.Label(root, text="Question:", bg="#ADD8E6", font=label_font).pack(pady=5)
question_entry = tk.Text(root, height=6, width=50)
question_entry.pack(pady=5)

#Add Questions Button
tk.Button(root, text="Add Question", bg="green", fg="white", font=label_font, command=add_question).pack(pady=10)

#Exit Button
tk.Button(root, text="Exit", bg="#D9534F", fg="white", font=label_font, command=root.destroy).pack(pady=5)

root.mainloop()
