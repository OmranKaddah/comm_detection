import sys
import os
import numpy as np
from karateclub import MNMF
from data_utils import load_

DATA_DIR = "./data/pyg/"



######################################################
############## SETTINGS ##################################
#########################################################
# DATASETS= [ "0","107","1684", "1912", "3437", "348","3980","414","686","698"]
# DATASETS= ["amazon","dblp","youtube"]
DATASETS = ["Cora", "CiteSeer", "Cora_ML_full", "Cora_full", "CiteSeer_full"]
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

directory = "./embedding"
try:
    os.mkdir(directory)
except:
    pass

outputs_dir= "./outputs"
try:
    os.mkdir(outputs_dir)
except:
    pass

directory_2= "./outputs/MNMF"
try:
    os.mkdir(directory_2)
except:
    pass

####################################################


print("MNMF Embedds")

for dataset in DATASETS:
    print("Now the dataset {} is processed.".format(dataset))

    # G, _, _, _  = read_facebook(dataset)
    G, _ = load_(dataset)
    G = G.to_undirected()

    model = MNMF(clusters=k_s[dataset])
    model.fit(G)
    embeddings = model.get_embedding()
    membership = model.get_memberships()
    np.save(directory+"/MNMF_{}.npy".format(dataset),embeddings)
    np.save(directory_2+"/clusterMembership_{}".format(dataset), membership)
