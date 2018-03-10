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

from dexdiff.MethodChar import MethodChar

class Method:
	def __init__(self, dvmRepr, methodName, idx, item):
		self.dvmRepr = dvmRepr
		self.methodName = methodName
		self.idx = idx
		self.item = item
		self.char = MethodChar(item)
		self.callers = []
		self.callees = []

	def addCaller(self, method):
		self.callers.append(method)

	def addCallee(self, method):
		self.callees.append(method)

	def getCallers(self):
		return (self.callers)

	def getCallees(self):
		return (self.callees)

	def getDvmRepr(self):
		return (self.dvmRepr)

	def getMethodName(self):
		return (self.methodName)

	def getItem(self):
		return (self.item)

	def getIdx(self):
		return (self.idx)

	def getChar(self):
		return (self.char)