#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of DexDiff.
#
# Copyright(c) 2018 bla5r
# https://github.com/bla5r
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 3 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import sys
from androguard.core.bytecodes.dvm import DalvikVMFormat
from dexdiff.Logger import Logger

class ClassGraph:
	def __init__(self, dexFilename):
		self.logger = Logger(__name__).getLogger()
		self.dexFilename = dexFilename
		self._openFile(dexFilename)

	def __exit__(self):
		self._closeFile()

	def build(self):
		self.logger.info("Parsing \"%s\"..." % self.dexFilename)
		self.dvmRepr = DalvikVMFormat(self.rawFile.read())
		#self.logger.info("Building callgraph...")

	def _openFile(self, filename):
		try:
			self.rawFile = open(filename, "r")
		except IOError:
			self.logger.error("Unable to open the file \"%s\"" % filename)
			sys.exit(1)

	def _closeFile(self, rawFile):
		self.rawFile.close()