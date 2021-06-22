from tkinter import *
from tkinter import messagebox
import tkinter
import mysql.connector as mysql
import sys
import os
global root

db = mysql.connect(host="localhost",user = "root",passwd="pass",database="testedatabase")
db_cursor = db.cursor(buffered=True)
 #===============================================================================
class Windowstart:
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("350x450")
        self.root.iconbitmap('Medical-Management/icone.ico')
        self.root.resizable(0, 0)
 #===============================================================================
        self.label1 = Label(root, text='Welcome !',font='Helvetica 20 ',fg="#ECF0F1",bg="#2c2f33")
        self.label1.place(x=5,y=35, width=340 ,height=70)
        self.label2 = Label(root, text='Clinical Profile Management',font='Helvetica 14 '
                    ,fg="#D0D3D4",bg="#2c2f33")
        self.label2.place(x=5,y=80, width=340 ,height=50)
        self.label3 = Label(root, text='All work by mr-p-oliveira(⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#23272a").place(x=0,y=440, width=350 ,height=10)
        
        self.frame = LabelFrame(root, text='Log-in Area',fg="#99aab5",bg="#2c2f33")
        self.frame.place(x=5,y=180, width=340 ,height=120)
        
        self.b = Button(self.frame, text='Sign in', width=20 ,height=2,command=self.log_sign)
        self.b.pack(side=TOP, pady=5)
        self.b2= Button(self.frame, text='Log in', width=20 ,height=2,command=self.log_win)
        self.b2.pack()
        
        self.exi = Button(root, text='Exit', font='Helvetica 8',command=self.ExitApp,pady=3)
        self.exi.place(x=125,y=400, width=100 ,height=25)
 #===============================================================================        
    def log_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Window2(self.newWindow)
    
    def log_sign(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Window3(self.newWindow)
        
    def ExitApp(self):
        self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
        if self.ExitApp == 'yes':
            self.root.destroy()
            sys.exit(0)
        else:
            messagebox.showinfo('Return','You will now return to the application screen')
        
class Window2:
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal- Log in")
        self.root.geometry("350x450")
        self.root.iconbitmap('Medical-Management/icone.ico')
        self.root.resizable(0, 0)
        self.nome  = StringVar()
        self.passp = StringVar()
 #====================================================================================================        
        self.label1 = Label(root, text='Log-in',font='Helvetica 20 bold',fg="#ECF0F1",bg="#2c2f33")
        self.label1.place(x=5,y=35, width=340 ,height=70)
    
        self.label3 = Label(root, text='All work by mr-p-oliveira(⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#23272a")
        self.label3.place(x=0,y=440, width=350 ,height=10)
        self.frame = LabelFrame(root,bg="#2c2f33")
        self.frame.place(x=5,y=150, width=340 ,height=135)  
 #====================================================================================================  
        self.name = Label(self.frame,text ='Username',font='Helvetica 13 bold',fg="white",bg="#2c2f33")
        self.name.pack(side=TOP, pady=2)        
        self.name = Entry(self.frame,text ='Username',textvariable=self.nome,font='Helvetica 13',justify='center')
        self.name.pack(side=TOP, pady=2)

        self.passw = Label(self.frame,text ='Password',font='Helvetica 13 bold',fg="white",bg="#2c2f33")
        self.passw.pack(side=TOP, pady=2)        
        self.passw = Entry(self.frame,text ='Password',textvariable=self.passp,font='Helvetica 13',show='*',justify='center')
        self.passw.pack(side=TOP, pady=2)

        
        self.ent = Button(root, text='Enter', width=10 ,height=1,command=self.login).place(x=90,y=300)
        self.bck = Button(root, text='Back', width=10 ,height=1,command=self.back_win).place(x=175, y=300)
        
        self.exi = Button(root, text='Exit', font='Helvetica 8',command=self.ExitApp,pady=3)
        self.exi.place(x=125,y=400, width=100 ,height=25)
 #====================================================================================================  
    def login(self):
        db.connect()
        nome = self.nome.get()
        passp = self.passp.get()
            
        if nome == "" or passp =="":
            messagebox.showinfo('Information','Please Fill All Fields')
        else:
            T1 ="SELECT EXISTS(SELECT * FROM testedatabase.log WHERE nome = %s AND password = %s) "
            var=(nome,passp)
            db_cursor.execute(T1,var)
            result = db_cursor.fetchone()
            for row  in result:
                if row == 1:
                    messagebox.showinfo('Welcome','Log-in successful ' + str(nome))
                    os.system('python mainframe.py')
                    root.destroy()
                    sys.exit(0)
                else:
                    messagebox.showinfo('Information','The name or password is wrong !')
            db.close()
            
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windowstart(self.newWindow)     
        
    def ExitApp(self):
        self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
        if self.ExitApp == 'yes':
            root.destroy()
        else:
            tkinter.messagebox.showinfo('Return','You will now return to the application screen')
            
class Window3:
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal- Log in")
        self.root.geometry("350x450")
        self.root.iconbitmap('Medical-Management/icone.ico')
        self.root.resizable(0, 0)      
        self.nome  = StringVar()
        self.passp = StringVar()
        self.role  = StringVar()
 #===================================================================================
        self.label1 = Label(root, text='Sign-in',font='Helvetica 20 bold',fg="#ECF0F1",bg="#2c2f33")
        self.label1.place(x=5,y=35, width=340 ,height=70)
        self.label3 = Label(root, text='All work by mr-p-oliveira(⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#23272a")
        self.label3.place(x=0,y=440, width=350 ,height=10)
        self.frame = LabelFrame(root,bg="#2c2f33")
        self.frame.place(x=62,y=150, width=225 ,height=105)  
 #===================================================================================
        self.name = Label(self.frame,font='Helvetica 13 bold',text='Name',fg="white",bg="#2c2f33",pady=5,padx=3).grid(row=0)
        self.name = Entry(self.frame,textvariable=self.nome, justify='center').grid(row=0,column=2)
        
        self.passw = Label(self.frame,font='Helvetica 13 bold',text='Pass',fg="white",bg="#2c2f33",pady=5,padx=3).grid(row=1)
        self.passw = Entry(self.frame,textvariable=self.passp , show='*',justify='center').grid(row=1,column=2)

        choices = {'Admin','Supervisor','Employee'}
        self.role.set('Employee')
        self.DrpMenu = Label(self.frame,font='Helvetica 13 bold',fg="white",bg="#2c2f33",padx=5,pady=5).grid(row=2)
        self.DrpMenu = OptionMenu(self.frame, self.role, *choices).grid(row=2,column=2)

        self.ent = Button(root, text='Register', width=10 ,height=1,command=self.register).place(x=90,y=290)
        self.bck = Button(root, text='Back', width=10 ,height=1,command=self.back_win).place(x=175, y=290)
        
        self.exi = Button(root, text='Exit', font='Helvetica 8',command=self.ExitApp,pady=3)
        self.exi.place(x=125,y=400, width=100 ,height=25)
 #===================================================================================
    def register(self):
        db.connect()
        nome = self.nome.get()
        passp = self.passp.get()
        role = self.role.get()
        
        if nome == "" or passp =="":
            messagebox.showinfo('Information','Please Fill All Fields')
        else:
            query1 = "INSERT INTO log (nome, password, role ) VALUES (%s, %s, %s)"
            val = (nome,passp,role)
            db_cursor.execute(query1,val)
            db.commit()
            messagebox.showinfo('Information','Registration successful ' + str(nome))
            self.back_win()
            db.close()
            
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windowstart(self.newWindow)      

    def ExitApp(self):
        self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
        if self.ExitApp == 'yes':
            root.destroy()
        else:
            messagebox.showinfo('Return','You will now return to the application screen')           


 
if __name__ == "__main__": 
    root = Tk()
    app = Windowstart(root)
    root.mainloop()
