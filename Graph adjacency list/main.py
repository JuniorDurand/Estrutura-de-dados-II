from graph import Graph

#myGraph = Graph(5, oriented = "oriented")
myGraph = Graph(6)

myGraph.addEDGE(1,2,weight= 1)
myGraph.addEDGE(2,5,weight= 2)
myGraph.addEDGE(5,3,weight= 7)
myGraph.addEDGE(4,3,weight= 2)
myGraph.addEDGE(1,5,weight= 4)


print(myGraph)

"""
myGraph.Prim(u=1)

print(myGraph.MTS)
myGraph.Kruskal()
print(myGraph.MTS)
"""

myGraph.Dijkstra(1)

print(myGraph.vertex[4].dist)