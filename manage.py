

from tkinter import * 
import sqlite3
root=Tk()
v=IntVar()

m=IntVar()

t1=['1','FIRST NAME','LAST NAME','COMPANY','ADRESS','WEBSITE','BIRTH DATE']
t2=['1','PHONE TYPE','PHONE NUMBER']
t3=['1','EMAIL TYPE','EMAIL']

con=sqlite3.Connection('contact26_book.db')
cur=con.cursor()
cur.execute('create table if not exists contact00(callerid number primary key,f_name varchar (50),l_name varchar(50),compony varchar(30),adress varchar(80),website varchar(50),birthdate date)')
cur.execute('create table if not exists contact01(callerid number,callertype varchar(10),phone_numbers number,FOREIGN KEY(callerid) references contact00(callerid))')
cur.execute('create table if not exists contact02(callerid number,emailtype varchar(10),email varchar(50),FOREIGN KEY(callerid) references contact00(callerid))')            

cur.execute('select callerid from contact00')

i=cur.fetchall()[-1][0]
            

first_name=Entry(root,width=30)
first_name.grid(row=0,column=1)


last_name=Entry(root,width=30)
last_name.grid(row=1,column=1)


compony=Entry(root,width=30)
compony.grid(row=2,column=1)


phone_numbers=Entry(root,width=30)
phone_numbers.grid(row=3,column=1)

phone_number=Radiobutton(root,text="office",variable=v,value=1)
phone_number.grid(row=4,column=1)

phone_number=Radiobutton(root,text="personal",variable=v,value=2)
phone_number.grid(row=4,column=2)




email=Entry(root,width=30)
email.grid(row=5,column=1)

emaill=Radiobutton(root,text="commercial",variable=m,value=1)
emaill.grid(row=6,column=1)

emaill=Radiobutton(root,text="personal",variable=m,value=2)
emaill.grid(row=6,column=2)


adress=Entry(root,width=30)
adress.grid(row=7,column=1)


website=Entry(root,width=30)
website.grid(row=8,column=1)


birthdate=Entry(root,width=30)
birthdate.grid(row=9,column=1)


first_name_Label=Label(root,text="First Name")
first_name_Label.grid(row=0,column=0)

last_name_Label=Label(root,text="Last Name")
last_name_Label.grid(row=1,column=0)

compony_Label=Label(root,text="Compony")
compony_Label.grid(row=2,column=0)

phone_numbers_Label=Label(root,text="Phone numbers")
phone_numbers_Label.grid(row=3,column=0)

phone_numbers_Label=Label(root,text="phone number type")
phone_numbers_Label.grid(row=4,column=0)



email_Label=Label(root,text="Email ID")
email_Label.grid(row=5,column=0)

email_Label=Label(root,text="Email ID type")
email_Label.grid(row=6,column=0)

adress_name_Label=Label(root,text="Address")
adress_name_Label.grid(row=7,column=0)

website_name_Label=Label(root,text="Website")
website_name_Label.grid(row=8,column=0)


birthdate_name_Label=Label(root,text="Birth Date")
birthdate_name_Label.grid(row=9,column=0)



def submit():
    
    global i
    global typee
    global typee1

    if v.get()==1:
        typee='office'
    else:
        typee='personal'

    if v.get()==1:
        typee1='commercial'
    else:
        typee1='personal'    

    if first_name.get()!="" or last_name.get()!="" or website.get()!="" or phone_numbers.get()!="" or email.get()!="" or compony.get()!="" or adress.get()!="" or birthdate.get()!="":
        i=i+1

    con=sqlite3.Connection('contact26_book.db')
    cur=con.cursor()
    cur.execute('insert into contact00 values(:callerid,:f_name,:l_name,:compony,:adress,:website,:birthdate)',

                {
                 'callerid':i,
                 'f_name':first_name.get(),
                 'l_name':last_name.get(),
                 'compony':compony.get(),
                 
                 
                 'adress':adress.get(),
                 'website':website.get(),
                 'birthdate':birthdate.get()

                    }
    

                )

    cur.execute('insert into contact01 values(:callerid,:phone_numbers,:callertype)',

                {
                 'callerid':i,
                 
                 'phone_numbers':phone_numbers.get(),
                 'callertype':typee
                }
    

                )
            
    cur.execute('insert into contact02 values(:callerid,:emailtype,:email)',

                {
                 'callerid':i,
                 'emailtype':typee1,
                 'email':email.get()
                }
    

                )       
       
    con.commit()
    
    first_name.delete(0,END)
    last_name.delete(0,END)
    compony.delete(0,END)
    phone_numbers.delete(0,END)
    phone_number.deselect()
    emaill.deselect()
    email.delete(0,END)
    adress.delete(0,END)
    website.delete(0,END)
    birthdate.delete(0,END)

