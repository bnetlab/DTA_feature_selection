import pandas as pd
import numpy as np
import time
import random
import math
import os;
import sys;
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics

def selectOne(p):
    v = random.random();
    s = 0;
    for i in range(len(p)):
        s += p[i];
        if s >= v:
            return i;
    return len(p)-1;

def cssFeature(R,k):
    m,n = R.shape;
    if k > n:
        raise Exception("Weibi Algorithm requires k <= n, but k=%d, n=%d"%(k,n));    

    print("SVD starts");
    u,d,vt = np.linalg.svd(R);
    vtk    = vt[0:k, :];
    print("SVD ends");
    
    p      = np.array([0.0 for j in range(n)]);
    for j in range(n):
        p[j]  = np.linalg.norm(vt[0:k,j:j+1]);
        p[j] *= p[j];
        p[j] /= k;
    print("Probabilities calculation ends");
     
    C     = [];
    Cdict = [0 for j in range(n)];
    while len(C) < k:
        i = selectOne(p);
        if 0 ==  Cdict[i]:
            Cdict[i] = 1;
            C.append(i);
    return C


