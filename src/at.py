# at.py - code to interfere with at
# Copyright (C) 2004, 2005 Philip Van Hoof <me at freax dot org>
# Copyright (C) 2004, 2005 Gaute Hope <eg at gaute dot eu dot org>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import gtk
import mainWindow
import re
import os
import sys
import tempfile


##
## I18N
##
from rhpl.translate import _, N_
import rhpl.translate as translate
domain = 'gnome-schedule'
translate.textdomain (domain)
gtk.glade.bindtextdomain(domain)

class At:
	def __init__(self, parent):
		self.atRecordRegex = re.compile('([^\s]+)\s([^\s]+)\s([^\s]+)\s([^\s]+)\s([^\s]+)')
		self.ParentClass = parent

		#reading at
		self.read ()

		return

	def geteditor (self):
		raise 'Not implemented'

	def createtreemodel (self):
		raise 'Not implemented'
		
	def switchview (self, mode = "simple", init = 0):
		raise 'Not implemented'
		
	def createpreview (self, minute, hour, day, month, weekday, command):
		raise 'Not implemented'

	def getstandardvalue (self):
		raise 'Not implemented'
		
	def getfrequency (self, minute, hour, day, month, weekday):
		raise 'Not implemented'

	def checkfield (self, field, type, regex):
		raise Exception('Abstract method please override','','','')

	def write (self):
		raise 'Not implemented'

	def update (self, linenumber, record, nooutput, title):
		raise 'Not implemented'

	def delete (self, jobid):
		if jobid:
			execute = "atrm " + jobid
		#execute this
		#reread or delete from the list(preferably)		
			
		return

	def append (self, record, nooutput, title):
		raise 'Not implemented'

	def read (self):
		#do 'atq'
		execute = "atq"
		self.linecount = 0
		self.lines = os.popen(execute).readlines()
		for line in self.lines:
			array_or_false = self.parseRecord (line)
			if array_or_false != gtk.FALSE:
				(title, date, time, class_id, job_id, user, command) = array_or_false
				iter = self.ParentClass.treemodel.append([title, date, time, class_id, job_id, user, command])
			self.linecount = self.linecount + 1
		return

	def parse (self, line):
		if len (line) > 1 and line[0] != '#':
			m = self.atRecordRegex.match(line)
			if m != None:
					print m.groups()
					minute = m.groups ()[0]
					hour = m.groups ()[1]
					day = m.groups ()[2]
					month = m.groups ()[3]
					weekday = m.groups ()[4]
					command = m.groups ()[5]
					title = m.groups ()[7]
					if title == None:
						title = "Untitled"

					return minute, hour, day, month, weekday, command, title
		#left unchanged, the fields should be: user, job title, and id
		#would probably have to do a specific job check for each job 
		return gtk.FALSE

	def amountApp (self, amount):
		if amount == "1":
			return _("st.")
		else:
			return _("th.")

	def valToTimeVal (self, val):
		if val == "0" or val == "1" or val == "2" or val == "3" or val == "4" or val == "5" or val == "6" or val == "7" or val == "8" or val == "9":
			return "0" + val
		else:
			return val

	def easy (self, minute, hour, day, month, weekday):
		raise 'Not implemented'