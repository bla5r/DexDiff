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

import graphviz
from dexdiff.Logger import Logger

styles = {
	"graph": {
        "label": "Output callgraph",
        "fontsize": "16",
        "fontcolor": "white",
        "bgcolor": "#333333",
        "rankdir": "BT",
    },
    "nodes": {
        "fontname": "Helvetica",
        "fontcolor": "white",
        "color": "white",
        "style": "filled",
        "fillcolor": "#006699",
    },
    "edges": {
        "style": "dashed",
        "color": "white",
        "arrowhead": "open",
        "fontname": "Courier",
        "fontsize": "12",
        "fontcolor": "white",
    }
}

class Renderer:
	@staticmethod
	def _applyStyles(graph):
		graph.graph_attr.update(
			('graph' in styles and styles['graph']) or {}
		)
		graph.node_attr.update(
			('nodes' in styles and styles['nodes']) or {}
		)
		graph.edge_attr.update(
			('edges' in styles and styles['edges']) or {}
		)
		return (graph)

	@staticmethod
	def _writeFile(graph, filename):
		file = open(filename, "w")
		file.write(graph.source)
		file.close()

	@staticmethod
	def build(methods):
		outFile = "out"
		graph = graphviz.Digraph(format="png")
		logger = Logger(__name__).getLogger()
		for name, method in methods.iteritems():
			graph.node(method.getIdx(), method.getMethodName())
			for callee in method.getCallees():
				logger.debug("%s -> %s" % (method.getMethodName(), callee.getMethodName()))
				graph.edge(method.getIdx(), callee.getIdx())
		graph = Renderer._applyStyles(graph)
		Renderer._writeFile(graph, outFile)
		logger.info("Output file \"%s\" successfully created" % outFile)