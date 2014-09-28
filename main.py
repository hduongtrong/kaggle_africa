import pandas as pd
from sklearn.linear_model import LassoLarsCV

def get_data(filename):
    df = pd.read_csv(filename)
    c = list(df.columns)
    df = df[c[1:]]

    df['Depth'] = (df['Depth'] == "Subsoil")+0;
    n = 1157
    return df.as_matrix()[:n,:-5], df.as_matrix()[:n,-5:],\
           #df.as_matrix()[n:,:-5], df.as_matrix()[n:,-5:]

def score(model):
    for i in xrange(5):
        print mean((Yi[:,i] - model(fit_intercept = True, 
              normalize = True, cv = 5,verbose = 2)\
              .fit(Xi, Yi[:,i]).predict(Xi))**2)

if __name__ == "__main__":
    try: Xi
    except NameError: Xi, Yi = get_data("training.csv")
    print score(LassoLarsCV)
    
