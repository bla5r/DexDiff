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
from dexdiff.ArgParser import ArgParser
from dexdiff.Extractor import Extractor
from dexdiff.Callgraph import Callgraph
from dexdiff.Logger import Logger

def buildGraphs(argParser):
	callgraph = Callgraph()
	for filename in argParser.getInitialFiles():
		dvmRepr, methods = Extractor.getMethods(filename)
		callgraph.addDex(dvmRepr, methods)
	callgraph.build()

def main(argc, argv):
	Logger.enable()
	argParser = ArgParser(argv)
	buildGraphs(argParser)

if __name__ == "__main__":
	main(sys.argv, sys.argv[1:])