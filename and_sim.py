import pandas as pd
import numpy as np
from joblib import Parallel, delayed

def multiple(a, b):
        return sum(np.logical_and(a,b))

def and_sim_prl(X):
    res = Parallel(n_jobs=16)(delayed(multiple)(a=i, b=j) for i in X for j in X)
    return np.array(res).reshape(len(X),len(X))