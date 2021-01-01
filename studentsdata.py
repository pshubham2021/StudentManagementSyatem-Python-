from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas
import time

root = Tk()
root.title('STUDENT MANAGEMENT SYSTEM')

root.config(bg="gray")
root.iconbitmap('max.ico')
root.geometry('1174x650+0+0')
root.resizable(False, False)


# =========================================================================================
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m:%Y")
    clock.config(text="Date:" + date_string + "\n" + "Time:" + time_string)
    clock.after(200, tick)


def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)
#===============================================Main Operations=======================================
def addstudent():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime =time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%Y")
        try:
            strr='insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('Notification','Id {} Name {} Added sucessfully... and want to clear the form'.format(id,name),parent=addroot)
            if res==True:
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notification','id Already Exist pls Try another id.....',parent=addroot)
        strr='select *from studentdata'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.iconbitmap('max.ico')
    addroot.geometry('470x470+150+150')
    addroot.title('Add Student')
    addroot.resizable(False,False)
    addroot.config(bg='lightblue')
    #=====================================================================================
    idlabel = Label(addroot, text="Enter Id:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    idlabel.place(x=10,y=10)
    namelabel = Label(addroot, text="Enter Name:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    namelabel.place(x=10,y=60)
    mobilelabel = Label(addroot, text="Enter Mobile:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    mobilelabel.place(x=10,y=110)
    emaillabel = Label(addroot, text="Enter Email:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    emaillabel.place(x=10,y=160)
    addresslabel = Label(addroot, text="Enter Address:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    addresslabel.place(x=10, y=210)
    genderlabel = Label(addroot, text="Enter Gender:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    genderlabel.place(x=10, y=260)
    doblabel = Label(addroot, text="Enter D.O.B.:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    doblabel.place(x=10, y=310)
    #==============================================================================================
    idval=StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=2,textvariable=idval, bg="lightgreen")
    identry.place(x=200, y=10)
    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=2,textvariable=nameval,bg="lightgreen")
    nameentry.place(x=200, y=60)
    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=2,textvariable= mobileval, bg="lightgreen")
    mobileentry.place(x=200, y=110)
    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=2, textvariable=emailval,bg="lightgreen")
    emailentry.place(x=200, y=160)
    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=2, textvariable=addressval,bg="lightgreen")
    addressentry.place(x=200, y=210)
    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=2,textvariable= genderval, bg="lightgreen")
    genderentry.place(x=200, y=260)
    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=2,textvariable=dobval, bg="lightgreen")
    dobentry.place(x=200, y=310)
    addrootbutton=Button(addroot,text='Submit',command=submitadd,font=('arial',20,'bold'),bg='red',bd=3,activebackground='blue',activeforeground="white")
    addrootbutton.place(x=150,y=380)
    addroot.mainloop()
