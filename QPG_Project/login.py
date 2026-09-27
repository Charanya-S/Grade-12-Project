from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as mys


def forgot_pass():
    def change_pass():
        if usernameEntry.get()=='' or newpass_Entry.get()==''or newconfirm_Entry.get()=='':
          messagebox.showerror("ERROR","All Fields Are Required!",parent=window)
        elif newpass_Entry.get() != newconfirm_Entry.get():
           messagebox.showerror("ERROR","Password & confirm password are not matched!",parent=window)
        else:
            try:
                con=mys.connect(host='localhost', user='root', password='')
                mycursor=con.cursor()
            except:
              messagebox.showerror("ERROR",'Connection is not done,            PLEASE TRY AGAIN!!')
              return
            query='use userdata'
            mycursor.execute(query)
            query='select * from data where username=%s'
            mycursor.execute(query,(usernameEntry.get(),))
            row=mycursor.fetchone()
            
            if row ==None:
                messagebox.showerror("ERROR",'Incorrect username!',parent=window)
            else:
        
             try:
                con=mys.connect(host='localhost', user='root', password='')
                mycursor=con.cursor()
             except:
                messagebox.showerror("ERROR",'Connection is not done,            PLEASE TRY AGAIN!!')
                return
             query='use userdata'
             mycursor.execute(query)
             query='update  data set password =%s where username=%s'
             mycursor.execute(query,(newpass_Entry.get(),usernameEntry.get()))
             con.commit()
             con.close()
             messagebox.showinfo("SUCCESS",'Password is reset! Please Login! :)',parent=window)
             window.destroy()


    #making window
    window=Toplevel()
    window.title('Change Password')   
    #background
    background=ImageTk.PhotoImage(file='forgetpassword.png')
    bgLabel=Label(window,image=background)
    bgLabel.grid()
    #frame
    frame=Frame(window,bg='lawn green')
    frame.place(x=950,y=100)
    #making label
    heading=Label(frame,text='RESET PASSWORD',font=('Carlito',13,'bold'),bg='lawn green',fg='black')
    heading.grid(row=0,column=0,padx=10,pady=10)
    #usernamelabel
    usernameLabel=Label(frame,text='Username:',font=('Carlito',10,'bold'),bg='lawn green',fg='black')
    usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
    #username entry
    usernameEntry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='lawn green',fg='black')
    usernameEntry.grid(row=4,column=0,sticky='w',padx=25)
    #password label
    passwordLabel=Label(frame,text=' New Password:',font=('Carlito',10,'bold'),bg='lawn green',fg='black')
    passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
    #  new password entry
    newpass_Entry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='lawn green',fg='black')
    newpass_Entry.grid(row=6,column=0,sticky='w',padx=25)
    # confirm label
    confirmLabel=Label(frame,text='Confirm Password',font=('Carlito',10,'bold'),bg='lawn green',fg='black')
    confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
    #confirm entry
    newconfirm_Entry=Entry(frame,width=25,font=('Carlito',10,'bold'),bg='lawn green',fg='black')
    newconfirm_Entry.grid(row=8,column=0,sticky='w',padx=25)
    #submitbutton
    submitbutton=Button(frame,text='Submit',font=('Carlito',14,'bold'),bd=0,bg='lawn green',fg='black',activebackground='lawn green',activeforeground='black',command=change_pass)
    submitbutton.grid(row=10,column=0,pady=10)

    window.mainloop()


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("ERROR","All Fields Are Required!")
    else:
        try:
            con=mys.connect(host='localhost', user='root', password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror("ERROR",'Connection is not done,            PLEASE TRY AGAIN!!')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get(),))
        row=mycursor.fetchone()
        if row ==None:
            messagebox.showerror("ERROR",'Incorrect username or password!')
        else:
             messagebox.showinfo("WELCOME",'login is successful :)')
             login_window.destroy()
             import QPG

def user_enter(event):
    if usernameEntry.get()=='Username': 
        usernameEntry.delete(0,END)

def password_enter(event):
       if passwordEntry.get()=='Password':
           passwordEntry.delete(0,END)

def hide():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='closeEye.png')
    passwordEntry.config(show='')
    eyebutton.config(command=hide)
def signup_page():
    login_window.destroy()
    import signup

login_window=Tk()
login_window.title('Login')
background=ImageTk.PhotoImage(file='login.png')
bgLabel=Label(login_window,image=background)
bgLabel.grid()

#frame
frame=Frame(login_window,bg='cornflowerblue')
frame.place(x=950,y=100)
#making label
heading=Label(frame,text='Login into Your Account',font=('Carlito',13,'bold'),bg='cornflowerblue',fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)

#for username
usernameEntry=Entry(frame,width=25,font=('Carlito',12,'bold'),bd=0,fg='navy')
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
usernameEntry.grid(row=1,column=0,sticky='w',padx=25,pady=(10,2))

#Password
passwordEntry=Entry(frame,width=25,font=('Carlito',12,'bold'),bd=0,fg='navy',show='*')
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)
passwordEntry.grid(row=2,column=0,sticky='w',padx=25,pady=(10,2))

#closeeyebutton
openeye=PhotoImage(file='openeye.png')
eyebutton=Button(frame,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=show)
eyebutton.place(x=225,y=87)

#forget password
forgetbutton=Button(frame,text='Forgot Password',highlightbackground='cornflowerblue',bd=0,bg='cornflowerblue',activebackground='cornflowerblue',cursor='hand2',font=('Carlito',9,'bold'),fg='white',activeforeground='white',command=forgot_pass)
forgetbutton.grid(row=3,sticky='e',padx=24)

#login button
loginbutton=Button(frame,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='cornflowerblue',activeforeground='cornflowerblue',activebackground='white',cursor='hand2',width=17,bd=0,command=login_user)
loginbutton.grid(row=4,column=0,sticky='w',padx=25,pady=(12))

#createaccount button
newaccountbutton=Button(frame,text='Dont have an account? Create One',font=('Open Sans',8,'bold underline'),bg='cornflowerblue',fg='black',cursor='hand2',bd=0,highlightbackground='cornflowerblue',activeforeground='white',activebackground='cornflowerblue',width=35)
newaccountbutton.grid(row=5,column=0,pady=(15))
# signup button
SignupButton=Button(frame,text='Signup',font=('Carlito',10,'bold'),bg='cornflowerblue',fg='black',activebackground='cornflowerblue',activeforeground='black',command=signup_page)
SignupButton.grid(row=6,column=0,padx=(1,1),pady=1)



login_window.mainloop()
