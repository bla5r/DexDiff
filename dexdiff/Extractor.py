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
from dexdiff.Method import Method
from dexdiff.Signature import Signature

class Extractor:
	@staticmethod
	def _openFile(filename):
		logger = Logger(__name__).getLogger()
		try:
			return (open(filename, "r"))
		except IOError:
			logger.error("Unable to open the file \"%s\"." % filename)
			sys.exit(1)

	@staticmethod
	def _closeFile(file):
		file.close()

	@staticmethod
	def _parseDvmRepr(dexFilename):
		logger = Logger(__name__).getLogger()
		try:
			file = Extractor._openFile(dexFilename)
			logger.info("Parsing \"%s\"..." % dexFilename)
			dvmRepr = DalvikVMFormat(file.read())
			Extractor._closeFile(file)
			return (dvmRepr)
		except Exception:
			logger.error("The file \"%s\" doesn't seem to be a valid DEX file." % dexFilename)
			sys.exit(1)

	@staticmethod
	def _bytesToHex(bytes):
		return (''.join(["%02x" % ord(x) for x in bytes]).strip())

	@staticmethod
	def _getHashIdx(dvmRepr, idx):
		return (Signature.genHashIdx(str(dvmRepr.get_cm_method(idx))))

	@staticmethod
	def getMethods(dexFilename):
		logger = Logger(__name__).getLogger()
		methods = {}
		dvmRepr = Extractor._parseDvmRepr(dexFilename)
		for methodItem in dvmRepr.get_methods():
			cm = dvmRepr.get_cm_method(methodItem.get_method_idx())
			methodName = "%s->%s%s%s" % (cm[0], cm[1], cm[2][0], cm[2][1])
			hashIdx = Extractor._getHashIdx(dvmRepr, methodItem.get_method_idx())
			methods[hashIdx] = Method(dvmRepr, methodName, Extractor._bytesToHex(hashIdx), methodItem)
		return (dvmRepr, methods)