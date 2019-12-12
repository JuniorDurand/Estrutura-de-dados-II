from graph import Graph

#myGraph = Graph(5, oriented = "oriented")
myGraph = Graph(6)

myGraph.addEDGE(1,2)
myGraph.addEDGE(2,5)
myGraph.addEDGE(5,3)
myGraph.addEDGE(4,5)
myGraph.addEDGE(1,5)


print(myGraph)

myGraph.BFS(u=1)
myGraph.BFS_orig_dest( 1, 4)