# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #

#from gi.repository import Gtk, GdkPixbuf, Gdk

from gi.repository import Gtk
import tasklistbuilder, prefs

class listpicker:
	def __init__(self,parent):
		self.parent = parent
		self.builder = Gtk.Builder()
		self.builder.add_from_file('./selectlist.ui')
		self.builder.connect_signals(self)

		tlb = tasklistbuilder.tasklistbuilder()		
		tll = tlb.get_task_lists(prefs.lists_folder)
		names = tlb.get_tasklists_names(tll)
		
		listbox = self.builder.get_object('listbox2')

		for n in names:
			row = Gtk.ListBoxRow()
			hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
			label = Gtk.Label(n, xalign=0)
			label.set_margin_left(15)
			label.set_margin_top(10)
			label.set_margin_bottom(10)
			
			hbox.pack_start(label, True, True, 0)
			row.add(hbox)
			listbox.add(row)
		listbox.show_all()

		window = self.builder.get_object('listpickerdialog')
		window.resize(300,400)
		self.result = None
		


	def on_buttonCancel_clicked(self,button):
		# Gtk.main_quit()
		window = self.builder.get_object('listpickerdialog')
		self.result = None
		window.hide()
		

	def on_buttonOK_clicked(self,button):
		window = self.builder.get_object('listpickerdialog')
		listbox2 = self.builder.get_object('listbox2')
		row = None
		self.result = None
		row = listbox2.get_selected_row()
		if row != None:
			rowchild = row.get_children()
			box = rowchild[0]
			bchildren = box.get_children()
			labelobj = bchildren[0]
			text = labelobj.get_label()
			self.result = text
		window.hide()
		self.parent.swap_ui(text)
			


	def show_it(self,window):
		pickerdialog = self.builder.get_object('listpickerdialog')
		pickerdialog.set_transient_for(window)
		pickerdialog.set_modal(True)
		pickerdialog.show_all()


#app = listpicker()
	
#dialog = app.builder.get_object('listpickerdialog')
#window = self.builder.get_object('pydoitWindow')
#dialog.set_parent(None)
#		dialog.set_transient_for(window)
#dialog.set_modal(True)
#dialog.show_all()

#Gtk.main()	
