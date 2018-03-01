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

import argparse
from dexdiff.Logger import Logger

class ArgParser:
	def __init__(self, argv):
		self.logger = Logger(__name__).getLogger()
		self.parser = None
		self.argv = None
		self._run(argv)

	def getInitialFiles(self):
		return (self.argv.initial)

	def getModifiedFiles(self):
		return (self.argv.modified)

	def getClasses(self):
		return (self.argv.classes)

	def getOutput(self):
		return (self.argv.output)

	def _run(self, argv):
		self.parser = argparse.ArgumentParser(prog="dexdiff", description="Graph-based diff tool that aims to determine the differences between two versions of the same .dex files.")
		self.parser.add_argument("-i", "--initial", nargs="+", required=True, help="Path(s) to one or a few original dex files", metavar="FILEPATH")
		self.parser.add_argument("-m", "--modified", nargs="+", required=True, help="Path(s) to one or a few modified dex files", metavar="FILEPATH")
		self.parser.add_argument("-c", "--classes", nargs="+", required=False, help="Specific classes to inspect", metavar="CLASSNAME")
		self.parser.add_argument("-o", "--output", required=True, help="Name of the output file", metavar="FILENAME")
		self.argv = self.parser.parse_args(argv)
		self.logger.debug(self.argv)