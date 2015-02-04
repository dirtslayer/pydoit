# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import prefs, task, tasklist
import os

class tasklistbuilder:
	def get_task_lists(self,folder):
		# build tasklist from folder contents. follow structure of ./lists
		tasklists = []

		lists = os.listdir(folder)
		
		for tl in lists:

			newtasklist = tasklist.tasklist(tl,[])
		
			tasklists.append(newtasklist)

			taskfolders = os.listdir(folder + tl)
			
			for t in taskfolders:

				p = folder + tl + os.sep +  t

				if os.path.isdir(p):
					task_files = os.listdir(p)
					
					# build task from folder
					newtask = task.task(t,'text','image','sound')
					newtasklist.tasks.append(newtask)

					textfile = p + os.sep + t +".txt"

					if os.path.isfile(textfile):
						with open (textfile, "r") as myfile:
							newtask.text = myfile.read()
					
					imgext = [".jpg",".png"]
					for e in imgext:
						imagefile = p + os.sep + t + e
					
						if os.path.isfile(imagefile):
							newtask.image = imagefile

					sndext = [".ac3",".aac","mp3"]
					for e in sndext:
						soundfile = p + os.sep + t + e
					
						if os.path.isfile(soundfile):
							newtask.sound = soundfile		
		return tasklists

	def print_tasklists(self,x):
		# debug dump tasklists
		for tl in x:
			print(tl.name)
			for t in tl.tasks:
				print('  ',t.name,'  ',t.text,'  ',t.image,'  ',t.sound)


	def get_tasklists_names(self,x):
		# returns a list of all the tasklists
		toret = list()
		for tl in x:
			toret.append(tl.name)
		return toret

	
	def get_tasklist_from_tasklists(self,x,tname):
		# linear search on tasklist name from the list of tasklists
		for tl in x:
			if tl.name == tname:
				return tl
		return None
			

#testing			

tlb = tasklistbuilder()	
#print (prefs.lists_folder)		
tll = tlb.get_task_lists(prefs.lists_folder)
#tlb.print_tasklists(tll)

names = tlb.get_tasklists_names(tll)
#print(names)

tlx = tlb.get_tasklist_from_tasklists(tll,'bedtime')
#print(tlx.name)


