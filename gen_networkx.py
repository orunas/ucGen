# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:01:23 2021

@author: Arunas
"""
import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()
DG.add_edges_from(edges) 
nx.draw(DG, with_labels = True, connectionstyle="arc3,rad=0.1")

def convert_to_uc(nodes, mts):
    actors = {}
    
    for k in mts.keys():
        with ug.subgraph(name = k) as sg:
            sg.attr(color='lightgrey')
            for v in mts[k]:
                if nodes[v][2] == "F":
                    sg.node(v)
                    add_node(actors,nodes[v][1],v)