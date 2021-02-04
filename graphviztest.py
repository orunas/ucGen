# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:40:04 2021

@author: oruna
"""

from graphviz import Digraph

g = Digraph('G', filename='cluster.gv')
#g = Digraph()


# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
#       so that Graphviz recognizes it as a special cluster subgraph
"""
with g.subgraph(name='cluster_0') as c:
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
    c.attr(label='process #1')
"""

with g.subgraph(name='cluster_1') as c:
    #c.attr(color='blue')
    #c.node_attr['style'] = 'filled'
    c.node('b0')
    c.node('b1')
    c.node('b2')
    c.node('b3')
    #c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
    c.attr(label='process #2')

"""
g.edge('start', 'a0')
g.edge('start', 'b0')
g.edge('a1', 'b3')
g.edge('b2', 'a3')
g.edge('a3', 'a0')
g.edge('a3', 'end')
g.edge('b3', 'end')

g.node('start', shape='Mdiamond')
g.node('end', shape='Msquare')
"""
g.view()