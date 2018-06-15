class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        #create a new array
        array_for_return = []
        for edge in self.edges:
            #take values from the array of edges(value, node_from, node_to)
            append = (edge.value, edge.node_from.value, edge.node_to.value)
            #fill our array with the values
            array_for_return.append(append)
        return array_for_return

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        #create array, which consists of elements, all of which are "None"
        array_for_return = [None]
        for edge in self.edges:
            array_for_return.append(None)
        #create empty arrays for the elements in outer array, which indecies are equal to 'from' nodes
        for edge in self.edges:
            array_for_return[edge.node_from.value] = []
        #create var for indecies
        j = 0
        for i in array_for_return:
            if i == []:
                #find 'from' nodes which are equal to indecies with empty arrays
                for edge in self.edges:
                    if edge.node_from.value == j:
                        #fill the array with values
                        append = (edge.node_to.value, edge.value)
                        i.append(append)
            j += 1
        return array_for_return
        

    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""

        array_for_return = []
        #since values 'from' and 'to' are already sorted, look at the last edge to find max value
        i = self.edges[len(self.edges) - 1]
        src = i.node_from.value
        dest = i.node_to.value
        #find max value out of all 'from' and 'to' values to determine the size of matrix
        if src > dest:
            counter = src
        else:
            counter = dest
        #counter+1 = size of matrix
        for i in range(counter + 1):
            #create a row
            append = []
            for j in range(counter + 1):
                #append columns
                append.append(0)
                #look for spots in the matrix to fill with values
                for edge in self.edges:
                    if i == edge.node_from.value and j == edge.node_to.value:
                        #fill the found spot with the edge value
                        append[j] = edge.value
            #append rows
            array_for_return.append(append)
        return array_for_return
        

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()
