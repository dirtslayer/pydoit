# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #

class task():
	
	def __init__(self, name, text, image, sound):
		self.name = name	
		self.text = text
		self.image = image
		self.sound = sound


# testing

t = task('blah','blah blah blah','blah.png','blah.aac')
#print(t.text)
