# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:00:06 2021

@author: oruna
"""
#%% dependencies


import graphviz as gv

#%% library

def add_node(m,n,t):
    if n in m.keys():
        m[n].append(t)
    else:
        m[n] = [t]
    return

def convert_to_uc(nodes, mts):
    actors = {}
    for k in mts.keys():
        for v in mts[k]:
            if nodes[v][2] == "F":
                add_node(actors,nodes[v][1],v)
    return(actors)

def get_departments(nodes):
    deps = {}
    for k in nodes.keys():
        v = nodes[k]
        if v[1] in deps.keys():
             deps[v[1]].append(k)
        else:
            deps[v[1]] = [k]
    return(deps)

def get_edges(nodes):
    edges = []
    for k in nodes.keys():
        for t in nodes[k][0]:
            edges.append((k,t))
    return(edges)


#%% data

# node is 4 tuple: < id, outgoting edges, swimlande, type>
# type S - systemic, F - management function, P - enterpise process (material transaction)


nodes_map = {"Start": (["P1"],"Material", "S"),
         "P1": (["F1.1", "P2"], "Material", "P"),
         "P2": (["F2.1", "End"], "Material", "P"),
         "F1.1": (["F1.2"], "Department1", "F"),
         "F1.2": (["F1.3"], "Department2", "F"),
         "F1.3": (["P1"], "Department3", "F"),
         "F2.1": (["P2"], "Department3", "F"),
         "End" : ([] , "Material", "S")}

management_trans = {"MT11" : ["P1", "F1.1", "F1.2", "F1.3"],
                    "MT21" : ["P2", "F2.1"]}




#%% initial diagram
departments = get_departments(nodes_map)

dg = gv.Digraph()
 
for k in departments.keys():      
    aname = "cluster_" + k
    with dg.subgraph(name=aname) as sg:
        #sg.attr(shape="Box", style="filled", color="blue", label=k)
        sg.attr(label=k)
        for n in departments[k]:            
            sg.node(n)    

for k in management_trans.keys():
    aname = "cluster_mt_" + k
    with dg.subgraph(name=aname) as sg:
        sg.attr(label=k)
        for n in management_trans[k]:            
            sg.node(n)   
        
    

dg.edges(get_edges(nodes_map))

dg.view()

#%%

actors = convert_to_uc(nodes_map,management_trans)


ug = gv.Graph()                
for k in actors.keys():
    ug.node(k,shapefile="actor.png", margin="0,0.3",  fontsize = "8" ,height="0.5", labelloc="b")
    ug.edges(map(lambda x: (k, x),actors[k]))

    
ug.view()

