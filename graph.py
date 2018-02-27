def search_graph(graph, start, end):
    results = []
    generate_path(graph, [start], end, results)
    results.sort(lambda x, y: cmp(len(x), len(y)))
    return results

def generate_path(graph, path, end, results):
    node = path[-1]
    if node == end:
        results.append(path)
    else:
        for i in graph[node]:
            if i not in path:
                generate_path(graph, path+[i], end, results)

if __name__ == "__main__":
    Graph = {
             'A':['B', 'C', 'D'],
             'B':['E'],
             'C':['D', 'F'],
             'D':['B', 'E', 'G'],
             'E':[],
             'F':['D', 'G'],
             'G':['E']
            }
    results = search_graph(Graph, 'A', 'D')
    print Graph
    print ('A to D path:')
    for i in results:
        print i
