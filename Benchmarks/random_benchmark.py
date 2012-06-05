#! /usr/bin/env python

import random
import utilities

def read_nodes_from_training(file_name):
    """
    Returns a list of all the nodes in the graph
    """
    node_set = set()

    for nodes in utilities.edges_generator(file_name):
        for node in nodes:
            node_set.add(node)

    return list(node_set)

def random_benchmark(train_file, test_file, submission_file, num_predictions):
    """
    Runs the random benchmark.
    """
    nodes = read_nodes_from_training(train_file)
    test_nodes = utilities.read_nodes_list(test_file)
    test_predictions = [[random.choice(nodes) for x in range(num_predictions)]
                        for node in test_nodes]
    utilities.write_submission_file(submission_file, 
                                    test_nodes, 
                                    test_predictions)

if __name__=="__main__":
    random_benchmark("../Data/train.csv",
                     "../Data/test.csv",
                     "../Submissions/random_benchmark.csv",
                     10)