#=========================================================================================================
def searchstudent():
    def searchadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if id != '':
            strr='select *from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif name != '':
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif mobile != '':
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif email != '':
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif address != '':
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif gender != '':
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif dob != '':
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif addeddate != '':
            strr = 'select *from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.iconbitmap('max.ico')
    searchroot.geometry('470x540+150+150')
    searchroot.title('Search Student')
    searchroot.title('Search Student')
    searchroot.resizable(False, False)
    searchroot.config(bg='lightblue')
    # =====================================================================================
    idlabel = Label(searchroot, text="Search Id:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                    relief=GROOVE, borderwidth=3, width=12)
    idlabel.place(x=10, y=10)
    namelabel = Label(searchroot, text="Search Name:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    namelabel.place(x=10, y=60)
    mobilelabel = Label(searchroot, text="Search Mobile:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    mobilelabel.place(x=10, y=110)
    emaillabel = Label(searchroot, text="Search Email:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                       relief=GROOVE, borderwidth=3, width=12)
    emaillabel.place(x=10, y=160)
    addresslabel = Label(searchroot, text="Search Address:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                         relief=GROOVE, borderwidth=3, width=12)
    addresslabel.place(x=10, y=210)
    genderlabel = Label(searchroot, text="Search Gender:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    genderlabel.place(x=10, y=260)
    doblabel = Label(searchroot, text="Search D.O.B.:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                     relief=GROOVE, borderwidth=3, width=12)
    doblabel.place(x=10, y=310)
    datelabel = Label(searchroot, text="Search Date:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                     relief=GROOVE, borderwidth=3, width=12)
    datelabel.place(x=10, y=370)
    # ==============================================================================================
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=idval)
    identry.place(x=200, y=10)
    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=nameval)
    nameentry.place(x=200, y=60)
    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable= mobileval)
    mobileentry.place(x=200, y=110)
    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=emailval)
    emailentry.place(x=200, y=160)
    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen", textvariable=addressval)
    addressentry.place(x=200, y=210)
    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable= genderval)
    genderentry.place(x=200, y=260)
    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=dobval)
    dobentry.place(x=200, y=310)
    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=dateval)
    dateentry.place(x=200, y=370)
    searchrootbutton = Button(searchroot, text='Submit', command=searchadd, font=('arial', 20, 'bold'), bg='red', bd=3,
                           activebackground='blue', activeforeground="white")
    searchrootbutton.place(x=150, y=420)
    searchroot.mainloop()
#=======================================================================================================================
def deletestudent():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','id {} deleted succesfully'.format(pp))
    strr = 'select *from studentdata'
    mycursor.execute(strr, (strr))
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


#=======================================================================================================================
def updatestudent():
    def updateadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date=dateval.get()
        time=timeval.get()

        strr='update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification','id {} Modified sucessfuly...'.format(id),parent=updateroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.iconbitmap('max.ico')
    updateroot.geometry('470x580+60+50')
    updateroot.title('update Student')
    updateroot.resizable(False, False)
    updateroot.config(bg='lightblue')
    # =====================================================================================
    idlabel = Label(updateroot, text="Update Id:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                    relief=GROOVE, borderwidth=3, width=12)
    idlabel.place(x=10, y=10)
    namelabel = Label(updateroot, text="Update Name:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    namelabel.place(x=10, y=60)
    mobilelabel = Label(updateroot, text="Update Mobile:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    mobilelabel.place(x=10, y=110)
    emaillabel = Label(updateroot, text="Update Email:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                       relief=GROOVE, borderwidth=3, width=12)
    emaillabel.place(x=10, y=160)
    addresslabel = Label(updateroot, text="Update Address:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                         relief=GROOVE, borderwidth=3, width=12)
    addresslabel.place(x=10, y=210)
    genderlabel = Label(updateroot, text="Update Gender:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    genderlabel.place(x=10, y=260)
    doblabel = Label(updateroot, text="Update D.O.B.:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                     relief=GROOVE, borderwidth=3, width=12)
    doblabel.place(x=10, y=310)
    datelabel = Label(updateroot, text="Update Date:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                     relief=GROOVE, borderwidth=3, width=12)
    datelabel.place(x=10, y=370)
    timelabel = Label(updateroot, text="Update Time:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                     relief=GROOVE, borderwidth=3, width=12)
    timelabel.place(x=10, y=430)
    # ==============================================================================================
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval=StringVar()
    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=idval)
    identry.place(x=200, y=10)
    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=nameval)
    nameentry.place(x=200, y=60)
    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable= mobileval)
    mobileentry.place(x=200, y=110)
    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=emailval)
    emailentry.place(x=200, y=160)
    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen", textvariable=addressval)
    addressentry.place(x=200, y=210)
    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable= genderval)
    genderentry.place(x=200, y=260)
    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=dobval)
    dobentry.place(x=200, y=310)
    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=dateval)
    dateentry.place(x=200, y=370)
    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=timeval)
    timeentry.place(x=200, y=430)
    updaterootbutton = Button(updateroot, text='Submit', command=updateadd, font=('arial', 20, 'bold'), bg='red', bd=3,
                           activebackground='blue', activeforeground="white")
    updaterootbutton.place(x=150, y=490)
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if len(pp) !=0 :
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()
#===============================================================================================================

def showstudent():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

#==================================================================================================================
def exportstudent():
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp= content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time']
    df=pandas.DataFrame(list(zip( id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths= r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification', 'student data is saved {}'.format(paths))
#====================================================================================================================
def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do You Want to Exit?')
    if res==True:
        root.destroy()
# ==================================================================================
def connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwdval.get()




        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect pls try again')
            return
        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            strr='create table studentdata(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'database connected and now you are connected to the database...',parent = dbroot)
        except:
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database...',parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.resizable(False, False)
    dbroot.config(bg="lightblue")
    dbroot.geometry('470x250+450+230')

    # ===================================
    hostlabel = Label(dbroot, text="Enter host:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    hostlabel.place(x=10, y=10)
    userlabel = Label(dbroot, text="Enter User:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                      relief=GROOVE, borderwidth=3, width=12)
    userlabel.place(x=10, y=70)
    passwdlabel = Label(dbroot, text="Enter Passwd:", bg="lightgreen", anchor='w', font=('arial', 15, 'bold'),
                        relief=GROOVE, borderwidth=3, width=12)
    passwdlabel.place(x=10, y=130)
    # ===========================================================
    hostval = StringVar()
    userval = StringVar()
    passwdval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=hostval)
    hostentry.place(x=200, y=10)
    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=userval)
    userentry.place(x=200, y=70)
    passwdentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=2, bg="lightgreen",textvariable=passwdval)
    passwdentry.place(x=200, y=130)

    dbbutton = Button(dbroot, text="Submit", bg='red', font=('roman', 15, 'bold'), width=20, activebackground="blue",
                      activeforeground="white",command=submitdb)
    dbbutton.place(x=150, y=200)

    dbroot.mainloop()


# ============================================================================================
import random

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)


# ================================================================================
DataEntryFrame = Frame(root, bg='gold3', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=200, height=550)
#==================================================================================
frontlabel=Label(DataEntryFrame,text="-------------:WELCOME:-----------",width=15,font=('arial',15,'italic bold'),bg='gray')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,command=addstudent,text='Add Student',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
addbtn.pack(side=TOP,expand=True)
Searchbtn=Button(DataEntryFrame,command=searchstudent,text='Search Student',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
Searchbtn.pack(side=TOP,expand=True)
Deletebtn=Button(DataEntryFrame,command=deletestudent,text='Delete Student',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
Deletebtn.pack(side=TOP,expand=True)
Updatebtn=Button(DataEntryFrame,command=updatestudent,text='Update Student',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
Updatebtn.pack(side=TOP,expand=True)
Showbtn=Button(DataEntryFrame,command=showstudent,text='Show All',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
Showbtn.pack(side=TOP,expand=True)
Exportbtn=Button(DataEntryFrame,command=exportstudent,text='Export Data',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
Exportbtn.pack(side=TOP,expand=True)
Exitbtn=Button(DataEntryFrame,command=exitstudent,text='Exit',width=25,font=("chiller",15,"bold"),bd=2,bg='red', activebackground="blue",activeforeground="white")
Exitbtn.pack(side=TOP,expand=True)
#==================================================================================
ShowDataFrame = Frame(root, bg='gold3', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=250, y=80, width=920, height=550)
#==========================================show data frame==============================================================
style=ttk.Style()
style.configure('Treeview.Heading',font=('georgia',12,'bold'),foreground='blue')
style.configure('Treeview',font=('arial',10,'bold'),foreground='green')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable=Treeview(ShowDataFrame,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set,column=('Id','Name','Mobile No','Email','Address','Gender','DOB','Added Date','Added Time'))
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('DOB',text='DOB')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=50)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=100)
studenttable.column('Email',width=200)
studenttable.column('Address',width=300)
studenttable.column('Gender',width=100)
studenttable.column('DOB',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)



# =======================================================================================
ss = 'Welcome To Student Management System'
count = 0
text = ''
# ====================================================================================
SliderLabel = Label(root, text=ss, font=('roman', 30, 'italic bold'), relief=RIDGE, borderwidth=5, width=25,
                    bg="cyan")
SliderLabel.place(x=260, y=0)
IntroLabelTick()
IntroLabelColorTick()
# =======================================================================================
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, width=20, bg="lawn green")
clock.place(x=0, y=0)
tick()
# =======================================================================================
connectbutton = Button(root, text='connect to database', borderwidth=4, width=20, font=('chiller', 14, 'italic bold'),
                       bg="lawn green", activebackground="blue", activeforeground="white", command=connectdb)
connectbutton.place(x=920, y=0)
root.mainloop()
