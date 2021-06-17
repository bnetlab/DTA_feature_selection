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

# classification without feature selection
def runClassifierMulticlass(X_train,y_train_bin,X_test, y_test_bin,rindex ):
    print("scoring...")
    clf = svm.SVC(kernel='linear', C=1).fit(X_train[:,rindex], y_train_bin)
    scores = clf.score(X_test[:,rindex], y_test_bin)
    ypred = clf.predict(X_test[:,rindex])
    print(classification_report(y_test_bin, ypred))
    print(confusion_matrix(y_test_bin, ypred))
    return y_test_bin, ypred

def roc_auc_score_multiclass(actual_class, pred_class, average = "macro"):

#creating a set of all the unique classes using the actual class list
    unique_class = set(actual_class)
    roc_auc_dict = {}
    for per_class in unique_class:
        #creating a list of all the classes except the current class 
        other_class = [x for x in unique_class if x != per_class]

        #marking the current class as 1 and all other classes as 0
        new_actual_class = [0 if x in other_class else 1 for x in actual_class]
        new_pred_class = [0 if x in other_class else 1 for x in pred_class]

        #using the sklearn metrics method to calculate the roc_auc_score
        roc_auc = roc_auc_score(new_actual_class, new_pred_class, average = average)
        roc_auc_dict[per_class] = roc_auc

    print("Avg AUC:", np.array(list(roc_auc_dict.values())).mean())
    return roc_auc_dict


 # classification without feature selection
def runClassifier(X_train,y_train_bin,X_test, y_test_bin,rindex ):
    print("scoring...")
    clf = svm.SVC(kernel='linear', C=1).fit(X_train[:,rindex], y_train_bin)
    scores = clf.score(X_test[:,rindex], y_test_bin)
    ypred = clf.predict(X_test[:,rindex])
    print(classification_report(y_test_bin, ypred))
    conM=confusion_matrix(y_test_bin, ypred)
    print(conM)
    print('ROC:', roc_auc_score(y_test_bin, ypred))
    fpr, tpr, thresholds = metrics.roc_curve(y_test_bin, ypred, pos_label=1)
    aucV=metrics.auc(fpr, tpr)
    print("AUC:" ,aucV)
    print("Scored!")
    return conM[0][1], conM[1][0], aucV


