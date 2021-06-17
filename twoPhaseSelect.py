import pandas as pd
import numpy as np
import random
import math
import os;
import sys;
import scipy.io
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics

import time


#initial_stage
def initial_stage(A, k, times=None):
    row,col = A.shape;
    u,d,vt  = np.linalg.svd(A); 
    p       = np.array([0.0 for i in range(col)]);
    for j in range(col):
        for i in range(k):
            p[j] +=  vt[i,j]*vt[i,j];
        p[j] /= k;

    #c in pratice
    if None == times:
        c = 6 * k;
    else:
        c = times * k;
        c = int(ceil(c));

    return u,d,vt,p,c;


def selectOne(p):
    v = random.random();
    s = 0;
    for i in range(len(p)):
        s += p[i];
        if s >= v:
            return i;
    return len(p)-1;

def randomized_stage(A, k, vt, p, c):
    row,col = A.shape;
    S1 = np.array([0.0 for j in range(c)]); 
    D1 = np.array([0.0 for j in range(c)]);

    vkts1d1 = np.array([[0.0 for j in range(c)] for i in range(k)]);
    for t in range(c):
        i = selectOne(p); # check here 
        S1[t] = i;
        D1[t] = 1.0 / math.sqrt( c * p[i] );
        for r in range(k):
            vkts1d1[r,t] = vt[r,i] * D1[t];

    return vkts1d1, S1, D1;
# determinestic stage

def deterministic_stage_matlab(vts1d1,k):
    row,col      = vts1d1.shape;
    hat          = np.zeros([col,col]);
    hat[0:row,:] = vts1d1;
    return hat

def twoPhaseFeature1 (X_train,k):
	import time
	start_time = time.time()
	u,d,vt,p,c=initial_stage(X_train,k)
	vkts1d1, s1, d1=randomized_stage(X_train,k,vt,p,c)
	s2 = deterministic_stage_matlab(vkts1d1, k)
	print("--- %s seconds ---" % (time.time() - start_time))
	scipy.io.savemat('testin.mat', dict(x=s2,k=k))
	return s1

def twoPhaseFeature2(s1,k):
	X=scipy.io.loadmat("testout.mat")
	s2=X['p']
	print(s2.shape)
	top_feature10  =  np.array(list(range(k)));
	for i in range(k):
	    top_feature10[i] = s1[s2[0][i]-1];
	return top_feature10
