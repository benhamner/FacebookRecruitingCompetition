#! /usr/bin/env python

from collections import deque
import utilities

def breadth_first_search(graph, node, num_nodes):
    """
    Does a breadth-first search of the graph starting at the node.
    Returns the first num_nodes nodes (excluding direct neighbors)
    """
    neighbors = set(graph[node])
    looked_at = set(graph[node])
    looked_at.add(node)
    visited = []
    queue = deque(graph[node])

    while queue and len(visited)<num_nodes:
        next_node = queue.popleft()
        if next_node not in neighbors:
            visited.append(next_node)
        queue.extend(n for n in graph[next_node] if n not in looked_at)
        looked_at.update(graph[next_node])

    return visited

def bfs_benchmark(train_file, test_file, submission_file, num_predictions):
    """
    Runs the breadth-first search benchmark.
    """
    graph = utilities.read_graph(train_file)
    test_nodes = utilities.read_nodes_list(test_file)
    test_predictions = [breadth_first_search(graph, node, num_predictions)
                        for node in test_nodes]
    utilities.write_submission_file(submission_file, 
                                    test_nodes, 
                                    test_predictions)

if __name__=="__main__":
    bfs_benchmark("../Data/train.csv",
                  "../Data/test.csv",
                  "../Submissions/bfs_benchmark_updated.csv",
                  10)
