# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
# kidslistDB.py
# Copyright (C) 2015 Unknown <darrell@designr8.com>
#
# kidslist is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# kidslist is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
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
			task varchar(255), date varchar(255)
			)"""
		self.cursor.execute(cmd)	
		return True

	def insert_into_inlist(self,listname,task,date):
		cmd = "insert into tasks values ('%s','%s','%s')" % (listname, task , date)
		self.cursor.execute(cmd)	
		self.db.commit()
		return True

	def delete_task_from_date_inlist(self,listname,date,task):
		cmd = "delete from tasks where listname='%s' and date='%s' and task='%s'" % (listname, date , task)
		self.cursor.execute(cmd)
		self.db.commit()
		return True

	def get_tasks_on_date_inlist(self,inlist,date):
		cmd = "select task from tasks where listname='%s' and date='%s'" % (inlist,date)
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
