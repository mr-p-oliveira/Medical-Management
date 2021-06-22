from tkinter import *
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkcalendar import DateEntry 
from tkinter import messagebox
import tkinter
import datetime
import mysql.connector as mysql
from PIL import Image, ImageTk
global beat

db = mysql.connect(host="localhost",user = "root",passwd="kilmyPME1",database="testedatabase")
db_cursor = db.cursor(buffered=True)
#=============================================================================================================
class Window_anal:
    def __init__(self,beat):
        self.beat = beat
        self.beat.config(bg="#2c2f33")
        self.beat.title("Clinical Analysis")
        self.beat.geometry("1220x720")
        self.beat.iconbitmap('Medical-Management/icone.ico')
        self.beat.resizable(0, 0)

        db.connect()
        db_cursor.execute('SELECT * FROM pat_reg')
        rows = len(db_cursor.fetchall())
        db_cursor.execute('SELECT * FROM bld_test')
        rows2 = len(db_cursor.fetchall())
        db_cursor.execute('SELECT COUNT(*) FROM testedatabase.bld_test WHERE curdate()')
        rows3 = len(db_cursor.fetchall())
        db.close()
        self.info_1 = Label(beat,text=" Medical Records ",font='Helvetica 16 bold',fg="white",bg="PaleVioletRed3").place(x=300, y=87,width=205)
        self.info_11 = Label(beat,text=rows,font='Helvetica 40 bold ',fg="white",bg="PaleVioletRed2").place(x=300, y=116,width=205,height=85)

        self.info_2 = Label(beat,text=" Blood Analysis ",font='Helvetica 16 bold',fg="white",bg="SeaGreen3").place(x=525, y=87,width=205)
        self.info_22 = Label(beat,text=rows2,font='Helvetica 40 bold ',fg="white",bg="SeaGreen2").place(x=525, y=116,width=205,height=85)
        
        self.info_3 = Label(beat,text="Today Blood  ",font='Helvetica 16 bold',fg="white",bg="SeaGreen3").place(x=750, y=87,width=205)
        self.info_33 = Label(beat,text=rows3,font='Helvetica 40 bold ',fg="white",bg="SeaGreen2").place(x=750, y=116,width=205,height=85)
 #=============================================================================================================        
        self.frame_left = Frame(beat, width=260, height=720, bg="#23272a").place(x=0,y=0)
                        
        self.label3 = Label(beat, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        
        self.label2 = Label(beat,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)
        
        self.label = Label(beat, text=' Selected ',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
 #=============================================================================================================   
        self.lf_btn = Button(beat,text="Analysis",font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat',command=self.analY_win)
        self.lf_btn.place(x=0,y=100,width=260,height=55)
        self.lf_btn.bind("<Enter>", self.on_enter)
        self.lf_btn.bind("<Leave>", self.on_leave)

        self.lf_btn2 = Button(beat,text="Medical Records",font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn2.place(x=0,y=155,width=260,height=55)
        self.lf_btn2.bind("<Enter>", self.on_enter)
        self.lf_btn2.bind("<Leave>", self.on_leave)
               
        self.lf_btn3 = Button(beat,text="Search",font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn3.place(x=0,y=210,width=260,height=55)
        self.lf_btn3.bind("<Enter>", self.on_enter)
        self.lf_btn3.bind("<Leave>", self.on_leave)
                
        self.lf_btn4 = Button(beat,text="Edit",font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn4.place(x=0,y=265,width=260,height=55)
        self.lf_btn4.bind("<Enter>", self.on_enter)
        self.lf_btn4.bind("<Leave>", self.on_leave)
        
        self.lf_btn5 = Button(beat,text="Help",font='Helvetica 12',fg="white", bg="#1e2124",activebackground='#345',relief='flat')
        self.lf_btn5.place(x=0,y=550,width=260,height=55)
        self.lf_btn5.bind("<Enter>", self.on_enter)
        self.lf_btn5.bind("<Leave>", self.on_leave)
        
        self.but_ex = Button(beat,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#1e2124",relief='flat',command=self.ExitApp)
        self.but_ex.bind("<Enter>", self.on_enter)
        self.but_ex.bind("<Leave>", self.on_leave)
        self.but_ex.place(x=1150,y=700)      
 #============================================================================================================== 
    def on_enter(self,e):
         e.widget['background'] = '#0082c8'

    def on_leave(self,e):
         e.widget['background'] = '#1e2124'  
 #=============================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            beat.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
            
    def analY_win(self):
        self.beat.withdraw()
        self.newWindow = Toplevel(self.beat)
        self.app = Window_A1(self.newWindow)
class Window_A1:
    def __init__(self,beat):
        self.beat = beat
        self.beat.config(bg="#2c2f33")
        self.beat.title("Clinical Analysis")
        self.beat.geometry("1220x720")
        self.beat.iconbitmap('Medical-Management/icone.ico')
        self.beat.resizable(0, 0)
 #=============================================================================================================        
        self.frame_left = Frame(beat, width=260, height=720, bg="#23272a").place(x=0,y=0)                   
        self.label3 = Label(beat, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        self.label2 = Label(beat,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)
        self.label = Label(beat, text=' Selected ',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
 #============================================================================================================= 
        self.lf_btn = Label(beat,text="Analysis",font='Helvetica 12',fg="white", bg="#0082c8",relief='flat')
        self.lf_btn.place(x=0,y=100,width=260,height=55)
        self.blood_btn = Button(beat,text="•    Hematology ",font='Helvetica 10',fg="white", bg="#1e2124",relief='flat',justify='center',command=self.blood_win)
        self.blood_btn.place(x=0,y=155,width=260,height=40)
        self.urine_btn = Button(beat,text="•   Urology  ",font='Helvetica 10',fg="white", bg="#1e2124",relief='flat',justify='center',command=self.blood_uri)
        self.urine_btn.place(x=0,y=195,width=260,height=40)
        self.img_btn = Button(beat,text="•  Medical Imaging ",font='Helvetica 10',fg="white", bg="#1e2124",relief='flat',justify='center',command=self.blood_im)
        self.img_btn.place(x=0,y=235,width=260,height=40)
        self.but_ex = Button(beat,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#1e2124",relief='flat',command=self.ExitApp)
        self.but_ex.place(x=1150,y=700)    
 #=============================================================================================================
    def blood_win(self):
        self.beat.withdraw()
        self.newWindow = Toplevel(self.beat)
        self.app = Window_blood(self.newWindow)
    def blood_uri(self):
        self.beat.withdraw()
        self.newWindow = Toplevel(self.beat)
        self.app = Window_urine(self.newWindow)
    def blood_im(self):
        self.beat.withdraw()
        self.newWindow = Toplevel(self.beat)
        self.app = Window_img(self.newWindow)
            
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            beat.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')         
class Window_blood:
    def __init__(self,beat):
        self.beat = beat
        self.beat.config(bg="#2c2f33")
        self.beat.title("Clinical Analysis")
        self.beat.geometry("1220x720")
        self.beat.iconbitmap('Medical-Management/icone.ico')
        self.beat.resizable(0, 0)
        self.number = StringVar()
        self.tub_num = StringVar()
        self.patoccur= StringVar()
 #============================================================================================================= 
        self.tsh_val = IntVar()
        self.t4_val = IntVar()
        self.hmb_val = IntVar()
        self.glu_val = IntVar()
        self.tri_val = IntVar()
        self.cri_val = IntVar()
        self.Total_val = IntVar()
        self.hdl_val = IntVar()
        self.ldl_val = IntVar()
        self.vldl_val = IntVar()
        self.searx = StringVar()
        self.date = StringVar()
 #============================================================================================================= 
        self.frame_left = Frame(beat, width=260, height=720, bg="#23272a").place(x=0,y=0)                 
        self.label3 = Label(beat, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        self.label2 = Label(beat,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)
        load = Image.open("Medical-Management/blod.png")
        render = ImageTk.PhotoImage(load)
        img = Label(beat, image=render)
        img.image = render
        img.place(x=0, y=0,width=260,height=95)
        self.label = Label(beat, text=' Selected ',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
 #=============================================================================================================
        self.lf_btn = Label(beat,text="Hematology",font='Helvetica 12',fg="white", bg="#0082c8",relief='flat')
        self.lf_btn.place(x=0,y=100,width=260,height=55)
        self.but_ex = Button(beat,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#1e2124",relief='flat',command=self.ExitApp)
        self.but_ex.place(x=1150,y=700)    
 #=============================================================================================================
        self.proc_lbl = Label(beat,text="Process nº :",font='Helvetica 12',fg="white", bg="#23272a",relief='flat').place(x=0,y=185,width=260,height=55)
        self.proc_inf = Label(beat,text="Empty",font='Helvetica 16',fg="red",relief='flat')
        self.proc_inf.place(x=30,y=235,width=200,height=35)
 #=============================================================================================================
        self.ent_frm = LabelFrame(beat,text="  Patient Select ",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=285,y=85,width=845,height=75)
        self.srch_lbl = Label(beat,text=" Insert :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=315,y=116)
        self.srch_ent = Entry(beat,font='Helvetica 12',width=16,justify='center',textvariable=self.number)
        self.srch_ent.place(x=445,y=118)
        self.typ_cmbx = Label(beat, text="NHS number",font='Helvetica 10',width=5)
        self.typ_cmbx.place(x=595,y=118,width=115)
        self.srch_btn = Button(beat,text="Search",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.searcx).place(x=770,y=115)
        self.clr_btn = Button(beat,text="Clear",font='Helvetica 12',width=12,fg="white", bg="red",command=self.clear_srch_reg).place(x=900,y=115)
 #=============================================================================================================
        self.cho_frm = LabelFrame(beat,text="  Select tests  ",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=285,y=165,width=845,height=195)
        self.tsh_lbl = Label(beat,text="TSH",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=195)
        self.tsh_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.tsh_val,command=self.check_val)
        self.tsh_chk.place(x=405,y=195)
        self.tsh_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disabled')
        self.tsh_ent.place(x=435,y=198,height=17,width=60)
        self.tsh_uni_lbl = Label(beat,text="mUI/L",font='System 11',fg="white",bg="#2c2f33").place(x=500,y=195)
        
        self.t4_lbl = Label(beat,text="T4 Free",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=220)
        self.t4_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.t4_val,command=self.check_val)
        self.t4_chk.place(x=405,y=220)
        self.t4_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.t4_ent.place(x=435,y=224,height=17,width=60)
        self.t4_uni_lbl = Label(beat,text="ng/dL",font='System 11',fg="white",bg="#2c2f33").place(x=500,y=220)
        
        self.hmb_lbl = Label(beat,text="Hemoglobin",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=245)
        self.hmb_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.hmb_val,command=self.check_val)
        self.hmb_chk.place(x=405,y=245)
        self.hmb_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.hmb_ent.place(x=435,y=250,height=17,width=60)
        self.hmb_uni_lbl = Label(beat,text="mmol/mol",font='System 11',fg="white",bg="#2c2f33").place(x=500,y=245)
        
        self.glu_lbl = Label(beat,text="Glucose",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=270)
        self.glu_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.glu_val,command=self.check_val)
        self.glu_chk.place(x=405,y=270)
        self.glu_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.glu_ent.place(x=435,y=276,height=17,width=60)
        self.glu_uni_lbl = Label(beat,text="mg/dL",font='System 11',fg="white",bg="#2c2f33").place(x=500,y=270)
        
        self.tri_lbl = Label(beat,text="Triglyceride",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=295)
        self.tri_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.tri_val,command=self.check_val)
        self.tri_chk.place(x=405,y=295)
        self.tri_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.tri_ent.place(x=435,y=302,height=17,width=60)
        self.tri_uni_lbl = Label(beat,text="mg/dL",font='System 11',fg="white",bg="#2c2f33").place(x=500,y=295)
        
        self.cri_lbl = Label(beat,text="Creatinine",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=320)
        self.cri_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.cri_val,command=self.check_val)
        self.cri_chk.place(x=405,y=320)
        self.cri_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.cri_ent.place(x=435,y=328,height=17,width=60)
        self.cri_uni_lbl = Label(beat,text="mg/dL",font='System 11',fg="white",bg="#2c2f33").place(x=500,y=320)
        self.lbl_lbl = Label(beat,text="Cholesterol :",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=565,y=195)
        for i in range(195, 295, 25):
              self.Total_uni_lbl = Label(beat,text="mg/dL",font='System 11',fg="white",bg="#2c2f33").place(x=810,y=i)
               
        self.Total_lbl = Label(beat,text="Total",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=665,y=195)
        self.Total_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.Total_val,command=self.check_val)
        self.Total_chk.place(x=710,y=194)
        self.Total_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.Total_ent.place(x=740,y=198,height=17,width=60)

        self.hdl_lbl = Label(beat,text="HDL",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=665,y=220)
        self.hdl_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.hdl_val,command=self.check_val)
        self.hdl_chk.place(x=710,y=219)
        self.hdl_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.hdl_ent.place(x=740,y=224,height=17,width=60)
        
        self.vldl_lbl = Label(beat,text="VLDL",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=665,y=245)
        self.vldl_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.vldl_val,command=self.check_val)
        self.vldl_chk.place(x=710,y=244)
        self.vldl_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.vldl_ent.place(x=740,y=250,height=17,width=60)
        
        self.ldl_lbl = Label(beat,text="LDL",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=665,y=270)
        self.ldl_chk = Checkbutton(beat,bg="#2c2f33",onvalue =1,offvalue=0,variable=self.ldl_val,command=self.check_val)
        self.ldl_chk.place(x=710,y=269)
        self.ldl_ent = Entry(beat,font='Helvetica 11',justify=CENTER,state='disable')
        self.ldl_ent.place(x=740,y=276,height=17,width=60)
        
        self.sele_btn = Button(beat,text="Select All",font='Helvetica 12',width=12,fg="white",bg="#005042",command=self.checkall).place(x=665,y=320)
        self.cl2r_btn = Button(beat,text="Clear all",font='Helvetica 12',width=12,fg="white", bg="red",command=self.deseall).place(x=790,y=320)
        self.reg_btn = Button(beat,text="Register",font='Helvetica 12',width=12,fg="white", bg="#2c2f33",command=self.register).place(x=915,y=320)
  #=============================================================================================================
        self.tst_frm = LabelFrame(beat,text="  Select tube  ",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=285,y=365,width=845,height=325)
        self.ref_lbl = Label(beat,text="Type :",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=315,y=395)
        self.ref_serx = ("No Additive","Clot Ativ","EDTA","Gel & Clot","Heparin")
        self.ref_cmb = Combobox(beat,values=self.ref_serx,textvariable=self.searx,font='Helvetica 10',width=11,justify='center')
        self.ref_cmb.place(x=365,y=397)
        self.ref_cmb.current(2)
        self.ref_cmb.bind("<<ComboboxSelected>>", self.colour)
        self.ref_lbl2= Label(beat,text="    ",font='Helvetica 11',bg="white")
        self.ref_lbl2.place(x=475,y=397)
        self.numb_lbl= Label(beat,text="Reff :",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=545,y=396)
        self.numb_ent= Entry(beat,font='Helvetica 11',justify=CENTER,width=15,textvariable=self.tub_num).place(x=590,y=397)
        self.numb_btn = Button(beat,text="Register",font='Helvetica 10',width=7,fg="white",bg="#005042",command=self.tube_reg).place(x=716,y=397,height=23)
  #=============================================================================================================
        headings=('Type','Tube','Reff','Data')
        self.tree = Treeview(beat,columns=("Type","Tube","Reff","Data"),show='headings',selectmode="extended")
        self.tree.place(x=315,y=435,height=220,width=765)
        for j in range(len(headings)):
          self.tree.column(j, width=10, anchor=CENTER)
          self.tree.heading(j, text=headings[j])
  #=============================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            beat.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
    def searcx(self):
           nhsnumber = self.number.get()
           db.connect()
           sq1l = "SELECT * FROM pat_reg WHERE nhsnumber='" + nhsnumber + "'"
           db_cursor.execute(sq1l)
           checknumb = db_cursor.rowcount
           if checknumb != 1:
              messagebox.showinfo('Info','No Record Found')
           else:
              self.srch_ent.configure(state='disable') 

           sql2 = "SELECT coalesce(MAX(process),0)+1 FROM bld_test WHERE nhsnumber='" + nhsnumber + "'" 
           db_cursor.execute(sql2)
           result = db_cursor.fetchall()
           for i in result:
              self.patoccur = i[0]
           self.proc_inf.configure(text=self.patoccur)
           db.close()  
    def clear_srch_reg(self):
        self.srch_ent.configure(state='normal')
        self.srch_ent.delete(0, 'end')
        self.tsh_ent.delete(0, 'end')
        self.t4_ent.delete(0, 'end')
        self.hmb_ent.delete(0, 'end')
        self.glu_ent.delete(0, 'end')
        self.tri_ent.delete(0, 'end')
        self.cri_ent.delete(0, 'end')
        self.Total_ent.delete(0, 'end')
        self.hdl_ent.delete(0, 'end')
        self.vldl_ent.delete(0, 'end')
        self.ldl_ent.delete(0, 'end')   
        self.proc_inf.configure(text="EMPTY")  
    def checkall(self):
        self.tsh_chk.select()
        self.t4_chk.select()
        self.hmb_chk.select()
        self.glu_chk.select()
        self.tri_chk.select()
        self.cri_chk.select()
        self.Total_chk.select()
        self.hdl_chk.select()
        self.vldl_chk.select()
        self.ldl_chk.select()
        self.check_val()     
    def deseall(self):
        self.clear_srch_reg()
        self.tsh_chk.deselect()
        self.t4_chk.deselect()
        self.hmb_chk.deselect()
        self.glu_chk.deselect()
        self.tri_chk.deselect()
        self.cri_chk.deselect()
        self.Total_chk.deselect()
        self.hdl_chk.deselect()
        self.vldl_chk.deselect()
        self.ldl_chk.deselect()
        self.check_val()    
    def colour(self,event=None):
        type = self.searx.get()
        if type == "No Additive" or type == "Clot Ativ":
               self.ref_lbl2["background"] = "red"
        elif type == "EDTA":
               self.ref_lbl2["background"] = "purple3"
        elif type == "Gel & Clot":
               self.ref_lbl2["background"] = "yellow"
        else:
               self.ref_lbl2["background"] = "green" 
    def register(self):
       db.connect()
       tsh = self.tsh_ent.get()
       T4 =  self.t4_ent.get()
       hmb = self.hmb_ent.get()
       glu = self.glu_ent.get()
       tri = self.tri_ent.get()
       cri = self.cri_ent.get()
       total=self.Total_ent.get()
       hdl = self.hdl_ent.get()
       vldl= self.vldl_ent.get()
       ldl=  self.ldl_ent.get()
       nhsnumber = self.number.get()
       process = self.patoccur
          
       query1 = "INSERT INTO bld_test(nhsnumber, tsh, T4, hmb, glu, tri, cri, ch_tot, ch_hdl, ch_ldl, ch_vldl, date, process) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
       val =(nhsnumber, tsh, T4, hmb, glu, tri, cri, total, hdl, ldl, vldl, date, process)
       db_cursor.execute(query1,val)
       db.commit()
       
       sqls = "SELECT firstnam,lastnam FROM pat_reg WHERE nhsnumber='" + nhsnumber + "'"
       db_cursor.execute(sqls)
       result = db_cursor.fetchall()
       for i in result:
          firstnam = i[0]
          lastnam = i[1]
       messagebox.showinfo('Information','Patient ' + str(firstnam) +" "+ str(lastnam)+" Blood Test successful")
       db.close()
    def tube_reg(self):
       db.connect()
       nhsnumber = self.number.get()
       type = self.searx.get()
       process = self.patoccur
       reff = self.tub_num.get()
       supp = reff[0:3]
       lote = reff[4:7]
       refer = reff[8:12]
 
       if supp == "180":
        supp = "MEDVac"
       elif supp == "130":
        supp = "TUBMed"
       elif supp == "241":
        supp = "VacInternational"
       else:
          messagebox.showerror('Error','Inser a valid Reference')
          
       query1 = "INSERT INTO stock_reg(type_stck, lote_stck, fornecedor_stck, reff_stck, patient, date, process) VALUES (%s, %s, %s, %s, %s, %s, %s) "
       val = (type, lote, supp, refer, nhsnumber, date, process)
       db_cursor.execute(query1,val)
       db.commit()

       self.tree.delete(*self.tree.get_children())
       sql2 = "SELECT * FROM stock_reg WHERE patient= %s AND process= %s"
       var=(nhsnumber,process)
       db_cursor.execute(sql2,var)
       rows = db_cursor.fetchall()
       for ro in rows:
         self.tree.insert("", 'end', text="", values=(ro[1],ro[3],ro[4],ro[6]))
       db.close() 
    def check_val(self):
       if self.tsh_val.get() == 1:
          self.tsh_ent.configure(state='normal')
       else:
          self.tsh_ent.configure(state='disable')
 
       if self.t4_val.get() == 1:
          self.t4_ent.configure(state='normal')
       else:
          self.t4_ent.configure(state='disable')
          
       if self.hmb_val.get() == 1:
          self.hmb_ent.configure(state='normal')
       else:
          self.hmb_ent.configure(state='disable')
          
       if self.glu_val.get() == 1:
          self.glu_ent.configure(state='normal')
       else:
          self.glu_ent.configure(state='disable')
          
       if self.tri_val.get() == 1:
          self.tri_ent.configure(state='normal')
       else:
          self.tri_ent.configure(state='disable')
          
       if self.cri_val.get() == 1:
          self.cri_ent.configure(state='normal')
       else:
          self.cri_ent.configure(state='disable')
          
       if self.Total_val.get() == 1:
          self.Total_ent.configure(state='normal')
       else:
          self.Total_ent.configure(state='disable')
          
       if self.hdl_val.get() == 1:
          self.hdl_ent.configure(state='normal')
       else:
          self.hdl_ent.configure(state='disable')
          
       if self.ldl_val.get() == 1:
          self.ldl_ent.configure(state='normal')
       else:
          self.ldl_ent.configure(state='disable')
          
       if self.vldl_val.get() == 1:
          self.vldl_ent.configure(state='normal')
       else:
          self.vldl_ent.configure(state='disable')       
class Window_urine:
    def __init__(self,beat):
        self.beat = beat
        self.beat.config(bg="#2c2f33")
        self.beat.title("Clinical Analysis")
        self.beat.geometry("1220x720")
        self.beat.iconbitmap('Medical-Management/icone.ico')
        self.beat.resizable(0, 0)
        self.number = StringVar()
 #============================================================================================================= 
        self.frame_left = Frame(beat, width=260, height=720, bg="#23272a").place(x=0,y=0)                 
        self.label3 = Label(beat, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        self.label2 = Label(beat,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)
        self.label = Label(beat, text=' Selected ',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
 #=============================================================================================================
        self.lf_btn = Label(beat,text="Urology",font='Helvetica 12',fg="white", bg="#0082c8",relief='flat')
        self.lf_btn.place(x=0,y=100,width=260,height=55)
        self.but_ex = Button(beat,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#1e2124",relief='flat',command=self.ExitApp)
        self.but_ex.place(x=1150,y=700)    
 #=============================================================================================================
        self.ent_frm = LabelFrame(beat,text="  Patient Select ",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=285,y=85,width=845,height=75)
        self.srch_lbl = Label(beat,text=" Insert :",width=14,font='Helvetica 12',fg="white", bg="#2c2f33").place(x=315,y=116)
        self.srch_ent = Entry(beat,font='Helvetica 12',width=16,justify='center',textvariable=self.number)
        self.srch_ent.place(x=445,y=118)
        self.typ_cmbx = Label(beat, text="NHS number",font='Helvetica 10',width=5)
        self.typ_cmbx.place(x=595,y=118,width=115)
        self.srch_btn = Button(beat,text="Search",font='Helvetica 12',width=12,fg="white", bg="#005042",command=self.searcx).place(x=770,y=115)
        self.clr_btn = Button(beat,text="Clear",font='Helvetica 12',width=12,fg="white", bg="red").place(x=900,y=115)
 #=============================================================================================================
        self.cho_frm = LabelFrame(beat,text="  Select tests  ",font='Helvetica 11',fg="white",bg="#2c2f33").place(x=285,y=165,width=845,height=195)
      
      
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            beat.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
    def searcx(self):
           nhsnumber = self.number.get()
           db.connect()
           sq1l = "SELECT * FROM pat_reg WHERE nhsnumber='" + nhsnumber + "'"
           db_cursor.execute(sq1l)
           checknumb = db_cursor.rowcount
           if checknumb != 1:
              messagebox.showinfo('Info','No Record Found')
           else:
              self.srch_ent.configure(state='disable') 
              
class Window_img:
    def __init__(self,beat):
        self.beat = beat
        self.beat.config(bg="#2c2f33")
        self.beat.title("Clinical Analysis")
        self.beat.geometry("1220x720")
        self.beat.iconbitmap('Medical-Management/icone.ico')
        self.beat.resizable(0, 0)
 #============================================================================================================= 
        self.frame_left = Frame(beat, width=260, height=720, bg="#23272a").place(x=0,y=0)                 
        self.label3 = Label(beat, text='All work by mr-p-oliveira (⌐■_■), 2021',font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=0 ,y=700, width=260, height=22)
        self.label2 = Label(beat,font='Helvetica 7',
                    fg="#D0D3D4",bg="#1e2124").place(x=260 ,y=700, width=960, height=22)
        self.label = Label(beat, text=' Selected ',font='Helvetica 8',
                            fg="#D0D3D4",bg="#1e2124").place(x=0,y=87,width=260,height=13)
 #=============================================================================================================
        self.lf_btn = Label(beat,text="Medical Imaging",font='Helvetica 12',fg="white", bg="#0082c8",relief='flat')
        self.lf_btn.place(x=0,y=100,width=260,height=55)
        self.but_ex = Button(beat,text="Exit",font='Helvetica 7',width=10,fg="white", bg="#1e2124",relief='flat',command=self.ExitApp)
        self.but_ex.place(x=1150,y=700)    
 #=============================================================================================================
        self.ent_frm = LabelFrame(beat,text="Patient",fg="white",bg="#2c2f33").place(x=285, y=100 ,width=600, height= 55 )
 #=============================================================================================================
    def ExitApp(self):
         self.ExitApp = tkinter.messagebox.askquestion ('Exit Portal','Are you sure you want to exit the application. ( Your data is automatically saved )',icon = 'warning')
         if self.ExitApp == 'yes':
            beat.destroy()
         else:
            messagebox.showinfo('Return','You will now return to the application screen')
if __name__ == "__main__": 
   date= datetime.datetime.now().date()
   beat = Tk()
   app = Window_anal(beat)
   beat.mainloop()

