"""
Reference implementation of node2vec.
Author: Aditya Grover

For more details, refer to the paper:
node2vec: Scalable Feature Learning for Networks
Aditya Grover and Jure Leskovec
Knowledge Discovery and Data Mining (KDD), 2016
"""

import argparse
import networkx as nx
import node2vec
import numpy as np
from gensim.models import Word2Vec
from subprocess import call
import sys, os

from Convert_WordEmbedding_to_Json import save_word_emb, save_word_emb_with_name


def parse_args():
    # Parses the node2vec arguments.

    parser = argparse.ArgumentParser(description="Run node2vec.")

    parser.add_argument('--input', nargs='?', default='../graph/karate.edgelist',
                        help='Input graph path')

    parser.add_argument('--output', nargs='?', default='../emb/karate2.emb',
                        help='Embeddings path')

    parser.add_argument('--dimensions', type=int, default=128,
                        help='Number of dimensions. Default is 128.')

    parser.add_argument('--walk-length', type=int, default=80,
                        help='Length of walk per source. Default is 80.')

    parser.add_argument('--num-walks', type=int, default=10,
                        help='Number of walks per source. Default is 10.')

    parser.add_argument('--window-size', type=int, default=10,
                        help='Context size for optimization. Default is 10.')

    parser.add_argument('--iter', default=1, type=int,
                        help='Number of epochs in SGD')

    parser.add_argument('--workers', type=int, default=8,
                        help='Number of parallel workers. Default is 8.')

    parser.add_argument('--p', type=float, default=1,
                        help='Return hyperparameter. Default is 1.')

    parser.add_argument('--q', type=float, default=1,
                        help='Inout hyperparameter. Default is 1.')

    parser.add_argument('--weighted', dest='weighted', action='store_true',
                        help='Boolean specifying (un)weighted. Default is unweighted.')
    parser.add_argument('--unweighted', dest='unweighted', action='store_false')
    parser.set_defaults(weighted=True)

    parser.add_argument('--directed', dest='directed', action='store_true',
                        help='Graph is (un)directed. Default is undirected.')
    parser.add_argument('--undirected', dest='undirected', action='store_false')
    parser.set_defaults(directed=False)

    return parser.parse_args()


def c_parse_args():
    # Parses the node2vec arguments.

    parser = argparse.ArgumentParser(description="Run word2vec.")

    parser.add_argument('--input', nargs='?', default='raw_data',
                        help='Input graph path')

    parser.add_argument('--output', nargs='?', default='test_calling_c',
                        help='Embeddings path')
    parser.add_argument('--save-vocab', nargs='?', default='test_vocab',
                        help='vocab path')
    parser.add_argument('--alpha', type=float, default=0.1,
                        help='Learning Rate. Default is 0.1.')
    parser.add_argument('--window', type=int, default=10,
                        help='Context size for optimization. Default is 10.')
    parser.add_argument('--cbow', type=int, default=0,
                        help='cbow or skip-gram.')
    parser.add_argument('--sample', type=float, default=1e-5,
                        help='dropping high frequent word. Default is 1e-5.')
    parser.add_argument('--threads', type=int, default=20,
                        help='Number of parallel threads. Default is 20.')
    parser.add_argument('--iter', default=15, type=int,
                        help='Number of epochs in SGD')
    return parser.parse_args()


def read_graph():
    # Reads the input network in networkx.

    if args.weighted:
        G = nx.read_edgelist(args.input, nodetype=int, data=(('weight', float),), create_using=nx.DiGraph())
    else:
        G = nx.read_edgelist(args.input, nodetype=int, create_using=nx.DiGraph())
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1

    if not args.directed:
        G = G.to_undirected()

    return G


def learn_embeddings(walks):
    """
    Learn embeddings by optimizing the Skipgram objective using SGD.
    """

    walks = [map(str, walk) for walk in walks]
    print(walks)
    # ./word2vec -train raw_data -output vectors___init2_context_D_50_S_3_K_03.bin -save-vocab vocab
    # -alpha 0.50
    # -window 10 -cbow 0 -sample 1e-3 -threads 20 -binary 1 -iter 15

    model = Word2Vec(walks, size=args.dimensions, window=args.window_size, min_count=0, sg=1, workers=args.workers,
                     iter=args.iter, negative=5)

    # model.most_similar("1001")
    model.save_word2vec_format(args.output)

    return


def main(args, c_args):
    """
    Pipeline for representational learning for all nodes in a graph.
    """

    #generate corpus
    """
    nx_G = read_graph()
    G = node2vec.Graph(nx_G, args.directed, args.p, args.q)
    G.preprocess_transition_probs()
    walks = G.simulate_walks(args.num_walks, args.walk_length)
    sentences = ""

    # create raw data
    # _walks = [map(str, walk) for walk in walks]
    print("walks converted")
    for i in range(len(walks)):
        sentences += str(walks[i][0])
        for j in range(1, len(walks[i])):
            sentences += (" " + str(walks[i][j]))
        sentences += '\n'
    file = open('../corpus/' + source_name + '.txt', 'w+')
    file.write(sentences)
   

    #learn_embeddings(walks)
    call("./../Modified_DIVE/word2vec -train ../corpus/"
         +source_name+".txt -output ../emb/"+source_name+".emb "
         +source_name+"-vocab -alpha 0.10 -window 10 -cbow 0 -sample 1e-5 -threads 20 -binary 0 -iter 15",
         shell=True)
    """
    save_word_emb_with_name("../emb/"+source_name+".emb", "../json/"+source_name+"_with_name.json","../graph/"+source_name+"_id_name.net")



if __name__ == "__main__":
    args = parse_args()
    c_args = c_parse_args()
    print(c_args)
    print(vars(c_args))
    # args.directed = True
    source_name = 'social_influence_citation'

    args.input = '../graph/' + source_name + '.edgelist'
    args.output = '../emp/' + source_name + '.emb'
    main(args, c_args)
