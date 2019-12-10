from graph import Graph

#myGraph = Graph(5, oriented = "oriented")
myGraph = Graph(5)

myGraph.addEDGE(1,2)
myGraph.addEDGE(2,4)
myGraph.addEDGE(2,3)


print(myGraph)

myGraph.BFS(u=1)