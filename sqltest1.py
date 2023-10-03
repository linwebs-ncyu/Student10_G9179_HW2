import mysql.connector 
db = mysql.connector.connect(host="localhost", user="newuser", passwd="pass", db="sample") 
cur = db.cursor() 
name = input('Enter Name: ') 
cur.execute("SELECT * FROM userdata WHERE Name = '%s';" % name) 
for row in cur.fetchall(): 
    print(row) 
db.close()
