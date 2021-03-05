from tkinter import *
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkcalendar import DateEntry 
from tkinter import messagebox
import tkinter
import mysql.connector as mysql
import time
global root

db = mysql.connect(host="localhost",user = "root",passwd="kilmyPME1",database="testedatabase")
db_cursor = db.cursor(buffered=True)
#=============================================================================================================
class Window1:
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)
 #=============================================================================================================        
        self.frame_left = Frame(root, width=260, height=720, bg="#23272a")
        self.frame_left.place(x=0,y=0)
        
        self.clck = Label(root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label3.place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label2.place(x=260 ,y=700, width=960, height=22)
        
        self.label = Label(root, text='Main navigation',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124")
        self.label.place(x=0,y=87,width=260,height=13)
        db.connect()
        db_cursor.execute('SELECT * FROM pat_reg')
        rows = len(db_cursor.fetchall())
        db.close()
        self.info_1 = Label(root,text=" Medical Records ",font='Helvetica 16 bold',fg="white",bg="red").place(x=300, y=87,width=205)
        self.info_11 = Label(root,text=rows,font='Helvetica 40 bold ',fg="white",bg="red").place(x=300, y=116,width=205,height=85)
 #=============================================================================================================
        self.lf_btn = Button(root,text="New",command=self.new_win ,font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn.place(x=0,y=100,width=260,height=55)
        self.lf_btn.bind("<Enter>", self.on_enter)
        self.lf_btn.bind("<Leave>", self.on_leave)

        self.lf_btn2 = Button(root,text="View",command=self.view_win,font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn2.place(x=0,y=155,width=260,height=55)
        self.lf_btn2.bind("<Enter>", self.on_enter)
        self.lf_btn2.bind("<Leave>", self.on_leave)
               
        self.lf_btn3 = Button(root,text="Search",command=self.search_win,font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn3.place(x=0,y=210,width=260,height=55)
        self.lf_btn3.bind("<Enter>", self.on_enter)
        self.lf_btn3.bind("<Leave>", self.on_leave)
                
        self.lf_btn4 = Button(root,text="Edit",command=self.edit_win,font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn4.place(x=0,y=265,width=260,height=55)
        self.lf_btn4.bind("<Enter>", self.on_enter)
        self.lf_btn4.bind("<Leave>", self.on_leave)
        
        self.lf_btn5 = Button(root,text="Help",font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn5.place(x=0,y=550,width=260,height=55)
        self.lf_btn5.bind("<Enter>", self.on_enter)
        self.lf_btn5.bind("<Leave>", self.on_leave)
        self.but_ex = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#1e2124",relief='flat',command=self.ExitApp)
        self.but_ex.place(x=1150,y=700)     
 #============================================================================================================== 
    def on_enter(self,e):
         e.widget['background'] = '#005042'

    def on_leave(self,e):
         e.widget['background'] = '#1e2124'
 #=============================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
   
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock)
        
    def new_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windnew(self.newWindow)
        
    def view_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windview(self.newWindow)

    def search_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windsearch(self.newWindow)  
   
    def edit_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = WindEdit(self.newWindow)
 #=============================================================================================================
class Windnew:
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)
 #=============================================================================================================
 #===========================================  Variables  =====================================================
        self.name_nw  = StringVar()
        self.lasname_nw = StringVar()
        self.gend_nw = StringVar()
        self.birth_nw = StringVar()
        self.adress_nw = StringVar()
        self.city_nw = StringVar()
        self.zipcod_nw = StringVar()
        self.phone_nw = StringVar()
        self.email_nw = StringVar()
        self.sscnumber_nw = StringVar()
        self.nhsnumber_nw = IntVar()
        self.blood_nw = StringVar()
        self.martial_nw = StringVar()
        self.height_nw = DoubleVar()
        self.weight_nw = DoubleVar()
        self.allerg_nw = StringVar()
        self.doctor_nw = StringVar()
 #=============================================================================================================        
        self.frame_left = Frame(self.root, width=260, height=720, bg="#23272a")
        self.frame_left.place(x=0,y=0)
        
        self.clck = Label(self.root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label3.place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label2.place(x=260 ,y=700, width=960, height=22)
        
        self.label = Label(root, text='Selected',font='Helvetica 8',
                        fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
        
        self.frame = LabelFrame(root, text=' New Register ',fg="white",bg="#2c2f33")
        self.frame.place(x=295,y=70, width=890 ,height=215)
        
        self.frame2 = LabelFrame(root, text=' Information ',fg="white",bg="#2c2f33")
        self.frame2.place(x=295,y=295, width=890 ,height=185)
        
        self.frame3 = LabelFrame(root, text=' Medic Assign ',fg="white",bg="#2c2f33")
        self.frame3.place(x=295,y=495, width=890 ,height=90)
 #======================================================================================================================
        self.lf_lbl = Label(root,text="New",font='Helvetica 12',fg="white", bg="#005042").place(x=0,y=100,width=260,height=55)
        
        self.reg_btn = Button(root,text="Register",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.register_form).place(x=920,y=650)

        self.bck_btn = Button(root,text="Back",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.back_win).place(x=1050,y=650)      
        
        self.but_ex = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#2c2f33",relief='flat',command=self.ExitApp).place(x=1150,y=700)
 #======================================================================================================================= 
 #============================================= Frame 1 =================================================================
        self.nw_name = Label(root,text="First Name",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=100) 
        self.nw_namee = Entry(root,justify='center',font='Helvetica 11',textvariable=self.name_nw).place(x=445,y=100)
        
        self.lasname  = Label(root,text="Last Name",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=650,y=100) 
        self.lasnamee  = Entry(root,justify='center',font='Helvetica 11',textvariable=self.lasname_nw).place(x=745,y=100)
        
        self.sex =  Label(root,text="Gender",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=135) 
        gender = ("Male", "Female", "Transgender","Non-binary/non-conforming")
        self.gender = Combobox(root, values= gender,font='Helvetica 11',width=18,textvariable=self.gend_nw,justify='center').place(x=445,y=135)
        
        self.calen = Label(root,text="Birthdate",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=650 , y=135)
        self.cal = DateEntry(root, width=18, year= 1995, background='black', foreground='white', 
                             borderwidth=2,cursor="hand1",justify='center',date_pattern='yyyy-mm-dd',font='Helvetica 11',textvariable=self.birth_nw).place(x=745,y=135)
        
        self.adress = Label(root,text="Adress",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=170) 
        self.adresse = Entry(root,font='Helvetica 11',textvariable=self.adress_nw,justify='left',width=45).place(x=445,y=170)    
        
        self.city = Label(root,text="City",font='Helvetica 11',fg="white", bg="#2c2f33",width=5).place(x=815,y=170) 
        self.citye = Entry(root,font='Helvetica 11',justify='left',textvariable=self.city_nw,width=10).place(x=875,y=170)
        
        self.pstcod = Label(root,text="Zip Code",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=205)
        self.pstcode = Entry (root,font='Helvetica 11',justify='center',textvariable=self.zipcod_nw,width=10).place(x=445,y=205)
        
        self.cell = Label(root,text="Phone",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=560,y=205)
        self.celle  = Entry(root,justify='center',font='Helvetica 11',textvariable=self.phone_nw,width=15).place(x=620,y=205)  
        
        self.emal = Label(root,text="E-Mail",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=240)
        self.emaile= Entry(root,justify='center',font='Helvetica 11',textvariable=self.email_nw,width=37).place(x=445,y=240)
 #=======================================================================================================================
 #============================================= Frame 2 =================================================================
        self.socinum = Label(root,text="Social Sec number",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=307,y=330)
        self.socinume = Entry(root,justify='center',font='Helvetica 11',textvariable=self.sscnumber_nw).place(x=445,y=330)

        self.nhsnum = Label(root,text="NHS number",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=650,y=330)
        self.nhsnume = Entry(root,justify='center',font='Helvetica 11',textvariable=self.nhsnumber_nw).place(x=745,y=330)

        blood = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        self.bloodtyp = Label(root,text="Blood type",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=365)
        self.bloodtype = Combobox(root, values= blood,font='Helvetica 11',width=5,justify='center',textvariable=self.blood_nw).place(x=445,y=365)
        
        martial =("Single", "Married", "Widowed", "Divorced", "Separated") 
        self.mart = Label(root,text="Martial Status",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=650,y=365)
        self.marte = Combobox(root, values= martial,font='Helvetica 11',width=9,justify='center',textvariable=self.martial_nw).place(x=745,y=365)

        self.weight = Label(root,text="Weight",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=400)
        self.weighte = Entry(root,justify='center',font='Helvetica 11',width=6,textvariable=self.weight_nw).place(x=445,y=400)

        self.height = Label(root,text="Height",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=530,y=400)
        self.heighte = Entry(root,justify='center',font='Helvetica 11',width=6,textvariable=self.height_nw).place(x=590,y=400)
        
        self.warn = Label(root,text="Medication Allergy or Other Allergies",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=307,y=435)
        self.choi_nw = StringVar() 
        self.choi_nw.set('Yes')
        self.ys =Radiobutton(root, text="Yes" ,variable = self.choi_nw,value='Yes',font='Helvetica 11').place(x=560,y=434)
        self.nnn =Radiobutton(root, text="No", variable = self.choi_nw,value='No',font='Helvetica 11').place(x=615,y=434)      
 #=======================================================================================================================
 #============================================= Frame 3==================================================================
        self.med = Label(root,text=" Family Doctor ",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=350,y=535) 
        doctr= ("Dr. Dick L. Ong","Dr. B.J. Hardick","Dr. Flamen Ball","Dr. Doom","Dr. A. Paine")
        self.docter = Combobox(root, values=doctr,font='Helvetica 11',width=16,justify='center',textvariable=self.doctor_nw).place(x=465,y=535)
 #=======================================================================================================================
 #============================================  Querie ==================================================================
    def register_form(self):
        db.connect()
        firstnam = self.name_nw.get()
        lastnam  = self.lasname_nw.get()
        gender   = self.gend_nw.get() 
        birthdate= self.birth_nw.get()
        adress   = self.adress_nw.get()
        city     = self.city_nw.get()
        zipcod   = self.zipcod_nw.get()
        phone    = self.phone_nw.get()
        email    = self.email_nw.get()
        sscnumber= self.sscnumber_nw.get()
        nhsnumber= self.nhsnumber_nw.get()
        blood    = self.blood_nw.get() 
        martial  = self.martial_nw.get() 
        height   = self.height_nw.get() 
        weight   = self.weight_nw.get() 
        allerg   = self.choi_nw.get() 
        doctor   = self.doctor_nw.get()

        if firstnam == "" or lastnam == "" or gender == "" or adress == "" or city == "" or zipcod == "" or phone == "" or email == "" or sscnumber == "" or nhsnumber == "" or height == "" or weight == "":
               messagebox.showinfo('Information','Please Fill All Fields')
        else:     
         query1 = "INSERT INTO pat_reg (firstnam , lastnam , gender, birthdate, adress, city, zipcod, phone, email, sscnumber, nhsnumber, blood, martial, weight, height, allerg, doctor ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
         val = (firstnam , lastnam , gender, birthdate, adress, city, zipcod, phone, email, sscnumber, nhsnumber, blood, martial, weight, height, allerg, doctor)
         db_cursor.execute(query1,val)
         db.commit()
         messagebox.showinfo('Information','Patient Registry successful ' + str(firstnam) + " " + str(lastnam))
         self.back_win()
         db.close()
 #=======================================================================================================================       
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
           
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock)         

    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Window1(self.newWindow)     
class Windview:
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)
 #=============================================================================================================        
        self.frame_left = Frame(self.root, width=260, height=720, bg="#23272a")
        self.frame_left.place(x=0,y=0)
        
        self.clck = Label(self.root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label3.place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label2.place(x=260 ,y=700, width=960, height=22)        
        
        self.label = Label(root, text='Selected',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124")
        self.label.place(x=0,y=87,width=260,height=13)
        
        self.lf_lbl = Label(root,text="View",font='Helvetica 12',fg="white", bg="#005042").place(x=0,y=100,width=260,height=55)    
 #======================================================================================================================         
        self.but_ex = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#2c2f33",relief='flat',command=self.ExitApp).place(x=1150,y=700)
        self.bck_btn = Button(root,text="Back",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.back_win).place(x=1050,y=650)  
        self.see_btn = Button(root,text="See all",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.allreg_win).place(x=925,y=650) 
 #======================================================================================================================
        i = 0
        db.connect()
        
        self.tree = Treeview(root, columns=("NHS","Social", "Gender", "Blood", "Allergies","Phone", "Doctor"),show='headings', selectmode="extended")
        headings=('NHS','Social','Gender','Blood', 'Allergies','Phone','Doctor')
        sq2l = ("SELECT * FROM pat_reg")
        db_cursor.execute(sq2l)
        for j in range(len(headings)):
            self.tree.column(j, width=10, anchor=CENTER)
            self.tree.heading(j, text=headings[j])
        for ro in db_cursor:
            self.tree.insert('', i, text="",values=(ro[11], ro[10], ro[3], ro[12], ro[16],ro[8] ,ro[17]))
            i+=1
        self.tree.place(x=295,y=70,height=400,width=900)
        db.close()
        self.vscroll = Scrollbar(root,orient=VERTICAL,command=self.tree.yview)
        self.vscroll.place(x=1195,y=70,height=400)
        self.tree.config(yscrollcommand=self.vscroll.set)
 #=======================================================================================================================       
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
           
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock)  
        
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Window1(self.newWindow)   
        
    def allreg_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windallreg(self.newWindow)      
class Windallreg():
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)
        self.frame_left = Frame(self.root, width=260, height=720, bg="#23272a")
        self.frame_left.place(x=0,y=0)
        self.nome  = StringVar()
        self.passp = StringVar()
 #===============================================================================================================================     
        self.clck = Label(self.root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
 #==============================================================================================================================                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label3.place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124")
        self.label2.place(x=260 ,y=700, width=960, height=22)        
        
        self.label = Label(root, text='Selected',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124")
        self.label.place(x=0,y=87,width=260,height=13)
        
        self.lf_lbl = Label(root,text="View",font='Helvetica 12',fg="white", bg="#005042").place(x=0,y=100,width=260,height=55)
 #===============================================================================================================================
        self.log_lbl = Label(root,text="Confirm Log-in",font='Helvetica 19',fg="white", bg="#005042").place(x=610,y=85,width=260,height=55)
        self.but_ex = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#2c2f33",relief='flat',command=self.ExitApp).place(x=1150,y=700)
 #===============================================================================================================================
        self.fr_1 = LabelFrame(root, text=' Log-in ',fg="white",bg="#2c2f33").place(x=610,y=175,width=260,height=90)
        
        self.nm_fr = Label(root,text="User :",font='Helvetica 12',fg='white',bg="#2c2f33").place(x=625,y=200)
        self.nm_ent = Entry(root,font='Helvetica 12',width=14,justify='center',textvariable=self.nome).place(x=720,y=200)
        self.pss_fr = Label(root,text="Password :",font='Helvetica 12',fg='white',bg="#2c2f33").place(x=625,y=226)
        self.pss_ent = Entry(root,font='Helvetica 12',width=14,show='*',justify='center',textvariable=self.passp).place(x=720,y=226)   
        
        self.conf_btn = Button(root,text="Enter",command=self.login,font='Helvetica 10',fg="white", bg="#2c2f33", width=15 ,height=1).place(x=610,y=275)
        self.back_btn = Button(root,text="Back",command=self.back_win,font='Helvetica 10',fg="white", bg="#2c2f33", width=15 ,height=1).place(x=745,y=275)
 #===============================================================================================================================
    def login(self):
            db.connect()
            nome = self.nome.get()
            passp = self.passp.get()

            T1 ="SELECT EXISTS(SELECT * FROM testedatabase.log WHERE nome = %s AND password = %s) "
            var=(nome,passp)
            db_cursor.execute(T1,var)
            result = db_cursor.fetchone()
            for row  in result:
                if row == 1:
                        self.root.withdraw()
                        self.newWindow = Toplevel(self.root)
                        self.app = Windallreg2(self.newWindow) 
                else:
                    messagebox.showinfo('Information','The name or password is wrong !')
            db.close()
 #===============================================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
           
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock) 
        
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windview(self.newWindow)  
 #===============================================================================================================================
class Windallreg2():
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)       
 #=============================================================================================================        
        self.frame_left = Frame(self.root, width=260, height=720, bg="#23272a").place(x=0,y=0)
        
        self.clck = Label(self.root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)        
        
        self.label = Label(root, text='Selected',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
        
        self.lf_lbl = Label(root,text="Search",font='Helvetica 12',fg="white", bg="#005042").place(x=0,y=100,width=260,height=55)  
 #=======================================================================================================================
        i = 0
        db.connect()
        
        self.tree = Treeview(root,columns=("firstnam" , "lastnam" , "gender", "birthdate", "adress", "city", "zipcod", "phone", "email", "sscnumber", "nhsnumber", "blood", "martial","weight","height","allerg", "doctor"),show='headings', selectmode="extended")
        self.tree.place(x=295,y=70,height=450,width=900)

        headings=('First name','Last name','Gender','Birthdate','Adress','City','Zipcode', 'Phone','Email','Social','NHS','Blood','Martial status','Weight','Height','Allergies','Doctor') 
        sq2l = ("SELECT * FROM pat_reg")
        db_cursor.execute(sq2l)
        for j in range(len(headings)):
            self.tree.column(j,minwidth=100,width=120, stretch=0, anchor=CENTER)
            self.tree.heading(j,text=headings[j])
        for ro in db_cursor:
            self.tree.insert('', i, text="",values=(ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10], ro[11], ro[12], ro[13], ro[14], ro[15], ro[16], ro[17]))
            i+=1
        db.close()

        self.vscroll = Scrollbar(root,orient=VERTICAL,command=self.tree.yview)
        self.vscroll.place(x=1195,y=70,height=450)
        self.hscroll = Scrollbar(root,orient=HORIZONTAL,command=self.tree.xview)
        self.hscroll.place(x=295,y=500,width=900)

        self.tree.configure(xscrollcommand=self.hscroll.set,yscrollcommand=self.vscroll.set)
 #=======================================================================================================================         
        self.but_ex = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#2c2f33",relief='flat',command=self.ExitApp).place(x=1150,y=700)
        self.bck_btn = Button(root,text="Back",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.back_win).place(x=1050,y=650)  
 #=======================================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
           
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock)  
        
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Windview(self.newWindow)        
class Windsearch():
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)       
        self.searx = StringVar()
        self.number = StringVar()
 #=======================================================================================================================       
        self.frame_left = Frame(self.root, width=260, height=720, bg="#23272a").place(x=0,y=0)
        
        self.clck = Label(self.root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)        
        
        self.label = Label(root, text='Selected',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
        
        self.lf_lbl = Label(root,text="Search",font='Helvetica 12',fg="white", bg="#005042").place(x=0,y=100,width=260,height=55)  
        
        self.fr_1 = LabelFrame(root,fg="white",bg="#2c2f33").place(x=300,y=100,width=750,height=55)
 #=======================================================================================================================
        self.srch_lbl = Label(root,text=" Insert :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=315,y=116)
        self.srch_ent = Entry(root,font='Helvetica 12',width=16,justify='center',textvariable=self.number)
        self.srch_ent.place(x=445,y=118)
        self.types_serx = ("NHS number","SSC number")
        self.typ_cmbx = Combobox(root, values=self.types_serx,textvariable=self.searx,font='Helvetica 10',width=5,justify='center')
        self.typ_cmbx.place(x=595,y=118,width=115)
        self.typ_cmbx.current(0)
 #=======================================================================================================================  
        self.srch_btn = Button(root,text="Search",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.search_reg).place(x=770,y=115)
        self.clr_btn = Button(root,text="Clear",font='Helvetica 12',width=12,fg="white", bg="red",command=self.clear_srch_reg).place(x=900,y=115)
 #=======================================================================================================================       
        self.but_ex = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#2c2f33",relief='flat',command=self.ExitApp).place(x=1150,y=700)
        self.bck_btn = Button(root,text="Back",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.back_win).place(x=1050,y=650)  
 #=======================================================================================================================
        headings=('Last name','Gender','Birthdate','Blood','Martial status','Weight','Height','Allergies','Doctor')
        self.tree = Treeview(root,columns=("lastnam","gender", "birthdate","city","blood", "martial","weight","height","allerg","doctor"),show='headings', selectmode="extended")
        self.tree.place(x=300,y=170,height=50,width=750)
        for j in range(len(headings)):
            self.tree.column(j,minwidth=100,width=120, stretch=0, anchor=CENTER)
            self.tree.heading(j,text=headings[j])
 #=======================================================================================================================
        self.hscroll = Scrollbar(root,orient=HORIZONTAL,command=self.tree.xview)
        self.hscroll.place(x=300,y=220,width=750)
        self.tree.configure(xscrollcommand=self.hscroll.set)
 #=======================================================================================================================
    def search_reg(self):
        db.connect()
        i = 0
        type = self.searx.get()
        if type == "NHS number":
                nhsnumber = self.number.get()
                self.tree.delete(*self.tree.get_children())
                sq4l = "SELECT * FROM pat_reg WHERE nhsnumber='" + nhsnumber + "'"
                db_cursor.execute(sq4l)
                rows = db_cursor.fetchall()
                for ro in rows:
                 self.tree.insert("", 'end', text="", values=(ro[2], ro[3], ro[4], ro[12], ro[13], ro[14], ro[15], ro[16], ro[17]))
                db.close()
        else:
                sscnumber = self.number.get()
                self.tree.delete(*self.tree.get_children())
                sq5l = "SELECT * FROM pat_reg WHERE sscnumber='"+ sscnumber + "'"
                db_cursor.execute(sq5l)
                rows = db_cursor.fetchall()
                for ro in rows:
                 self.tree.insert("", 'end', text="",values=(ro[2], ro[3], ro[4], ro[12], ro[13], ro[14], ro[15], ro[16], ro[17]))
                db.close()        
    def clear_srch_reg(self):
        self.tree.delete(*self.tree.get_children())
        self.srch_ent.delete(0, 'end')
 #=======================================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
           
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock)  
        
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Window1(self.newWindow)   
class WindEdit():
    def __init__(self,root):
        self.root = root
        self.root.config(bg="#2c2f33")
        self.root.title("Portal")
        self.root.geometry("1220x720")
        self.root.iconbitmap('icone.ico')
        self.root.resizable(0, 0)       
        self.searx = StringVar()
        self.number = StringVar()
        self.city_x = StringVar()
        self.adress_x = StringVar()
        self.wei_x = StringVar()
        self.hei_x = StringVar()
        self.mart_ans = StringVar()
 #=======================================================================================================================       
        self.frame_left = Frame(self.root, width=260, height=720, bg="#23272a").place(x=0,y=0)
        
        self.clck = Label(self.root,text="",font='Helvetica 14',fg="white",bg="#1e2124")
        self.clck.place(x=0, y=20,width=260,height=30) 
        self.update_clock()
                        
        self.label3 = Label(root, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(root,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)        
        
        self.label = Label(root, text='Selected',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
        
        self.lf_lbl = Label(root,text="Edit",font='Helvetica 12',fg="white", bg="#005042").place(x=0,y=100,width=260,height=55)  
        
        self.fr_1 = LabelFrame(root,fg="white",bg="#2c2f33").place(x=300,y=100,width=750,height=55)
        self.fr_2 = LabelFrame(root,text=' Record Update ',fg="white",bg="#2c2f33").place(x=300,y=245,width=750,height=100)
 #=======================================================================================================================
        self.srch_lbl = Label(root,text=" Insert :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=315,y=116)
        self.srch_ent = Entry(root,font='Helvetica 12',width=16,justify='center',textvariable=self.number)
        self.srch_ent.place(x=445,y=118)
        self.types_serx = ("NHS number","SSC number")
        self.typ_cmbx = Combobox(root, values=self.types_serx,textvariable=self.searx,font='Helvetica 10',width=5,justify='center')
        self.typ_cmbx.place(x=595,y=118,width=115)
        self.typ_cmbx.current(0)
 #=======================================================================================================================
        self.city_lbl = Label(root,text="City :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=315,y=275)
        self.city_ent = Entry(root,width=18,font='Helvetica 10',justify='center',textvariable=self.city_x).place(x=405,y=276)
        self.adres_lbl = Label(root,text="Adress :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=303,y=305)
        self.adres_ent = Entry(root,width=18,font='Helvetica 10',justify='center',textvariable=self.adress_x).place(x=405,y=307)
        self.mart_lbl =  Label(root,text="Martial Status :",font='Helvetica 11',fg="white", bg="#2c2f33").place(x=565,y=275)
        martial =("Single", "Married", "Widowed", "Divorced", "Separated")
        self.mart_cmb = Combobox(root, values= martial,textvariable=self.mart_ans,font='Helvetica 11',width=10,justify='center')
        self.mart_cmb.place(x=675,y=275)
        self.mart_cmb.current(0)
        self.hei_lbl = Label(root,text="Height :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=572,y=305)
        self.hei_ent = Entry(root,width=14,font='Helvetica 10',justify='center',textvariable=self.hei_x).place(x=675,y=307)
        self.wei_lbl = Label(root,text="Weight :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=780,y=305)
        self.wei_etn = Entry(root,width=14,font='Helvetica 10',justify='center',textvariable=self.wei_x).place(x=880,y=307)
 #=======================================================================================================================  
        self.srch_btn = Button(root,text="Search",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.search_reg).place(x=770,y=115)
        self.clr_btn = Button(root,text="Clear",font='Helvetica 12',width=12,fg="white", bg="red",command=self.clear_srch_reg).place(x=900,y=115)
        self.updt_btn = Button(root,text="Update Record",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.update_reg).place(x=770,y=355)
        self.delet_btn = Button(root,text="Delete Record",font='Helvetica 12',width=12,fg="white", bg="red",command=self.delete_reg).place(x=900,y=355)
 #=======================================================================================================================       
        self.ex_btn = Button(root,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#2c2f33",relief='flat',command=self.ExitApp).place(x=1150,y=700)
        self.bck_btn = Button(root,text="Back",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.back_win).place(x=1050,y=650)  
 #======================================================TreeView==========================================================
        headings=('Last name','Gender','Birthdate','Blood','Martial status','Weight','Height','Allergies','Doctor')
        self.tree = Treeview(root,columns=("lastnam","gender", "birthdate","city","blood", "martial","weight","height","allerg","doctor"),show='headings', selectmode="extended")
        self.tree.place(x=300,y=170,height=50,width=750)
        for j in range(len(headings)):
            self.tree.column(j,minwidth=100,width=120, stretch=0, anchor=CENTER)
            self.tree.heading(j,text=headings[j])
        self.hscroll = Scrollbar(root,orient=HORIZONTAL,command=self.tree.xview)
        self.hscroll.place(x=300,y=220,width=750)
        self.tree.configure(xscrollcommand=self.hscroll.set)
        self.tree.bind("<Double 1>",self.click_bind)
 #=======================================================================================================================
    def search_reg(self):
        db.connect()
        i = 0
        type = self.searx.get()
        if type == "NHS number":
                self.nhsnumber = self.number.get()
                self.tree.delete(*self.tree.get_children())
                sq4l = "SELECT * FROM pat_reg WHERE nhsnumber='" + self.nhsnumber + "'"
                db_cursor.execute(sq4l)
                rows = db_cursor.fetchall()
                for ro in rows:
                 self.tree.insert("", 'end', text="", values=(ro[2], ro[3], ro[4], ro[12], ro[13], ro[14], ro[15], ro[16], ro[17]))
                db.close()
        else:
                self.sscnumber = self.number.get()
                self.tree.delete(*self.tree.get_children())
                sq5l = "SELECT * FROM pat_reg WHERE sscnumber='"+ self.sscnumber + "'"
                db_cursor.execute(sq5l)
                rows = db_cursor.fetchall()
                for ro in rows:
                 self.tree.insert("", 'end', text="",values=(ro[2], ro[3], ro[4], ro[12], ro[13], ro[14], ro[15], ro[16], ro[17]))
                db.close()        
    def clear_srch_reg(self):
        self.tree.delete(*self.tree.get_children())
        self.srch_ent.delete(0, 'end') 
        self.city_x.set(' ')
        self.adress_x.set(' ')
        self.wei_x.set(' ')
        self.hei_x.set(' ')
        
    def click_bind(self,e):
        db.connect()
        self.numb = self.number.get()
        sq6l = "SELECT * FROM pat_reg WHERE sscnumber='"+ self.numb + "' OR nhsnumber='" + self.numb + "'"
        db_cursor.execute(sq6l)
        rows = db_cursor.fetchall()
        for ro in rows:
                self.city_x.set(ro[6])
                self.adress_x.set(ro[5])
                self.wei_x.set(ro[14])
                self.hei_x.set(ro[15])
    def update_reg(self):
        city = self.city_x.get()
        adress = self.adress_x.get()
        weight = self.wei_x.get()
        height = self.hei_x.get()
        martial = self.mart_ans.get()
        if adress == "" or city == "" or height == "" or weight == "":
              messagebox.showinfo('Information','Please Fill All Fields')
        else:
         db.connect()
         sq6l = "UPDATE pat_reg set adress =%s, city=%s, weight=%s, height=%s, martial =%s WHERE sscnumber=%s OR nhsnumber=%s"
         val = (adress, city, weight, height, martial, self.numb, self.numb)
         db_cursor.execute(sq6l,val)
         db.commit()
         messagebox.showinfo('Information','Patient Record Updated')
         db.close()
         self.clear_srch_reg()
    def delete_reg(self):
        self.delet_mess = messagebox.askquestion("Confirm", "Do You Want to Delete this Record",icon = 'warning')
        if self.delet_mess == 'yes' :
                db.connect()
                sq7l = "DELETE FROM pat_reg WHERE sscnumber=%s OR nhsnumber=%s"
                val = (self.numb,self.numb)
                db_cursor.execute(sq7l,val)
                db.commit()
                db.close()
                messagebox.showinfo('Complete','Patient Record ' + str(self.numb) + ' Deleted')
                self.clear_srch_reg()
        else:
                messagebox.showinfo('Return','You will now return to the application screen')
        
            
 #=======================================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            root.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
           
    def update_clock(self):
        now = time.strftime("%d %b %Y ,%H:%M:%S")
        self.clck.configure(text=now)
        self.clck.after(1000, self.update_clock)  
        
    def back_win(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = Window1(self.newWindow)       
 #=======================================================================================================================      
if __name__ == "__main__": 
    root = Tk()
    app = Window1(root)
    root.after(1000, app.update_clock)
    root.mainloop()

    
