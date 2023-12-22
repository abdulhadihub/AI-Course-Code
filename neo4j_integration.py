from py2neo import Graph, Node, Relationship
graph = Graph(password='hadiIsTheBest')

node1 = Node("Animal", name="Cat")
graph.create(node1)
node2 = Node("Object", name="Fur")
graph.create(node2)

relationship = Relationship(node1, "HAS", node2)
graph.create(relationship)
