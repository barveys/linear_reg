import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='db4')
print(mydb.connection_id) #number

cur=mydb.cursor()#current position

'''cur.execute("create database db4")
print("dbase created")'''

'''s="create table book123(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(s)
print("table created")'''



'''d="insert into book123(bookid,title,price) values(%s,%s,%s)"

b1=(1,'python',345)

cur.execute(d,b1) #hard coding

print("data insert")

mydb.commit()'''

d="insert into book123(bookid,title,price) values(%s,%s,%s)"

books=[(2,'C',200),(3,'C++',400),(4,'JAVA',500)]
cur.executemany(d,books )


print("data insert")
mydb.commit()






