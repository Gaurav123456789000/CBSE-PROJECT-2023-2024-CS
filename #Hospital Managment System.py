def add():
    print("INSERT INFORMATION ABOUT THE PATIENT")
    P_id=int(input("ENTER THE PATIENT ID IN DIGIT:"))
    P_name=input("ENTER PATIENT NAME:")
    Age=int(input("ENTER PATIENT AGE:"))
    Disease=input("ENTER PATIENT DISEASE:")
    Incharge=input("ENTER DOCTOR INCHARGE:")
    fee=int(input("ENTER DOCTOR FEES:"))
    cursor.execute("insert into w(P_id,P_name,Age,Disease,Incharge,fee)values('%d','%s','%d','%s','%s','%d')"%(P_id,P_name,Age,Disease,Incharge,fee3
                                                                                                               ))
    print("RECORD OF PATIENT ADDED SUCCESSFULLY:")
    connect.commit()

def delete():
    s=int(input("ENTER PATIENT ID  YOU WANT TO DELETE:"))
    cursor.execute("delete from w where P_id={}".format(s))
    print("PATIENT RECORD DELETED SUCCESSFULLY:")
    connect.commit()

def display():
    print("*********MEDI CARE HOSPITAL*********")
    cursor.execute("SELECt * from w")
    v=cursor.fetchall()
    for i in v:
        print(i)

def update():
    m=input("ENTER THE PATIENT ID:")
    d=int(input("ENTER THE NEW DOCTOR FEES:"))
    cursor=connect.cursor()
    n="update w set fee="+d+'where P_id='+m+';'
    cursor.execute(n)
    cursor.execute("select * from w where P_id="+m)
    for i in cursor:
        P_id,P_name,Age,Disease,Incharge,fee=i
        print("P_id\tP_name\tAge\tDisease\tIncharge\tfee")
        print(P_id,"\t",P_name,"\t",Age,"\t",Disease,"\t",Incharge,"\t\t",fee)
    print("*******RECORD UPDATED********")
    cursor.commit()

def search():
    t=input("ENTER PATIENT ID TO BE SEARCHED:")
    cursor.execute("select * from w where P_id="+t)
    u=cursor.fetchone()
    print(u)
    cursor.commit()
                                         #Hospital Managment System
print("Hospital Managmnet System Project By Gaurav Garg")
print("WELCOME TO MEDI CARE HOSPITAL")

import mysql.connector as mysql
connect=mysql.connect(host='localhost',user='root',password='gaurav')
cursor=connect.cursor()
cursor.execute("create database if  not exists Sample")
cursor.execute("use Sample")
cursor.execute("create table if not exists w\
               (P_id  int primary key,\
               P_name varchar(20),\
               Age int not null,\
               disease varchar(20),\
               Incharge varchar(20),\
               fee int)")

print("       Managment system         ")
print("===========================================================================================")
c=0
while c==0:
    print("===================================================================================")
    print("1.ADD A NEW PATIENT")
    print("2.Delete Old Record")
    print("3.Display Records")
    print("4.Update Records")
    print("5.Search Records")
    print("6.Exit")
    ch=int(input("ENTER YOUR CHOICE"))
    if ch==1:
        add()
    elif ch==2:
        delete()
    elif ch==3:
        display()
    elif ch==4:
        update()
    elif ch==5:
        search()
    elif ch==6:
        break
    else:
        print("INVALID OPTION/CHOICE1")