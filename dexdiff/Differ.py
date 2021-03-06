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

from dexdiff.Extractor import Extractor
from dexdiff.Callgraph import Callgraph
from dexdiff.Logger import Logger

class Differ:
	def __init__(self, initialFiles, modifiedFiles):
		self.logger = Logger(__name__).getLogger()
		self.initialFiles = initialFiles
		self.modifiedFiles = modifiedFiles

	def _buildGraph(self, files):
		callgraph = Callgraph()
		for filename in files:
			methods = Extractor.getMethods(filename)
			callgraph.addMethods(methods)
		callgraph.build()
		return (callgraph)

	def _buildGraphs(self):
		self.logger.info("Gathering information from initial file(s)...")
		initCallgraph = self._buildGraph(self.initialFiles)
		self.logger.info("Gathering information from modified file(s)...")
		modCallgraph = self._buildGraph(self.modifiedFiles)
		return (initCallgraph, modCallgraph)

	def run(self):
		initCallgraph, modCallgraph = self._buildGraphs()
		initCallgraph.compare(modCallgraph)