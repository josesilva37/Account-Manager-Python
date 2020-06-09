from tkinter import *
import sqlite3
from cryptography.fernet import Fernet


root=Tk()
root.iconbitmap("icon.ico")
root.title("Account Manager")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('accounts_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE accounts (
		name text,
		email text,
		password text
		)""")
'''
#Commit Changes
conn.commit()

# Close Connection 
conn.close()

def account():
	pswd = p.get()
	if(pw==pswd):
		list = root.grid_slaves()
		for l in list:
			l.destroy()

		def submit():
			conn = sqlite3.connect('accounts_book.db')
			c = conn.cursor()

			c.execute("INSERT INTO accounts VALUES (:name,:email,:password)",
			{
				'name': e1.get(),
				'email': e2.get(),
				'password': e3.get()
			})

			conn.commit()

			e1.delete(0, END)
			e2.delete(0, END)
			e3.delete(0, END)

		def query():
			conn = sqlite3.connect('accounts_book.db')
			c = conn.cursor()

			#Query Database
			c.execute("SELECT *, oid FROM accounts ")
			records = c.fetchall()
			print_records=""
			for record in records:
				print_records += str(record) + "\n"

			query_label = Label(root,text=print_records)
			query_label.grid(row=8,column=1,columnspan=2)

			conn.commit()		

		def delete():
			# Create a database or connect to one
			conn = sqlite3.connect('accounts_book.db')
			# Create cursor
			c = conn.cursor()

			# Delete a record
			c.execute("DELETE from accounts WHERE oid = " + delete_e.get())

			delete_e.delete(0, END)

			#Commit Changes
			conn.commit()

		l1= Label(root,text='Service Name')
		l2= Label(root,text='Email')
		l3= Label(root,text='Password')

		l1.grid(row=1,column=0)
		l2.grid(row=2,column=0)
		l3.grid(row=3,column=0)

		e1 = Entry(root,width=35,borderwidth=5)
		e1.grid(row=1,column=1)

		e2 = Entry(root,width=35,borderwidth=5)
		e2.grid(row=2,column=1)

		e3 = Entry(root,show="*",width=35,borderwidth=5)
		e3.grid(row=3,column=1)

		b = Button(root, text='Submit', command = submit)
		b.grid(row=4,column=1,)

		query_b = Button(root, text='Show Accounts',command=query)
		query_b.grid(row=7,column=1,columnspan=2)

		delete_e = Entry(root,width=35,borderwidth=5)
		delete_e.grid(row=5,column=1,columnspan=2)

		delete_b = Button(root, text = 'Delete Accounts', command=delete)
		delete_b.grid(row=6,column=1,columnspan=2)
		

	else:
		list = root.grid_slaves()
		for l in list:
			l.destroy()
		wrong = Label(root,text='Wrong Password')
		wrong.grid(row=1,column=1)

#OpenKey
file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()


f = open("Pass.txt","rb")
pw = f.read()
f = Fernet(key)
decrypted = f.decrypt(pw)
pw = decrypted.decode('utf-8')


password = Label(root,text="Enter Password")
password.grid(row=1,column=0)

p = Entry(root, show="*", width=15)
p.grid(row=1,column=1)

b = Button(root, text='Ok', command = account)
b.grid(row=2,column=1)



root.mainloop()