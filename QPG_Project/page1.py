from tkinter import *
#from PIL import ImageTk

#Create main window
welcome = Tk()
welcome.title('Question Paper Generator')
bg=PhotoImage(file="welcome.png")
label1=Label(welcome,image=bg)
label1.grid()
f = ("Times bold", 14)

#Importing next page
def logPage():
    welcome.destroy()
    import login
def ad_page():
    welcome.destroy()
    import admin_login
    
#Create USER LOGIN Button   
Button(
    welcome, 
    text="USER LOGIN", 
    font=f,
    bg='#92A2D5',
    command=logPage
    ).place(relx =1 , x =-1000, y =435)

#Create  ADMIN LOGIN Button   
Button(
    welcome, 
    text="ADMIN LOGIN", 
    font=f,
    bg='#92A2D5',
    command=ad_page
    ).place(relx =1 , x =-1000, y =495)

#Run the main loop
welcome.mainloop()
