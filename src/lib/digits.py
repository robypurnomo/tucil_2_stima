import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from lib.convexHull.ConvexHull import myConvexHull

def digits() :

    data = datasets.load_digits() 

    # create a DataFrame 
    df = pd.DataFrame(data.data, columns=data.feature_names) 
    df['Target'] = pd.DataFrame(data.target) 
    print(df.shape)
    df.head()

    # visualisasi ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('pixel_0_3 vs pixel_0_4')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[2,3]].values
        x, y = myConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        plt.plot(x, y, colors[i%2])
    plt.legend()
    plt.show()
