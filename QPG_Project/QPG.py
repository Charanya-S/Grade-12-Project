import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql_connector
from fpdf import FPDF

#Connect to Database
def connect_to_db():
    return mysql_connector.connect(host='localhost',
                                   user='root',
                                   passwd='',
                                   database='')

#Fetching Classes from DB
def load_classes():
    myconn=connect_to_db()
    mycursor=myconn.cursor()
    q="select distinct Class from Questions"
    mycursor.execute(q)
    classes=[row[0] for row in mycursor.fetchall()]
    myconn.close()

    classes=["Select Class"]+classes
    menu=class_dropdown["menu"]
    menu.delete(0, "end")
    for c in classes:
        menu.add_command(label=c, command=lambda value=c: selected_class.set(value))
    selected_class.set("Select Class")    
    load_subjects()

#Fetching Subjects from DB
def load_subjects(*args):
    current_class=selected_class.get()
    menu = subject_dropdown["menu"]
    menu.delete(0, "end")
    
    if current_class=="Select Class":
        selected_subject.set("Select Subject")
        load_questions()
        return

    myconn=connect_to_db()
    mycursor=myconn.cursor()
    q1="select distinct Subject from Questions where class=%s"
    mycursor.execute(q1,(current_class,))
    subjects=[row[0] for row in mycursor.fetchall()]
    myconn.close()

    subjects=["Select Subject"]+subjects
    for s in subjects:
        menu.add_command(label=s, command=lambda value=s: selected_subject.set(value))
    selected_subject.set("Select Subject")
    load_questions()

#Fetching Marks from DB
def load_marks(*args):
    current_class = selected_class.get()
    current_subject = selected_subject.get()
    menu = marks_dropdown["menu"]
    menu.delete(0, "end")
    selected_marks.set("Select Marks")

    if current_class == "Select Class" or current_subject == "Select Subject":
        load_questions()
        return

    myconn = connect_to_db()
    mycursor = myconn.cursor()
    q = "select distinct Marks from Questions where Class=%s and Subject=%s"
    mycursor.execute(q, (current_class, current_subject))
    marks_list = [row[0] for row in mycursor.fetchall()]
    myconn.close()

    marks_list = ["Select Marks"] + [str(m) for m in marks_list]
    for m in marks_list:
        menu.add_command(label=m, command=lambda value=m: selected_marks.set(value))
    selected_marks.set("Select Marks")
    load_questions()

#Fetching Questions from DB
def load_questions(*args):
    current_class = selected_class.get()
    current_subject = selected_subject.get()
    current_marks = selected_marks.get()

    menu = question_dropdown["menu"]
    menu.delete(0, "end")
    selected_question.set("Select Question")

    if (current_class == "Select Class" or 
        current_subject == "Select Subject" or 
        current_marks == "Select Marks"):
        return

    myconn = connect_to_db()
    mycursor = myconn.cursor()
    q2 = "select Question from Questions where Class=%s and Subject=%s and Marks=%s"
    mycursor.execute(q2, (current_class, current_subject, current_marks))
    questions = [row[0] for row in mycursor.fetchall()]
    myconn.close()

    questions = ["Select Question"] + questions
    for q in questions:
        menu.add_command(label=q, command=lambda value=q: on_question_selected(value))

#Adding Questions to Text Box
def on_question_selected(question):
    
    selected_question.set(question)
    
    if question != "Select Question":
        myconn = connect_to_db()
        mycursor = myconn.cursor()
        q = "select Marks from Questions where Question=%s"
        mycursor.execute(q, (question,))
        mark = mycursor.fetchone()[0]
        myconn.close()
        
        added_questions = selected_questions_textbox.get("1.0", tk.END)
        
        if question in added_questions:
            messagebox.showerror("Error!!", "Duplicte Question")
            
        else:
            selected_questions_textbox.insert(tk.END, f"{question} ({mark} Marks)\n")

