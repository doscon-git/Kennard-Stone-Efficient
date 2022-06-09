import os
import json
import KS_Sampling as ks
import numpy as np

"""
Goes through all files and creates kennard stone selections
from the files.
"""

WORKING_DIR = os.path.dirname(__file__)
dockerdata_path = os.path.join(WORKING_DIR,"dockerdata")
with open(os.path.join(dockerdata_path,"config.json"),"r") as infile:
    config = json.load(infile)


n_sample = 5000
n_feature = 100
X = np.random.randn(n_sample, n_feature)
X *= 100

ks_sample = ks.ks_sampling(X, n_result=config["n_result"])
print(ks_sample[0])
if os.path.exists(dockerdata_path):
    print(os.listdir(dockerdata_path))
    np.savetxt(os.path.join(os.path.dirname(__file__),"dockerdata","selection.csv"),ks_sample[0],delimiter=",")
    np.savetxt(os.path.join(os.path.dirname(__file__),"dockerdata","remainder.csv"),ks_sample[1],delimiter=",")