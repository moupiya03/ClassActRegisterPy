from tkinter import *
from tkinter import ttk
import datetime
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class A:
    
    def __init__(self):

        self.root=Tk()
        self.root.geometry("1200x1200")
        self.root.configure(bg="black")
        l1=Label(self.root,text="                                                              ACTIVITY REGISTER                                                                ",bg="dark cyan",font="Helvetica 20 bold")
        l1.grid(row=0,column=0,columnspan=4,sticky="we")
        l=Label(self.root,text="Select a class",bg="dark cyan",font="Helvetica 11 bold")
        l.grid(row=2,column=0,padx=10,pady=10,ipadx=32,sticky="w")
        self.clas=['Select']
        try:
            #creating database
            self.con1=mysql.connector.connect(host='localhost',user='root',passwd='',charset='utf8')
            cur1 = self.con1.cursor()
            cur1.execute("create database  if not exists db_project")

            #creating tables
            self.con=mysql.connector.connect(host='localhost',charset='utf8',database='db_project',user='root',password="")
            c=self.con.cursor()
            c.execute("create table if not exists tbl_class (slno int(3) primary key, cname varchar(50), sec varchar(1), no_students int(2));")
            c.execute("create table if not exists tbl_main (date varchar(50) primary key, slno int(3), class varchar(4), section varchar(4), total_no_of_students int(3), student_present int(3), subject varchar(20), topic varchar(100), teacher_name varchar(20), weakness varchar(100), monitor_boy varchar(20), monitor_girl varchar(20));")
            c.execute("create table if not exists tbl_setting (slno int(3) primary key);")
            c.execute("create table if not exists tbl_sub (slno int(2) primary key, sname varchar(30));")
            c.execute("create table if not exists tbl_teacher (slno int(2) primary key, tname varchar(30));")           
            c.execute("select distinct(cname)from tbl_class")
            result=c.fetchall() 
            for i in result:
                self.clas.append(i)
            c.close()
        except Error as e:
            print(e)
        #self.L=["LKG","UKG","1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D","6A","6B","6C","6D","7A","7B","7C","7D","8A","8B","8C","8D","9A","9B","9C","9D","10A","10B","10C","10D","11A","11B","11C","11D","11E","12A","12B","12C","12D","12E"]
        self.cb=ttk.Combobox(self.root,values=self.clas)
        self.cb.current(0)
        self.cb.bind("<<ComboboxSelected>>",self.getSection)

        self.cb.grid(row=2,column=1,sticky="e")

        
        L2=Label(self.root,text='Select Section',bg="dark cyan",font="Helvetica 11 bold")
        L2.grid(row=3,column=0,padx=10,pady=10,ipadx=32,sticky="w")
        self.sec=['Select']

        L3=Label(self.root,text='Total no of students',bg="dark cyan",font="Helvetica 11 bold")
        L3.grid(row=4,column=0,padx=10,pady=10,ipadx=12,sticky="w")

        L4=Label(self.root,text='Total students present',bg="dark cyan",font="Helvetica 11 bold")
        L4.grid(row=5,column=0,padx=10,pady=10,ipadx=5,sticky="w")

        self.t2=Entry(self.root)
        self.t2.grid(row=5,column=1,padx=10,pady=10,ipadx=5,sticky="e")

        L5=Label(self.root,text='Select Subject',bg="dark cyan",font="Helvetica 11 bold")
        L5.grid(row=6,column=0,padx=10,pady=10,ipadx=32,sticky="w")
        self.sub=['Select']
        c=self.con.cursor()
        c.execute("select sname from tbl_sub")
        result=c.fetchall()
        for i in result:
            self.sub.append(i)
        c.close()
        self.cb2=ttk.Combobox(self.root,values=self.sub)
        self.cb2.current(0)
        self.cb2.grid(row=6,column=1,sticky="e")

        

        L6=Label(self.root,text='Topic',bg="dark cyan",font="Helvetica 11 bold")
        L6.grid(row=7,column=0,padx=10,pady=10,ipadx=62,sticky="w")

        self.t3=Entry(self.root)
        self.t3.grid(row=7,column=1,padx=10,pady=10,ipadx=5,sticky="e")

        L7=Label(self.root,text='Select Teacher',bg="dark cyan",font="Helvetica 11 bold")
        L7.grid(row=8,column=0,padx=10,pady=10,ipadx=30,sticky="w")
        self.teacher=['Select']
        c=self.con.cursor()
        c.execute("select tname from tbl_teacher")
        result=c.fetchall()
        for i in result:
            self.teacher.append(i)
        c.close()
        self.cb3=ttk.Combobox(self.root,values=self.teacher)
        self.cb3.current(0)
        self.cb3.grid(row=8,column=1,sticky="e")

        L8=Label(self.root,text='Weakness',bg="dark cyan",font="Helvetica 11 bold")
        L8.grid(row=9,column=0,padx=10,pady=10,ipadx=48,sticky="w")

        self.t4=Entry(self.root)
        self.t4.grid(row=9,column=1,padx=10,pady=10,ipadx=5,sticky="e")

        L9=Label(self.root,text='Monitor(boy)',bg="dark cyan",font="Helvetica 11 bold")
        L9.grid(row=10,column=0,padx=10,pady=10,ipadx=38,sticky="w")

        self.t5=Entry(self.root)
        self.t5.grid(row=10,column=1,padx=10,pady=10,ipadx=5,sticky="e")

        L10=Label(self.root,text='Monitor(girl)',bg="dark cyan",font="Helvetica 11 bold")
        L10.grid(row=11,column=0,padx=10,pady=10,ipadx=38,sticky="w")

        self.t6=Entry(self.root)
        self.t6.grid(row=11,column=1,padx=10,pady=10,ipadx=5,sticky="e")

        self.b1=Button(self.root,text='SAVE',bg="dark cyan",font="Helvetica 11 bold",command=self.getSaveInfo)
        self.b1.grid(row=12,column=0,padx=10,pady=10,ipadx=20,sticky="w")

        self.b2=Button(self.root,text='RESET',bg="dark cyan",font="Helvetica 11 bold",command=self.reset_values)
        self.b2.grid(row=12,column=1,padx=10,pady=10,ipadx=20,sticky="e")

        self.b3=Button(self.root,text='QUIT',bg="black",fg="red",font="Helvetica 15 bold underline",command=self.root.destroy)
        self.b3.grid(row=13,column=0,padx=20,pady=20,ipadx=20,ipady=10,sticky="w")


        L11=Label(self.root,text='SL.No',bg="dark cyan",font="Helvetica 11 bold")
        L11.grid(row=1,column=0,padx=10,pady=10,ipadx=62,sticky="w")
        

        self.t7=Entry(self.root)
        c=self.con.cursor()
        c.execute("select slno from tbl_setting")
        result=c.fetchone()
        #x=result[0]
        #self.t7.insert(END,str(x))
        
        self.t7.grid(row=1,column=1,padx=10,pady=10,ipadx=5,sticky="e")

        L12=Label(self.root,text='Date',bg="dark cyan",font="Helvetica 11 bold")
        L12.grid(row=1,column=2,padx=10,pady=10,ipadx=20,sticky="e")

        self.t8=Entry(self.root)
        d=datetime.now()
        d=d.strftime("%d-%m-%y %H:%M:%S")
        self.t8.insert(END,str(d))
        self.t8.grid(row=1,column=3,padx=10,pady=10,ipadx=20,sticky="e")
        
        self.root.mainloop()
    def getSection(self,e):
        no=self.cb.get()
        c=self.con.cursor()
        c.execute("select sec from tbl_class where cname='"+no+"'")
        result=c.fetchall()
        for i in result:
            self.sec.append(i)
        c.close()
        self.cb1=ttk.Combobox(self.root,values=self.sec)
        self.cb1.current(0)
        self.cb1.bind("<<ComboboxSelected>>",self.getNoOfStudents)

        self.cb1.grid(row=3,column=1,sticky="e")
        
    def getNoOfStudents(self,e):
        no=self.cb1.get() #sec
        no1=self.cb.get() #cname
        c=self.con.cursor()
        c.execute("select no_students from tbl_class where cname='"+no1+"' and sec='"+no+"'")
        result=c.fetchone()
        x=result[0]
        
    
        self.t1=Entry(self.root)
        self.t1.insert(END,str(x))
        self.t1.grid(row=4,column=1,padx=10,pady=10,ipadx=5,sticky="e")
        

        c.close()

    def getSaveInfo(self):
        date=self.t8.get()
        slno=self.t7.get()
        clas=self.cb.get()
        sec=self.cb1.get()
        TS=self.t1.get()
        TP=self.t2.get()
        sub=self.cb2.get()
        topic=self.t3.get()
        teacher_name=self.cb3.get()
        weakness=self.t4.get()
        monitor_boy=self.t5.get()
        monitor_girl=self.t6.get()

        c=self.con.cursor()
        c.execute("insert into tbl_main(date,slno,class,section,total_no_of_students,student_present,subject,topic,teacher_name,weakness,monitor_boy,monitor_girl)values('"+date+"','"+slno+"','"+clas+"','"+sec+"','"+TS+"','"+TP+"','"+sub+"','"+topic+"','"+teacher_name+"','"+weakness+"','"+monitor_boy+"','"+monitor_girl+"')")
        messagebox.showinfo("Title","date="+str(date)+"slno="+str(slno)+"class="+clas+"section="+sec+"total_no_of_students="+TS+"student_present="+TP+"subject="+sub+"topic="+topic+"teacher_name="+teacher_name+"monitor_boy="+monitor_boy+"monitor_girl="+monitor_girl)
        c.close()
        
    def reset_values(self):
        self.cb.set(0)
        self.cb1.set(0)
        self.t1.delete(0,'end')
        self.t2.delete(0,'end')
        self.cb2.set(0)
        self.t3.delete(0,'end')
        self.cb3.set(0)
        self.t4.delete(0,'end')
        self.t5.delete(0,'end')
        self.t6.delete(0,'end')

        
    #reset()
       
        
        

        

            
        
        

                            
        
ob=A()

