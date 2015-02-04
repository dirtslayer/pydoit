# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import tasklistbuilder, prefs, math

class buttonbuilder():

	# param 1 - the name of the image as refered to in button template
	#   (usually the image file name without .png
	
	# param 2 - the image file name ( bathroom.png )
	image_template = '''
		<object class="GtkImage" id="%s">
		<property name="visible">True</property>
		<property name="can_focus">False</property>
		<property name="pixbuf">%s</property>
		</object>'''

	# param 1 - the button number / id (can be anything really)
	# param 2 - the label to appear on the button
	# param 3 - the image name to use on the button 

	# usually image_template. param1 == button_template .param 2 and .param 3

	# may need to add param 4 and 5 to be left_attach and top_attach
	
	button_template = '''
		 <child>
      <object class="GtkButton" id="button%s">
        <property name="label" translatable="yes">%s</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="image">%s</property>
        <property name="image_position">top</property>
        <property name="always_show_image">True</property>
		<signal name="clicked" handler="do_button" swapped="no"/>
      </object>
      <packing>
        <property name="left_attach">%s</property>
        <property name="top_attach">%s</property>
      </packing>
    </child>
	'''
	# param 1 - a series of image_templates
	# param 2 - a series of button_templates
	
	grid_template = '''<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="3.12"/>
  
<!-- a series of images -->
%s

  <object class="GtkGrid" id="grid2">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="row_spacing">5</property>
    <property name="column_spacing">5</property>
 <!-- a seres of buttons -->
%s
  </object>
  
</interface>
	'''

#	 def __init__(self):

	def build_from_tasklist(self,tl_name):
		
		tlb = tasklistbuilder.tasklistbuilder()	
			
		tll = tlb.get_task_lists(prefs.lists_folder)

		tlx = tlb.get_tasklist_from_tasklists(tll,tl_name)

		i = 0;
		images = ''
		buttons = ''
		width = int(math.sqrt(len(tlx.tasks)))
	
		#build a series of images
		#build a series of buttons
		for t in tlx.tasks:
			row = int(i / width)
			column = i % width
			i = i + 1
			images = images + self.image_template % (t.name,t.image)
			buttons = buttons + self.button_template % (t.name,t.name,t.name,column,row)
		toret = self.grid_template % (images,buttons)
		return toret

bb = buttonbuilder()
uistring = bb.build_from_tasklist(prefs.start_list)


	
			
