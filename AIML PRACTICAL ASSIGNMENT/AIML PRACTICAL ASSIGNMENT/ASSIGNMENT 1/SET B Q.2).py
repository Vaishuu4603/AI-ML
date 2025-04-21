# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:49:47 2025

@author: jayes
"""

from graphviz import Digraph

dot = Digraph()

dot.node('A', 'Start')
dot.node('B', 'Receive input')
dot.node('C', 'Process input')
dot.node('D', 'Provide output')
dot.node('E', 'End')

dot.edges(['AB', 'BC', 'CD', 'DE'])

dot.render('ai_flowchart', format='png', cleanup=True)
