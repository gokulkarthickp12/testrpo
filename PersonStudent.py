import sys;
import sqlite3; 
import re   

conn=sqlite3.connect("test2.db")
cur=conn.cursor()

class Address:

    def __init__(self,addressline,city,zipcode,state):
        self.__addressline=addressline
        self.__city=city
        self.__zipcode=zipcode
        self.__state=state
    
    def getaddressid(self):
        return self.__addressid
        
    def getaddressline(self):
        return self.__addressline

    def getcity(self):
        return self.__city

    def getzipcode(self):
        return self.__zipcode

    def getstate(self):
        return self.__state

    def setaddressline(self, value):
        self.__addressline = value

    def setcity(self, value):
        self.__city = value

    def setzipcode(self, value):
        self.__zipcode = value

    def setstate(self, value):
        self.__state = value
        
    def vadidatezipcode(self):
        if(len(self.__zipcode)==6):
            return True
        else:     
            print("Enter valid zipcode")
            return False


    
class Person:
     
    def __init__(self,name,telephoneno,email,ptype):
      
        self.__name=name
        self.__telephoneno=telephoneno
        self.__email=email
        self.__persontype=ptype
        
    def getname(self):
        return self.__name

    def gettelephoneno(self):
        return self.__telephoneno

    def getemail(self):
        return self.__email

    def setname(self, value):
        self.__name = value

    def settelephoneno(self, value):
        self.__telephoneno = value

    def setemail(self, value):
        self.__email = value

    def getpersontype(self):
        return self.__persontype
    
    def setpersontype(self,value):
        self.__persontype=value

    def validatetelephoneno(self):
            
        if(len(self.__telephoneno)==12 and self.__telephoneno.startswith('91')):
            return True
        else:
            print("Enter a valid telephone number")
            return False
            
        
class Student(Person):
            
            
    def __init__(self,name,telephoneno,email,ptype,rno,dept,m1,m2,m3):
        self.__rno=rno
        self.__dept=dept
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
        super(Student, self).__init__(name,telephoneno,email,ptype) # calling base class constructor

          
    def getrno(self):
        return self.__rno

    def getdept(self):
        return self.__dept

    def getm1(self):
        return self.__m1

    def getm2(self):
        return self.__m2

    def getm3(self):
        return self.__m3


    def setrno(self, value):
        self.__rno = value

    def setdept(self, value):
        self.__dept = value

    def setm1(self, value):
        self.__m1 = value

    def setm2(self, value):
        self.__m2 = value

    def setm3(self, value):
        self.__m3 = value
            
            
    def calculatetot(self):
        self.__tot=self.__m1+self.__m2+self.__m3
    
    def displaystudentinfo(self):
        print('Total:',self.__tot)



class Professor(Person):
            
            
    def __init__(self,name,telephoneno,email,ptype,pid,dept,desig,basic):
        self.__pid=pid
        self.__dept=dept
        self.__desig=desig
        self.__basic=basic
        
        super(Professor, self).__init__(name,telephoneno,email,ptype) # calling base class constructor

          
    def getpid(self):
        return self.__pid

    def getdept(self):
        return self.__dept

    def getdesig(self):
        return self.__desig

    def getbasic(self):
        return self.__basic

    def setpid(self, value):
        self.__pid = value

    def setdept(self, value):
        self.__dept = value

    def setdesig(self, value):
        self.__desig = value

    def setbasic(self, value):
        self.__basic = value

              
    def calculatesal(self):
        self.__sal=self.__basic+self.__basic*0.5+self.__basic*0.1-self.__basic*0.15
    
    def displayprofessorinfo(self):
        print('Salary:',self.__sal)
            

