#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#



from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys, calendar
import db, prefs, buttonbuilder
import listpicker
import tasklistbuilder


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "./pydoit.ui"
#UI_FILE = "/usr/local/share/pydoit/ui/pydoit.ui"

class GUI:
	hb = Gtk.HeaderBar()
	dbx = db.db()

	def __init__(self):

		self.current_list = prefs.start_list

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		menu = self.builder.get_object('menubar1')
		self.hb.add(menu)
	
		self.on_calendar1_day_selected (None)

		window = self.builder.get_object('pydoitWindow')
		window.connect('destroy', Gtk.main_quit)
		window.resize(500,600)

		mlabel = self.builder.get_object('msglabel')
		mlabel.set_alignment(0.03,0.0)

		#main window has a listpicker
		self.listpick = None
		#main window has a button builder
		self.bb = None

		

		self.swap_ui(prefs.start_list)

		self.tlb = tasklistbuilder.tasklistbuilder()	
			
		self.tll = self.tlb.get_task_lists(prefs.lists_folder)

		self.tlx = self.tlb.get_tasklist_from_tasklists(self.tll,self.current_list)

		

	def get_date_from_cal(self):
		cal = self.builder.get_object('calendar1')
		year,month,day = cal.get_date()
		return (year,month + 1,day)
		
	def set_header_title(self):
		window = self.builder.get_object('pydoitWindow')
		self.hb.set_show_close_button(True)
		year,month,day = self.get_date_from_cal()
		self.hb.props.title = self.dbx.username + "'s " + self.current_list + " list - " + \
		calendar.month_name[month] + \
		" " + str(day) + ", " + str(year)
		window.set_titlebar(self.hb)
		window.show_all()
		
	

	def listbox_remove_all(self):
		listbox = self.builder.get_object('listbox1')
		c =  listbox.get_children()
		for x in c:
			listbox.remove(x)			
		listbox.show_all()

	def on_calendar1_day_selected(self,window):
		self.set_header_title()
		self.listbox_remove_all()
		datestring = "%s-%s-%s" %  self.get_date_from_cal ()
		tasks = self.dbx.get_tasks_on_date_inlist(self.current_list,datestring)
		for rows in tasks:
			for t in rows:
				self.add_label(t)
		mlbl = self.builder.get_object('msglabel')
		mlbl.set_label('')
	
	def label_check(self,text):
		listbox = self.builder.get_object('listbox1')
		c =  listbox.get_children() # c is a list
		for x in c:
			xc = x.get_child()
			xcc = xc.get_children()
			labelg = xcc[0]
			if text == labelg.get_text():
				return True
		return False

		
	def add_label(self,text):
		listbox = self.builder.get_object('listbox1')

		if self.label_check(text) == False:
			row = Gtk.ListBoxRow()
			hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
			label = Gtk.Label(text, xalign=0)
			label.set_margin_left(15)
			label.set_margin_top(10)
			label.set_margin_bottom(10)		
			hbox.pack_start(label, True, True, 0)
			row.add(hbox)
			listbox.add(row)
			listbox.show_all()
			

	def on_listbox1_row_activated(self,box,row):
		if row:

			rowchild = row.get_children()
			listpopbox = rowchild.pop()			
			boxchildren = listpopbox.get_children()
			labelobj = boxchildren.pop()
			text = labelobj.get_label()

			datestring = "%s-%s-%s" %  self.get_date_from_cal ()
			self.dbx.delete_task_from_date_inlist(self.current_list,datestring,text)
			
			box.remove(row)
			box.show_all()
		return True

	def do_button(self,window):
		text = window.get_label()
		if self.label_check(text) == True:
			return
		self.add_label(text)
		datestring = "%s-%s-%s" %  self.get_date_from_cal ()
		self.dbx.insert_into_inlist(self.current_list,text,datestring)

		self.tlx = self.tlb.get_tasklist_from_tasklists(self.tll,self.current_list)
		#print(self.tlx)
		taskx = self.tlx.find_task(text)
		sndfile = taskx.sound
		os.system(prefs.play_sound_cmd % (sndfile))
		
		mlbl = self.builder.get_object('msglabel')
		mlbl.set_label(taskx.text)
		
	

	def on_imagemenuitem1_activate(self,window):
		dialog = self.builder.get_object('dialog1')
		window = self.builder.get_object('pydoitWindow')
		dialog.set_parent(window)
		dialog.set_transient_for(window)
		dialog.set_modal(True)
		dialog.show_all()

	def on_button7_clicked(self,window):
		dialog = self.builder.get_object('dialog1')
		entry = self.builder.get_object('entry1')
		self.dbx.set_user(entry.get_text())
		self.on_calendar1_day_selected(window)
		dialog.hide()
		
	def on_imagemenuitem2_activate(self,w):
		self.listpick =	listpicker.listpicker(self)
		window = self.builder.get_object('pydoitWindow')
		self.listpick.show_it(window)
		
		
	def swap_ui(self,lname):
		self.current_list = lname
		cll = self.builder.get_object('currentlistlabel')
		cll.set_label(lname)
		self.bb = buttonbuilder.buttonbuilder()
		uistring = self.bb.build_from_tasklist(lname)
		grid1 = self.builder.get_object('grid1')
		grid2 = self.builder.get_object('grid2')
		grid1.remove(grid2)
		grid2.destroy()
		self.builder.add_from_string(uistring)
		grid3 =  self.builder.get_object('grid2')
		grid1.add(grid3)
		self.builder.connect_signals(self)		
		grid1.grab_focus()
		self.on_calendar1_day_selected(None) 
		mlbl = self.builder.get_object('msglabel')
		mlbl.set_label(' ')

		
def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())

