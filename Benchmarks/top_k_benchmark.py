#! /usr/bin/env python

import random
import utilities

def get_top_k_nodes(file_name, k):
    """
    Returns a list of the top k most followed nodes
    """
    node_followers = {}

    for nodes in utilities.edges_generator(file_name):
        if nodes[1] not in node_followers:
            node_followers[nodes[1]] = 0
        node_followers[nodes[1]] += 1

    return sorted(node_followers.keys(), 
                  key=lambda n: node_followers[n], 
                  reverse = True)[:k]

def top_k_benchmark(train_file, test_file, submission_file, num_predictions):
    """
    Runs the top k benchmark
    """
    top_k_nodes = get_top_k_nodes(train_file, num_predictions)
    test_nodes = utilities.read_nodes_list(test_file)
    test_predictions = [top_k_nodes for node in test_nodes]
    utilities.write_submission_file(submission_file, 
                                    test_nodes, 
                                    test_predictions)

if __name__=="__main__":
    top_k_benchmark("../Data/train.csv",
                    "../Data/test.csv",
                     "../Submissions/top_k_benchmark.csv",
                    10)
