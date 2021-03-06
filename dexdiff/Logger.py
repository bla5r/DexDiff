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
import logging
from androguard.core.androconf import show_logging
from termcolor import colored

ANDROGUARD_LOG_LEVEL = logging.INFO
DEXDIFF_LOG_LEVEL = logging.DEBUG

class Logger:
	@staticmethod
	def enable():
		show_logging(level=ANDROGUARD_LOG_LEVEL)

	def __init__(self, name):
		self.logger = logging.getLogger(name)
		if len(self.logger.handlers) == 0:
			self.logger.propagate = False
			self.logger.setLevel(DEXDIFF_LOG_LEVEL)
			self._formatOutput()

	def _formatOutput(self):
		handler = logging.StreamHandler(sys.stdout)
		handler.setLevel(DEXDIFF_LOG_LEVEL)
		formatStr = "%s%s%s %s: %s" % (colored("[", attrs=["bold"]), "%(levelname)s", colored("]", attrs=["bold"]), colored("%(name)s", "red"), "%(message)s")
		formatter = logging.Formatter(formatStr)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)

	def getLogger(self):
		return (self.logger)