import networkx as nx
import re

def read_facebook(ds, relabel=True):

    fb_num = ds
    print('using facebook', fb_num)
    edge_fpath = '../data/facebook/{}.edges'.format(fb_num)
    label_fpath =  '../data/facebook/{}.circles'.format(fb_num)
    mapping = {}
    G = nx.Graph()
    with open(edge_fpath, 'r') as f:
        for line in f:
            e0, e1 = line.strip().split(' ')
            # print(e0, e1)
            try:
                tmp = mapping[e0]
            except:
                mapping[e0] = len(mapping)

            try:
                tmp = mapping[e1]
            except:
                mapping[e1] = len(mapping)


            G.add_edge(e0, e1)
            G.add_edge(e1, e0)
    maxindex = max(mapping.values())
    communities = []
    total_len = 0
    with open(label_fpath, 'r') as f:
        for coommunity, line in enumerate(f):
            nodes = re.split(' |\t', line.strip())[1:]
            for n in nodes:

                try:
                    tmp = mapping[n]
                except:
                    mapping[n] = len(mapping)

            communities.append(list([mapping[x] for x in nodes]))
            total_len += len(communities[coommunity])

    gt_communities = [ 0 for _ in range(maxindex+1)]

    with open(label_fpath, 'r') as f:
        for community, line in enumerate(f):
            nodes = re.split(' |\t', line.strip())[1:]
            for n in nodes:

                try:
                    tmp = mapping[n]
                except:
                    mapping[n] = len(mapping)
                if  mapping[n] > maxindex:
                    continue
                gt_communities[mapping[n]] = community

    G = nx.relabel_nodes(G, mapping)
    return G, nx.adjacency_matrix(G), gt_communities, communities


def load_(ds):
    dirpath = './data/pyg'
    edge_fpath = dirpath + '/{}_edges.txt'.format(ds)
    
    mapping = {}
    G = nx.Graph()
    with open(edge_fpath, 'r') as f:
        for line in f:
            e0, e1 = line.strip().split(' ')
            # print(e0, e1)
            try:
                tmp = mapping[e0]
            except:
                mapping[e0] = len(mapping)

            try:
                tmp = mapping[e1]
            except:
                mapping[e1] = len(mapping)


            G.add_edge(mapping[e0], mapping[e1])
            G.add_edge(mapping[e1], mapping[e0])

    return G, mapping