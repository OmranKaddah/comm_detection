import sys
import os
import numpy as np

import networkx as nx

from data_utils import load_

DATA_DIR = "./data/pyg/"



######################################################
############## SETTINGS ##################################
#########################################################
fracs = { "Cora": 0.0517, "PubMed": 0.003, "CiteSeer": 0.036, "wiki-cs":0.011, "CiteSeer_full":0.03, "Cora_ML_full":0.04, 
        "DBLP": 0.02, "Cora_full": 0.02}

DATASETS= ["Cora", "CiteSeer", "Cora_ML_full", "Cora_full", "CiteSeer_full","amazon","dblp","youtube"]
# DATASETS = ["amazon"]
k_s = {
"Cora": 7,
"CiteSeer": 6,
"CiteSeer_full": 6,
"Cora_ML_full": 7,
"Cora_full": 70,
"0" : 24 ,
"107" : 9 ,
"1684" : 17 ,
"1912"  :46 ,
"3437" : 32 ,
"348" : 14 ,
"3980": 17 ,
"414":  7 ,
"686"  :14 ,
"698"  :13,
"amazon": 5,
"dblp": 5,
"youtube":5
}

reindexed = "./reindexed/"
try:
    os.mkdir(reindexed)
except:
    pass

# alg= "MNMF"
alg = "GEMSEC"


directory = "./reindexed/" + alg
try:
    os.mkdir(directory)
except:
    pass

####################################################


for dataset in DATASETS:
    print("Now the embedding of {} is reindexed to the orignal node indexing.".format(dataset))


    G, mapping = load_(dataset)
    inv_map = {}
    for key in mapping.keys():
        inv_map[mapping[key]] = key
    embs = np.load("embedding/"+alg+"_"+dataset+".npy")
    new_embs = np.zeros_like(embs)
    membership = np.load("outputs/"+alg+"/clusterMembership_"+dataset+".npy", allow_pickle=True)
    membership = membership.flat[0]
    new_membership = np.zeros((embs.shape[0],1))

    for ix in range(embs.shape[0]):
        new_embs[int(inv_map[ix])] = embs[ix]
        new_membership[int(inv_map[ix])] = membership[ix]

    np.save(reindexed+ alg+ "_"+dataset, new_embs)
    np.save(directory+"/clutsterMembership_"+dataset, new_membership)