def show():
    root1=Tk()
    def search2(x):
        global t1,t2,t3
        con=sqlite3.Connection('contact26_book.db')
        cur=con.cursor()
        cur.execute('select * from contact00')
        lb.delete(0,END)
        def ll2(x):
            con=sqlite3.Connection('contact26_book.db')
            cur=con.cursor()
            t=str(lb.get(lb.curselection()))
            
            lb.delete(0,END)
            cur.execute('select * from contact00')
            contactinfo1=cur.fetchall()
            cur.execute('select * from contact01')
            c2=cur.fetchall()
            cur.execute('select * from contact02')
            c3=cur.fetchall()
            

            k=0
            print(c2)
            for i in contactinfo1:
                        
                        if t==(i[1]+" "+i[2]):
                            for j in range(1,7):
                                
                                lb.insert(END,t1[j]+" : "+i[j])
                                
                            
                            for j in range(1,3):
                                
                                lb.insert(END,t2[j]+" : "+str(c2[k][j]))

                            for j in range(1,3):
                                lb.insert(END,t3[j]+" : "+str(c3[k][j]))
                                
                        k=k+1
                        
        
        lb.bind("<<ListboxSelect>>",ll2)
        
        
        k=cur.fetchall()
        for j in k:
            
            m=e1.get()
            if j[1].find(m)==0 or j[2].find(m)==0:
                print(j[1]+" "+j[2])
                lb.insert(END,j[1]+" "+j[2])
                

        
    def ll(x):
            global t1,t2,t3
            con=sqlite3.Connection('contact26_book.db')
            cur=con.cursor()
            t=str(lb.get(lb.curselection()))
            
            lb.delete(0,END)
            cur.execute('select * from contact00')
            contactinfo=cur.fetchall()
            cur.execute('select * from contact01')
            c2=cur.fetchall()
            cur.execute('select * from contact02')
            c3=cur.fetchall()
            
            k=0
            for i in contactinfo:
                        if t==(i[1]+" "+i[2]):
                            for j in range(1,7):
                                
                                lb.insert(END,t1[j]+" : "+i[j])
                            
                        
                            for j in range(1,3):
                                
                                lb.insert(END,t2[j]+" : "+str(c2[k][j]))
                            for j in range(1,3):
                                lb.insert(END,t3[j]+" : "+str(c3[k][j]))    
                        k=k+1
        
        
        
    
        
        
    
    
    
    lb=Listbox(root1,width=50,selectmode=SINGLE)
    lb.grid(row=1,column=0)
    cur.execute('select * from contact00')
    for n in cur.fetchall():
        lb.insert(END,n[1]
                  +" "+n[2])
    

    
    
    
    lb.bind('<<ListboxSelect>>',ll)
    
    root1.bind("<Key>", search2)
    Label(root1,text=search2)
    root1.mainloop()
    

    



    
   
