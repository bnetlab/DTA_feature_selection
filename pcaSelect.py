import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score
import time
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn import metrics
from sklearn.decomposition import PCA

def pcaFeature(df,k):
	start_time = time.time()
	n_comp = df.shape[0]-1
	pca_trafo = PCA(n_components=n_comp)
	pca_data = pca_trafo.fit_transform(df)
	pca_inv_data = pca_trafo.inverse_transform(np.eye(n_comp))
	pca_inv_data_mean=pca_inv_data.mean(axis=0)
	df_pca_inv_data_mean= pd.DataFrame(pca_inv_data_mean)
	print("--- %s seconds ---" % (time.time() - start_time))
	top_feature=df_pca_inv_data_mean.sort_values(by=0, ascending=False)[0:k].index.tolist()
	return top_feature


