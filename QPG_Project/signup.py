from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as mys

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror("ERROR","All Fields Are Required!")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("ERROR","Password Mismatched!")
    elif check.get()==0:
        messagebox.showerror("ERROR","Please accept Terms & Conditions!")
   
    else:
        try:
          con=mys.connect(host='localhost', user='root', password='')
          mycursor=con.cursor()
                    
        except:
            messagebox.showerror("ERROR","Database connectivity issue,Please Try Again!")
            return
        
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data where email=%s'
        mycursor.execute(query,(emailEntry.get(),)) 
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('ERROR',"Username already exists!")
        else: 
            query='insert into data(email,username,password)values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS",'REGISTERED :)')
            clear()
            signup_window.destroy()
            import login

def login_page():
    signup_window.destroy()
    import login

signup_window=Tk()
signup_window.title('Signup Page')
background=ImageTk.PhotoImage(file='login.png')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

#frame
frame=Frame(signup_window,bg='cornflowerblue')
frame.place(x=950,y=100)
#making label
heading=Label(frame,text='CREATE AN ACCOUNT',font=('Carlito',13,'bold'),bg='cornflowerblue',fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)
#email label
emailLabel=Label(frame,text='Email:',font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
#emaillabelentry
emailEntry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)
#usernamelabel
usernameLabel=Label(frame,text='Username:',font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
#username entry
usernameEntry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)
#password label
passwordLabel=Label(frame,text='Password:',font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
#password entry
passwordEntry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)
#confirm label
confirmLabel=Label(frame,text='Confirm Password',font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
#confirm entry
confirmEntry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)
#termsandconditions
check=IntVar()
termsandconditions=Checkbutton(frame,text='     I agree to the Terms & conditions',font=('Carlito',7,'bold'),bg='cornflowerblue',fg='black',activebackground='cornflowerblue',activeforeground='black',cursor='hand2',width=37,variable=check)
termsandconditions.grid(row=9,column=0,sticky='w',padx=25,pady=10)
#signupbutton
signupbutton=Button(frame,text='Signup',font=('Carlito',14,'bold'),bd=0,bg='cornflowerblue',fg='black',activebackground='cornflowerblue',activeforeground='black',command=connect_database)
signupbutton.grid(row=10,column=0,pady=10)
#alreadyaccount
alreadyaccountLabel=Label(frame,text='Do you have an account?',font=('Carlito',9,'bold'),bg='cornflowerblue',fg='black')
alreadyaccountLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)
#loginbutton
loginButton=Button(frame,text='Login',font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black',activebackground='cornflowerblue',activeforeground='black',command=login_page)
loginButton.place(x=177,y=355)

signup_window.mainloop()
