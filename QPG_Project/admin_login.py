import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Username and Password Check
def check():
     te=username.get()
     pe=password.get()
     if (te=='user') and (pe=='pass'):

     #Successfully logged in message box
         messagebox.showinfo('Welcome',"You have successfully logged in")
         root.destroy()
         
         #Importing next page
         import admin_page

     #Enter correctly message box    
     else:
          messagebox.showinfo("Invalid Details", "Enter the correct username and password")
         
#Create main window
root = tk.Tk()
root.geometry("300x320")
root.resizable(False,False)
bg=PhotoImage(file='loginbg.png')
label1=Label(root,image=bg)
label1.place(x=0,y=0)
root.title('Login')
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=3)

#Create username label and text box for entering username
username = tk.Label(root, text="Username:",bg='#3D66D0',fg='white')
username.place(relx =1 , x =-300, y = 205)
username = tk.Entry(root)
username.place(relx =1 , x =-240, y = 205,width=190,height=20)

#Create password label and text box for entering password
password= tk.Label(root, text="Password:",bg='#3D66D0',fg='white')
password.place(relx =1 , x =-300, y = 270)
password = tk.Entry(root,  show="*")
password.place(relx =1 , x =-240, y = 270,width=190,height=22)

#Create the login button
login_button = tk.Button(root, text="Login",command=check,bg='#3D66D0',fg='white')
login_button.place(relx =1 , x =-173, y = 150)

#Close button
button=Button(root,text="❌",command=root.destroy,bg='#3D66D0',fg='white')
button.place(relx =1 , x =-26, y = 2)

#Run the main loop
root.mainloop()
