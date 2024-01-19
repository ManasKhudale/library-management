import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="root",database="library")

def addbook():
      bn = input("Enter book name:")
      c = input("Enter book code:")
      t = input("Total books:")
      s = input("Enter subject:")
      data = (bn,c,t,s)
      sql = "insert into book values(%s,%s,%s,%s)"
      c=con.cursor()
      c.execute(sql,data)
      con.commit()
      print("------------------------------------------")
      print("Data entered successfully")
      main()

def issueb():
      n = input("Enter name:")
      r = input("Enter reg no.:")
      co = input("Enter the book code:")
      d = input("Enter date:")
      a = "Insert into issue values(%s,%s,%s,%s)"
      data = (n, r, co, d)
      c = con.cursor()
      c.execute(a,data)
      con.commit()
      print("------------------------------------------")
      print("Book issued to:", n)
      bookup(co, -1)

def submitb():
      n = input("Enter name:")
      r = input("Enter reg no.:")
      co = input("Enter the book code:")
      d = input("Enter date:")
      a = "Insert into submit values(%s,%s,%s,%s)"
      data = (n,r,co,d)
      c = con.cursor()
      c.execute(a,data)
      con.commit()
      print("------------------------------------------")
      print("Book submitted by:",n)
      bookup(co,1)

def bookup(co,u):
      a = "select TOTAL from book where BCODE = %S"
      data = (co,)
      c = con.cursor()
      c.execute(a,data)
      myresult=c.fetchone()
      t=myresult[0]+u
      sql = "update book set TOTAL = %s where BCODE = %s"
      d = (t,co)
      c.execute(sql,d)
      con.commit()
      main()

def dbook():
      ac = input("Enter book code:")
      a = "Delete from book where BCODE = %s"
      data = (ac,)
      c = con.cursor()
      c.execute(a,data)
      con.commit()
      main()

def dispbook():
      a = "select * from book"
      c = con.cursor()
      c.execute(a)
      myresult = c.fetchall()
      for i in myresult:
            print("Book Name:",i[0])
            print("Book code:",i[1])
            print("Total:",i[2])
            print("----------------------")
      main()

def main():
 print( """            LIBRARY MANAGER
1. ADD BOOK
2. ISSUE BOOK
3. SUBMIT BOOK
4. DELETE BOOK
5. DISPLAY BOOKS
    """)
def pswd():
     ps = input("Enter password")
     if ps == "library":
            main()
     else:
            print("Wrong password! Try again!")
            pswd()
pswd()

print("--------------------------")
choice = input("Enter command number:")
if(choice=='1'):
            addbook()
elif(choice=='2'):
            issueb()
elif(choice=='3'):
            submitb()
elif(choice=='4'):
            dbook()
elif(choice=='5'):
            dispbook()
else:
         print("Wrong choice")
         main()
