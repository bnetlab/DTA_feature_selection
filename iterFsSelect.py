import numpy as np
import pandas as pd
import scipy.io
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics

import scipy.io

def iterFsFeature1(df,k):
	scipy.io.savemat('iterIn.mat', dict(x=df,k=k))
def iterFsFeature2():
	X=scipy.io.loadmat("iterOut.mat")
	return(np.ravel(X['R']))
