from random import choice
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from lib.convexHull.ConvexHull import myConvexHull

def digits() :

    data = datasets.load_digits() 

    # create a DataFrame 
    df = pd.DataFrame(data.data, columns=data.feature_names) 
    df['Target'] = pd.DataFrame(data.target) 
    print("Ukuran data :", df.shape)
    print()
    df.head()

    print("Pilih 2 data yang akan digunakan! (angka)")
    nomor = 1
    for i in data.feature_names :
        print(str(nomor) + ".", i)
        nomor += 1

    print()
    choice_x = int(input("Data pertama >> "))
    choice_y = int(input("Data kedua >> "))


    # visualisasi ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('Convex Hull Result')
    plt.xlabel(data.feature_names[choice_x-1])
    plt.ylabel(data.feature_names[choice_y-1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[choice_x-1,choice_y-1]].values
        x, y = myConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        plt.plot(x, y, colors[i%2])
    plt.legend()
    plt.show()
