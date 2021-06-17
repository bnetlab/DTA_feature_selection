import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score
from random import sample

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics

def randomFeature(df,k):
	return(np.array(sample(range(df.shape[1]), k)))
