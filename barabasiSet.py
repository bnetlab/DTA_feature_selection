import numpy as np
import pandas as pd
from scipy.stats import binom

def peep (df_Z, cutoff=2.5):
    """
    Peep from normalized dataframe
    Args:
    df_Z (dataFrame): normalized expresion, cutoff (float): peep cutoff
    Return:
    df_de (dataFrame): peep profile
    
    """
    df_de_up=(df_Z>cutoff).astype(int)
    df_de_down=(df_Z<-1*cutoff).astype(int)
    df_de=df_de_up + df_de_down
    return df_de

def findX(df,p):
    for i in range(100):
        a= df.shape[1]*(1-binom.cdf(i,df.shape[0],p))
        if a < 1:
            break
    return i+1

def barabasiSet(df,dfy,cutoff=2.5):
	"""
	Get barabasi geneset from disease and control sample
	Augs:
	df1 (dataframe) :normal data, df2 (dataframe) :disease data, cutoff (float): DE cutoff
	return:
	G (list): barabasi DE genes
	"""
	df2=df[pd.DataFrame(dfy).astype(bool).values]
	df1=df[~(pd.DataFrame(dfy).astype(bool)).values]

	df1_mean=df1.mean()
	df1_std=df1.std()
	# z score
	df1_Z=(df1-df1_mean)/df1_std
	df2_Z=(df2-df1_mean)/df1_std
	df1_de=peep(df1_Z,cutoff)
	df2_de=peep(df2_Z,cutoff)
	print(df2_de.shape)
	p= np.mean(df1_de.sum(axis=1))/df1.shape[1]
	X1=findX(df1_de,p)
	X2=findX(df2_de,p)
	gs1=df1_de.loc[:, (df1_de.sum(axis=0) > X1).values].columns
	gs2=df2_de.loc[:, (df2_de.sum(axis=0) > X2 ).values].columns
	d = pd.DataFrame()
	d['df2']=gs2
	d['df2_sum']=df2_de[gs2].sum(axis=0).values
	return d

def peepMat(df,dfy,cutoff=2.5):

	df2=df[pd.DataFrame(dfy).astype(bool).values]
	df1=df[~(pd.DataFrame(dfy).astype(bool)).values]

	df1_mean=df1.mean()
	df1_std=df1.std()
	# z score
	df1_Z=(df1-df1_mean)/df1_std
	df2_Z=(df2-df1_mean)/df1_std
	df1_de=peep(df1_Z,cutoff)
	df2_de=peep(df2_Z,cutoff)
	df_new = pd.concat([df2_de, df1_de])

	return df_new, df1_mean, df1_std, pd.concat([df2_Z, df1_Z])

def testPeep(df,mean,sd, cutoff=2.5):
	# z score
	df_Z=(df-mean)/sd
	df_de=peep(df_Z,cutoff)
	return df_de

def peepMatUnsupervised(df,cutoff=2.5):
	""" This convert expresion data to PEEP matrix (ignore  class label)

	Args:
		df (dataframe) : gene expresion matrix
		cutoff(double) : cutoff for z-score
	Returns:
		df_P(ndarray) : PEEP matrix
		df_mean(vector) : mean expression of each gene
		df_std (vector) : std of each gene expression
		df_Z (ndarray) : Z-score matrix
 	"""

	df_mean=df.mean()
	df_std=df.std()
	# z score
	df_Z=(df-df_mean)/df_std
	df_de=peep(df_Z,cutoff)

	return df_de, df_mean, df_std, df_Z

def peepMatRow(df,cutoff=2.5):
	""" This convert expresion data to PEEP matrix by rowwise normalization(ignore class label) 

	Args:
		df (dataframe) : gene expresion matrix
		cutoff(double) : cutoff for z-score
	Returns:
		df_P(ndarray) : PEEP matrix
		df_mean(vector) : mean expression of each gene
		df_std (vector) : std of each gene expression
		df_Z (ndarray) : Z-score matrix
 	"""

	df_mean = df.mean(axis=1)
	df_std = df.std(axis=1)
	# z score
	df_Z = df.subtract(df_mean, axis=0)
	df_Z = df_Z.divide(df_std, axis=0)
	df_de = peep(df_Z, cutoff)

	return df_de, df_mean, df_std, df_Z