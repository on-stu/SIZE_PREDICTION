def cluster(X, title):
    from sklearn.cluster import KMeans
    import seaborn as sns
    import matplotlib
    import matplotlib.pyplot as plt

    ###################################################################
    # clusetring with k=3,4,5
    ## model 
    cluster_m1=KMeans(n_clusters=3,n_init=10,max_iter=500,algorithm="auto")
    cluster_m2=KMeans(n_clusters=4,n_init=10,max_iter=500,algorithm="auto") 
    cluster_m3=KMeans(n_clusters=5,n_init=10,max_iter=500,algorithm="auto")

    ## fitting
    cluster_m1.fit(X)
    cluster_m2.fit(X)
    cluster_m3.fit(X)

    ## add predicted value
    X1=X.copy() 
    X2=X.copy() 
    X3=X.copy()

    X1["clu"]=cluster_m1.predict(X)
    X2["clu"]=cluster_m2.predict(X)
    X3["clu"]=cluster_m3.predict(X)
    ## plot
    matplotlib.rcParams['font.family'] ='D2Coding'
    plot_1=sns.pairplot(X1,hue="clu")
    plot_1.fig.suptitle("clustering with k=3",y=1.05)
    plt.savefig(f'{title}with3.png')
    plot_2=sns.pairplot(X2,hue="clu")
    plot_2.fig.suptitle("clustering with k=4",y=1.05)
    plt.savefig(f'{title}with4.png')
    plot_3=sns.pairplot(X3,hue="clu")
    plot_3.fig.suptitle("clustering with k=5",y=1.05)
    plt.savefig(f'{title}with5.png')

def cluster_prediction(X,y,given_X, title): # X : data for clustering, given_X : height, weight 
    import numpy as np
    from sklearn.cluster import KMeans
    import seaborn as sns
    import matplotlib
    import matplotlib.pyplot as plt
    from sklearn.model_selection import cross_val_score 
    from sklearn.ensemble import RandomForestRegressor
    ###################################################################
    # clusetring with k=3,4,5
    ## model 
    cluster_m1=KMeans(n_clusters=3,n_init=10,max_iter=500,algorithm="auto")
    cluster_m2=KMeans(n_clusters=4,n_init=10,max_iter=500,algorithm="auto") 
    cluster_m3=KMeans(n_clusters=5,n_init=10,max_iter=500,algorithm="auto")

    ## fitting
    cluster_m1.fit(X)
    cluster_m2.fit(X)
    cluster_m3.fit(X)

    ## add predicted value
    X1=X.copy() 
    X2=X.copy() 
    X3=X.copy()

    X1["clu"]=cluster_m1.predict(X)
    X2["clu"]=cluster_m2.predict(X)
    X3["clu"]=cluster_m3.predict(X)
    ## plot
    matplotlib.rcParams['font.family'] ='D2Coding'
    plot_1=sns.pairplot(X1,hue="clu")
    plot_1.fig.suptitle("clustering with k=3",y=1.05)
    plt.savefig(f'{title}with3.png')
    plot_2=sns.pairplot(X2,hue="clu")
    plot_2.fig.suptitle("clustering with k=4",y=1.05)
    plt.savefig(f'{title}with4.png')
    plot_3=sns.pairplot(X3,hue="clu")
    plot_3.fig.suptitle("clustering with k=5",y=1.05)
    plt.savefig(f'{title}with5.png')
        ##########################################################
        # Machine learning model training
        ## Cross-Validation -> choose k

    ### data
    given_X_1=given_X.copy()
    given_X_2=given_X.copy()
    given_X_3=given_X.copy()

    given_X_1["clu"]=cluster_m1.predict(X)
    given_X_2["clu"]=cluster_m2.predict(X)
    given_X_3["clu"]=cluster_m3.predict(X)

    ### modeling
    model=RandomForestRegressor()
    scores_1=cross_val_score(model,given_X_1,y,cv=10,scoring='neg_mean_squared_error')
    scores_1=np.sqrt(-1*scores_1)
    scores_2=cross_val_score(model,given_X_2,y,cv=10,scoring='neg_mean_squared_error')
    scores_2=np.sqrt(-1*scores_2)
    scores_3=cross_val_score(model,given_X_3,y,cv=10,scoring='neg_mean_squared_error')
    scores_3=np.sqrt(-1*scores_3)
    rmse_mean=[scores_1.mean(),scores_2.mean(),scores_3.mean()]
    rmse_std=[scores_1.std(),scores_2.std(),scores_3.std()] 
    return (rmse_mean,rmse_std)