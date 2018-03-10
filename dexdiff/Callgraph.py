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
from dexdiff.Logger import Logger
from dexdiff.Linker import Linker, branchOpcodes
from dexdiff.Renderer import Renderer

class Callgraph:
	def __init__(self):
		self.logger = Logger(__name__).getLogger()
		self.dexMethods = []

	def addDex(self, methods):
		self.dexMethods.append(methods)

	def _mergeDicts(self, x, y):
		z = x.copy()
		z.update(y)
		return (z)

	def build(self):
		self.logger.info("Building callgraph...")
		methods = {}
		for dexMethodsItem in self.dexMethods:
			methods = self._mergeDicts(methods, dexMethodsItem)
		for name, method in methods.iteritems():
			if method.getItem().get_code() != None:
				for inst in method.getItem().get_code().get_bc().get_instructions():
					if (inst.get_op_value() in branchOpcodes):
						branchOpcodes[inst.get_op_value()](methods, method, inst)
		Renderer.build(methods)



