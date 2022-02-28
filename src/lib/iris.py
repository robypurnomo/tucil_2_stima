import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from lib.convexHull.ConvexHull import myConvexHull

def iris() :

    data = datasets.load_iris() 

    # create a DataFrame 
    df = pd.DataFrame(data.data, columns=data.feature_names) 
    df['Target'] = pd.DataFrame(data.target) 
    print(df.shape)
    df.head()

    # visualisasi ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('petal Width vs petal Length')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[0,1]].values
        x, y = myConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        plt.plot(x, y, colors[i])
    plt.legend()
    plt.show()
