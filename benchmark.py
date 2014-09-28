import pandas as pd
import numpy as np
from sklearn import svm, cross_validation
from sklearn.linear_model import LassoLarsCV
from sys import stdout

def get_data():
    global xtrain, xtest, ytrain, ytest, xout
    train = pd.read_csv('training.csv')
    test = pd.read_csv('sorted_test.csv')
    rows = list(train.index); random.shuffle(rows)
    train = train.reindex(rows)

    labels = train[['Ca','P','pH','SOC','Sand']].values

    train.drop(['Ca', 'P', 'pH', 'SOC', 'Sand', 'PIDN'], axis=1, inplace=True)
    test.drop('PIDN', axis=1, inplace=True)
    train['Depth'] = (train["Depth"] == "Subsoil") + 0
    test['Depth']  = (test["Depth"]  == "Subsoil") + 0
    xtrain, xtest = np.array(train)[:800], np.array(train)[800:]
    ytrain, ytest = labels[:800], labels[800:]
    xout = test.values

def runModel(model):
    rmse = np.zeros(5)
    for i in xrange(5):
        rmse[i] = sqrt(mean((ytest[:,i] - model.fit(xtrain,\
               ytrain[:,i]).predict(xtest))**2))
        print rmse[i]
    return rmse

def getOutput(model):
    preds = np.zeros(shape = (xout.shape[0], 5))
    for i in xrange(5):
        preds[:,i] = model.fit(vstack([xtrain, xtest]), 
               vstack([ytrain, ytest])[:,i]).predict(xout)
    sample = pd.read_csv('sample_submission.csv')
    sample['Ca'] = preds[:,0]
    sample['P'] = preds[:,1]
    sample['pH'] = preds[:,2]
    sample['SOC'] = preds[:,3]
    sample['Sand'] = preds[:,4]
    sample.to_csv('beating_benchmark2.csv', index = False)

def getRMSE(model, n=10):
    l = np.zeros(shape = (n,5))
    for i in xrange(n):
        get_data()
        stdout.write(str(i*100/n) + "%.."); stdout.flush()
        l[i] = (runModel(model))
    return l

if __name__ == "__main__":
    #try: xtrain
    #except NameError: get_data()
    sup_vec = svm.SVR(C=10000.0, verbose = 0)
    las_cv = LassoLarsCV(fit_intercept = True, normalize = True, cv = 5)
    l = getRMSE(las_cv)
