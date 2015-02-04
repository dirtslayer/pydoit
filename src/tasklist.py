# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import task


class tasklist():
	
	def __init__(self, name, tasks):
		self.name = name
		self.tasks = tasks

	def find_task(self,tname):
		for t in self.tasks:
			if t.name == tname:
				return t
		return None



#testing

t1 = task.task('blah','blah blah blah','blah.png','blah.aac')
t2 = task.task('play','play play play','play.png','play.aac')

tlist = [t1,t2]

tl = tasklist('playblah',tlist)
