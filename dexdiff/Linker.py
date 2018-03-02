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

from dexdiff.Signature import Signature

class Linker:
	@staticmethod
	def _findMethod(dvmRepr, methods, idx):
		hashIdx = Signature.genHashIdx(str(dvmRepr.get_cm_method(idx)))
		try:
			return (methods[hashIdx])
		except KeyError:
			return (None)
	
	@staticmethod
	def invokeTie(dvmRepr, methods, caller, inst):
		callee = Linker._findMethod(dvmRepr, methods, inst.get_operands()[len(inst.get_operands()) - 1][1])
		if callee != None:
			callee.addCaller(caller)
			caller.addCallee(callee)

branchOpcodes = {
	0x6e: Linker.invokeTie,
	0x6f: Linker.invokeTie,
	0x70: Linker.invokeTie,
	0x71: Linker.invokeTie,
	0x72: Linker.invokeTie
}