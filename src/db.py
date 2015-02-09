# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -
import sqlite3
import prefs

class db():
	username = None # "username"
	filename = None #"username.db"
	db = None #sqlite3.connect(filename)
	cursor = None #db.cursor() 

	def __init__(self):
		self.set_user(prefs.user)
		
	def create_tables(self):
		cmd = """create table if not exists tasks( listname varchar(255),
			task varchar(255), day integer, month integer, year integer
			)"""
		self.cursor.execute(cmd)	
		return True

	def insert_into_inlist(self,listname,task,day,month,year):
		cmd = "insert into tasks values ('%s','%s','%s','%s','%s')" % (listname, task , day,month,year)
		self.cursor.execute(cmd)	
		self.db.commit()
		return True
	
	def get_days_in_month_task_was_done(self,listname,task,month,year):
		cmd = "select day from tasks where listname='%s' and month='%s' and year='%s' and task='%s'" % (listname,month,year,task)
		self.cursor.execute(cmd)
		rows = self.cursor.fetchall()
		# returns first column packed in tuple so unpack it
		column=[elt[0] for elt in rows]
		return column
		

	def delete_task_from_date_inlist(self,listname,day,month,year,task):
		cmd = "delete from tasks where listname='%s' and day='%s' and month='%s' and year='%s' and task='%s'" % (listname, day, month, year , task)
		
		self.cursor.execute(cmd)
		self.db.commit()
		return True

	def get_tasks_on_date_inlist(self,inlist,day,month,year):
		cmd = "select task from tasks where listname='%s' and day='%s' and month='%s' and year='%s'" % (inlist,day,month,year)
		self.cursor.execute(cmd)
		rows = self.cursor.fetchall()
		return rows

	def set_user(self,uname):
		self.username = uname
		self.filename = uname + ".db"
		self.db = sqlite3.connect(self.filename)
		self.cursor = self.db.cursor() 
		self.create_tables ()

		return True
