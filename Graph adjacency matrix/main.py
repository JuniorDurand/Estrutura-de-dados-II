from graph import Graph

#myGraph = Graph(5, oriented = "oriented")
myGraph = Graph(5)

myGraph.addEDGE(1,4)
myGraph.addEDGE(1,3)
myGraph.addEDGE(1,4)
myGraph.addEDGE(2,3)
myGraph.addEDGE(3,4)
myGraph.addEDGE(2,4)
myGraph.addEDGE(3,4)


print(myGraph)

myGraph.removeEDGE(3,4)

print(myGraph)