from anytree import Node, RenderTree

#sudo apt install python-pydot python-pydot-ng graphviz # For installing graphhviz


udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

mary = Node("Mary")
urs = Node("Urs", parent=mary)
chris = Node("Chris", parent=mary)
marta = Node("Marta", parent=mary)

udo.parent = mary


from anytree.exporter import DotExporter


DotExporter(mary).to_picture("tree.png")