#Generate PDF
def generate_pdf():
    global c
    content = selected_questions_textbox.get("1.0", tk.END).strip()
    if not content:
        messagebox.showerror("Error", "No questions to generate PDF")
        return

    chosen_class = selected_class.get()
    chosen_subject = selected_subject.get()
    entered_time = time_entry_textbox.get().strip()

    if not entered_time:
        messagebox.showerror("Error!!", "Please Enter Time")
        return #return to prevent pdf from generating even after error 
    
    #Total marks
    total_marks = 0
    for line in content.split("\n"):
        if "(" in line and "Marks" in line:
            try:
                marks = line.split("(")
                marks = marks[-1]
                marks = marks.split("Marks")
                marks = marks[0]
                marks = marks.strip()
                marks = int(marks)
                total_marks = total_marks + marks
            except:
                pass

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    #Heading
    pdf.cell(0, 10, txt="FREEDOM INTERNATIONAL SCHOOL", ln=1, align='C')
    pdf.cell(0, 10, txt="CLASS TEST", ln=1, align='C')
    pdf.cell(0, 10, txt=f"{chosen_class}", ln=1, align='C')
    pdf.cell(0, 10, txt=f"{chosen_subject}", ln=1, align='C')
    pdf.cell(0, 10, txt=f"MARKS:{total_marks}                                                                                                                            TIME:{entered_time}", ln=1, align='C')

    #Questions
    questions = content.split("\n")
    c = 1
    for q in questions:
        q = q.strip()
        if q != "":
            pdf.multi_cell(0, 10, f"Q{c}) {q}", align="L")
            c=c+1

    pdf.ln(5)
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, txt='********** ALL THE BEST **********', ln=1, align='C')
    
    pdf.output("Question Paper.pdf")
    messagebox.showinfo("Success", "PDF Successfully Generated!")

    #Reset
    selected_class.set("Select Class")
    selected_subject.set("Select Subject")
    selected_question.set("Select Question")
    selected_marks.set("Select Marks")
    selected_questions_textbox.delete("1.0", tk.END)
    time_entry_textbox.delete(0, tk.END)
    c = 0


#Tkinter Setup
root = tk.Tk()
root.title("Question Paper Generator")
root.geometry("700x600")
root.configure(bg="#ADD8E6")

#Styling
label_font = ("Comic Sans MS", 12, "bold")
button_font = ("Comic Sans MS", 12, "bold")
dropdown_font = ("Comic Sans MS", 12)
textbox_font = ("Comic Sans MS", 12)

#Dropdown Frame (for class, subject, marks)
dropdown_frame = tk.Frame(root, bg="#ADD8E6")
dropdown_frame.pack(pady=10)

#Class Dropdown
tk.Label(dropdown_frame, text="Class:", bg="#ADD8E6", font=label_font).pack(side="left", padx=5)
selected_class = tk.StringVar(root)
class_dropdown = tk.OptionMenu(dropdown_frame, selected_class, "")
class_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
class_dropdown.pack(side="left", padx=5)
selected_class.trace("w", load_subjects)

#Subject Dropdown
tk.Label(dropdown_frame, text="Subject:", bg="#ADD8E6", font=label_font).pack(side="left", padx=5)
selected_subject = tk.StringVar(root)
subject_dropdown = tk.OptionMenu(dropdown_frame, selected_subject, "")
subject_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
subject_dropdown.pack(side="left", padx=5)
selected_subject.trace("w", load_marks)

#Marks Dropdown
tk.Label(dropdown_frame, text="Marks:", bg="#ADD8E6", font=label_font).pack(side="left", padx=5)
selected_marks = tk.StringVar(root)
marks_dropdown = tk.OptionMenu(dropdown_frame, selected_marks, "")
marks_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
marks_dropdown.pack(side="left", padx=5)
selected_marks.trace("w", load_questions)

#Questions Dropdown
tk.Label(root, text="Select Questions:", bg="#ADD8E6", font=label_font).pack(pady=5)
selected_question = tk.StringVar(root)
question_dropdown = tk.OptionMenu(root, selected_question, "")
question_dropdown.config(highlightbackground="#ADD8E6", font=dropdown_font)
question_dropdown.pack(pady=5)

#Questions Text Box
tk.Label(root, text="Selected Questions:", bg="#ADD8E6", font=label_font).pack(pady=5)
selected_questions_textbox = tk.Text(root, height=12, width=70)
selected_questions_textbox.pack(pady=5)

#Enter Time Text Box
tk.Label(root, text="Time:", bg="#ADD8E6", font=label_font).pack(pady=5)
time_entry_textbox = tk.Entry(root, width=20, font=textbox_font)
time_entry_textbox.pack(pady=5)

#Generate PDF Button
generate_pdf_button = tk.Button(root, text="Save as PDF", command=generate_pdf, bg="green", fg="white", font=button_font)
generate_pdf_button.pack(pady=10)

#Logout Button
exit_button = tk.Button(root, text="Exit", bg="#D9534F", fg="white", font=button_font, command=root.destroy)
exit_button.pack(pady=10)


#Counter
c=0

#Load classes at start
load_classes()

root.mainloop()
