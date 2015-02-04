## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = pydoit.ui


## The main script
bin_SCRIPTS = pydoit.py \
	prefs.py \
	db.py \
	buttons.py

## Directory where .class files will be installed
pydoitdir = $(pythondir)/pydoit


pydoit_PYTHON = \
	pydoit.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