def search1():
    
    root1=Tk()
    def search2(x):
        global t1,t2,t3
        con=sqlite3.Connection('contact26_book.db')
        cur=con.cursor()
        cur.execute('select * from contact00')
        lb.delete(0,END)
        def ll2(x):
            con=sqlite3.Connection('contact26_book.db')
            cur=con.cursor()
            t=str(lb.get(lb.curselection()))
            
            lb.delete(0,END)
            cur.execute('select * from contact00')
            contactinfo1=cur.fetchall()
            cur.execute('select * from contact01')
            c2=cur.fetchall()
            cur.execute('select * from contact02')
            c3=cur.fetchall()
            

            k=0
            print(c2)
            for i in contactinfo1:
                        
                        if t==(i[1]+" "+i[2]):
                            for j in range(1,7):
                                
                                lb.insert(END,t1[j]+" : "+i[j])
                                
                            
                            for j in range(1,3):
                                
                                lb.insert(END,t2[j]+" : "+str(c2[k][j]))

                            for j in range(1,3):
                                lb.insert(END,t3[j]+" : "+str(c3[k][j]))
                                
                        k=k+1
                        
        
        lb.bind("<<ListboxSelect>>",ll2)
        
        
        k=cur.fetchall()
        for j in k:
            
            m=e1.get()
            if j[1].find(m)==0 or j[2].find(m)==0:
                print(j[1]+" "+j[2])
                lb.insert(END,j[1]+" "+j[2])
                

        
    def ll(x):
            global t1,t2,t3
            con=sqlite3.Connection('contact26_book.db')
            cur=con.cursor()
            t=str(lb.get(lb.curselection()))
            
            lb.delete(0,END)
            cur.execute('select * from contact00')
            contactinfo=cur.fetchall()
            cur.execute('select * from contact01')
            c2=cur.fetchall()
            cur.execute('select * from contact02')
            c3=cur.fetchall()
            
            k=0
            for i in contactinfo:
                        if t==(i[1]+" "+i[2]):
                            for j in range(1,7):
                                
                                lb.insert(END,t1[j]+" : "+i[j])
                            
                        
                            for j in range(1,3):
                                
                                lb.insert(END,t2[j]+" : "+str(c2[k][j]))
                            for j in range(1,3):
                                lb.insert(END,t3[j]+" : "+str(c3[k][j]))    
                        k=k+1
        
        
        
    
        
        
    
    e1=Entry(root1,width=50)
    e1.grid(row=0,column=0)
    lb=Listbox(root1,width=50,selectmode=SINGLE)
    lb.grid(row=1,column=0)
    cur.execute('select * from contact00')
    for n in cur.fetchall():
        lb.insert(END,n[1]
                  +" "+n[2])
    

    
    
    
    lb.bind('<<ListboxSelect>>',ll)
    
    root1.bind("<Key>", search2)
    Label(root1,text=search2)
    root1.mainloop()
    

def delete():
    root1=Tk()
    
    def delete1():
        cur.execute('select * from contact00')
        print(cur.fetchall())
        
        
        o=0
        t=str(lb.get(lb.curselection()))
        for j in c:
            print(c[o][0])
            if (j[1]+" "+j[2])==t:
                dels='DELETE from contact00 where callerid= ?'
                cur.execute(dels,(c[o][0],))
                dels1='DELETE from contact01 where callerid= ?'
                cur.execute(dels1,(c[o][0],))
                dels2='DELETE from contact02 where callerid= ?'
                cur.execute(dels2,(c[o][0],))
            o=o+1
            con.commit()

            
        
    

    lb=Listbox(root1,width=50,selectmode=SINGLE)
    lb.grid(row=0,column=0)
    button=Button(root1,text="delete",command=delete1)
    button.grid(row=1,column=0)
    cur.execute('select * from contact00')
    c=cur.fetchall()
    for n in c:
        lb.insert(END,n[1]
                  +" "+n[2])
    
    root1.mainloop()
    con.commit()
    




   
    
    
    


submit_button=Button(root,text="SUBMIT",command=submit)

submit_button.grid(row=14,column=0)

show_button=Button(root,text="show all contacts",command=show)

show_button.grid(row=14,column=1)

search=Button(root,text="sSEARCH",command=search1)

search.grid(row=14,column=2)

delete=Button(root,text="EDIT",command=delete)
delete.grid(row=14,column=3)













con.commit()
root.mainloop()