class Demo1:
    n=0
    ch='n'
    def personoptions(self):
        print("******************************")
        print(" College Management System")
        print("******************************")
        print("1. Add New Person")
        
     
        print("2. View All Student Details")
        print("3. View All Professor Details")
        print("4. Exit")
        n=int(input("Select your choice"))
        if n==1:
            self.insertrecord()
      
      
        elif n==2:
            self.viewallstudent()
        elif n==3:
            self.viewallprofessor()
        elif n==4:
            print("Thank You!!!")
            sys.exit
           
    
    def insertrecord(self):
        try:

           # conn.execute('''drop table student;''')
           # conn.execute('''drop table professor;''')
            #conn.execute('''drop table address;''')

           # conn.execute('''CREATE TABLE student (NAME  TEXT NOT NULL,telephoneno INT NOT NULL,email text NOT NULL,rno int,dept  text,m1 int,m2 int, m3 int, tot int);''')

            #conn.execute('''CREATE TABLE professor (NAME  TEXT NOT NULL,telephoneno INT NOT NULL,email text NOT NULL,pid int,dept  text,desig text,basic real, sal real);''')
           

            #conn.execute('''CREATE TABLE address (addressline text NOT NULL,city  TEXT    NOT NULL,zipcode INT     NOT NULL,state         text, customerid  int);''')
            
            pname=input("Enter Name")
            ptelephone = input("Enter  Telephone No.")
            pemail=input("Enter Email id")
            ptype=input("Enter person type (Student/Professor)")
            pobj=Person(pname,ptelephone,pemail,ptype) 
            cur.execute("select count(*) from Address")
            for n in cur.fetchall():
                addrrows=n[0]
            addobj=Address(None,None,None,None)
            
            addobj.setaddressline(input("Enter AddressLine"))
            addobj.setcity(input("Enter your City"))
            addobj.setzipcode(input("Enter your zipcode"))
            addobj.setstate(input("Enter your state"))
          
            
            if(pobj.validatetelephoneno()):
                if(pobj.getpersontype() =="Student"):
                    rno=input("Enter Roll no")
                    dept=input("Enter Department")
                    m1=int(input("Enter Mark1"))
                    m2=int(input("Enter Mark2"))
                    m3=int(input("Enter Mark3"))
                    pobj=Student(pname,ptelephone,pemail,ptype,rno,dept,m1,m2,m3)
                    #pobj.calculatetot()
                    if(addobj.vadidatezipcode()):
                        conn.execute("insert into address values(?,?,?,?,?)",(addobj.getaddressline(),addobj.getcity(),addobj.getzipcode(),addobj.getstate(),rno))
                    else:
                        print("Invalid Zipcode")
                        
                    # insert record in Customer table
                    conn.execute("""insert into student(name,telephoneno,email,rno,dept,m1,m2,m3,tot) 
                    values (?,?,?,?,?,?,?,?,?)""",(pobj.getname(),pobj.gettelephoneno(),pobj.getemail(),pobj.getrno(),pobj.getdept(),pobj.getm1(),pobj.getm2(),pobj.getm3(),pobj.calculatetot()))  
                    pobj.displaystudentinfo()
                elif(pobj.getpersontype()=="Professor"):
                    pid=input("Enter Professor ID ")
                    dept=input("Enter Department")
                    des=(input("Enter Designation"))
                    basic=int(input("Enter Basic Pay"))
                    
                    pobj=Professor(pname,ptelephone,pemail,ptype,pid,dept,des,basic)
                    #pobj.calculatesal()
                    
                    if(addobj.vadidatezipcode()):
                        conn.execute("insert into address values(?,?,?,?,?)",(addobj.getaddressline(),addobj.getcity(),addobj.getzipcode(),addobj.getstate(),pid))
                    else:
                        print("Invalid Zipcode")
                    # insert record in Customer table
                    conn.execute("""insert into Professor(name,telephoneno,email,pid,dept,desig,basic,sal) 
                    values (?,?,?,?,?,?,?,?)""",(pobj.getname(),pobj.gettelephoneno(),pobj.getemail(),pobj.getpid(),pobj.getdept(),pobj.getdesig(),pobj.getbasic(),pobj.calculatesal()))
                    pobj.displayprofessorinfo()
                                            
            else:
                print("Invalid Telephone No.")
                Demo1.gotooptions(self)  
        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        finally:
            conn.commit()
            
  
    

    def viewallstudent(self):
        cur.execute("select * from Student")
        for n in cur.fetchall():
            print(n) 

    def viewallprofessor(self):
        cur.execute("select * from Professor")
        for n in cur.fetchall():
            print(n)  

    def gotooptions(self):
        ch=input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            Demo1.personoptions(self)
            
obj=Demo1()
obj.personoptions()
obj.gotooptions()

