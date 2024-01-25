# get line sets and hot point from text file

import os,csv

def get_line_sets(directory):
    node_x,node_y = read_nodes(directory)
    connections = read_elements(directory)
    line_sets = separate_graphs(connections)
    
    return line_sets,node_x,node_y


def read_elements(directory):
    file_name = "elements.txt"
    file_path = os.path.join(directory, file_name)
    with open(file_path) as elements_file:
        eles = csv.reader(elements_file, delimiter=',')
        segments = []
        for ele in eles:
            a, b = ele     
            segments.append((int(a),int(b)))  
    # print(segments)
    return segments


def read_nodes(directory):
    file_name = "nodes.txt"
    file_path = os.path.join(directory, file_name)
    with open(file_path) as nodes_file: 
        nodes = csv.reader(nodes_file, delimiter=',')
        node_x = []
        node_y = []
        for node in nodes:
            x, y = node  
            node_x.append(float(x))
            node_y.append(float(y))
            # base.Newpoint(float(x), float(y), 0)          
    return node_x,node_y

   

def separate_graphs(connections):
    if len(connections) == 0:
        return []
    
    graph1 = set()
    graph2 = set()
    line_set1 = set()
    line_set2 = set()


    # 找到一个起始节点
    start_node = connections[0][0]
    graph1.add(start_node)

    while True:
        connected_nodes = []
        for node_pair in connections:
            if node_pair[0] in graph1 or node_pair[1] in graph1:
                connected_nodes.extend(node_pair)
        new_nodes = set(connected_nodes) - graph1 - graph2
        if not new_nodes:
            break
        graph1 |= new_nodes


    for idx, (node1, node2) in enumerate(connections, start=1):
        if node1 in graph1 and node2 in graph1:
            line_set1.add(idx)
        else:
            line_set2.add(idx)

    result = [[connections[i-1] for i in line_set1]]
    result.extend(separate_graphs([connections[i-1] for i in line_set2]))
    
    alone = set()
    for sublist in result:
        if len(sublist) == 1:
            alone.add(tuple(sublist))
            result.remove(sublist)

    return result

    

if __name__ == "__main__":
    directory = r"E:\#code\butto\data\input"
    line_sets,node_x,node_y = get_line_sets(directory)
    print(line_sets)
