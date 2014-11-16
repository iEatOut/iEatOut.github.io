import matplotlib.pyplot as plt
import numpy as np
import pylab
from ordrinTesterNew import get_restaurants

#Add labels
#Color code
#Add title
###filename = "C:\Users\Anirudh\Desktop\iEatOut.github.io\python\data.txt"
#filename = "data.txt" 
'''
with open(filename) as f:
    datum = f.readlines()
    polyShape = []
    f = open(filename)
    datum = f.readlines()
    f.close()
    import csv
    reader = csv.reader(datum)
    for i in datum:
        polyShape.append(i.split('\t'))
    #polyShape[0] =
    '''
from matplotlib.pyplot import figure, show
import numpy as npy
from numpy.random import rand
def priceGraph(address, city, zip, allergy, nutrition):
    polyShape = get_restaurants(address, city, zip, allergy, nutrition)

    polyShapeName = []
    polyShapePrice = []
    polyShapeAllergy = []
    polyShapeNutrition = []
    for i in range(len(polyShape)):
        for j in range(len(polyShape[i])):
            if(j == 0):
                polyShapeName.append(polyShape[i][j])
            if(j == 1):
                polyShapePrice.append(polyShape[i][j])
            if(j==2):
                polyShapeAllergy.append(polyShape[i][j])
            if(j==3):
                polyShapeNutrition.append(polyShape[i][j])
    print(polyShapeName)
    if 1: # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)

        x, y, c, s = rand(4, 100)
        def onpick3(event):
            ind = event.ind
            print 'onpick3 scatter:', ind, npy.take(x, ind), npy.take(y, ind)

        fig = figure()
        ax1 = fig.add_subplot(111)
        ax1.get_xaxis().tick_bottom()  
        ax1.get_yaxis().tick_left()
        ax1.spines["top"].set_visible(False)  
        ax1.spines["bottom"].set_visible(True)  
        ax1.spines["right"].set_visible(False)  
        ax1.spines["left"].set_visible(True)
        ax1.grid('on')
        ttl = ax1.title
        ttl.set_weight('bold')
        plt.title("Overall Health by Restaurant Against Price")
        plt.xlabel("Conducivity to Your Allergy")
        plt.ylabel("Average Price of Restaurant")
        plt.axis([0, 1.02, 0, 100])
        plt.tick_params(axis="both", which="both", bottom="off", top="off",  
                    labelbottom="on", left="off", right="off", labelleft="on") 
        x1 = [1]
        x2 = [1]
        x = polyShapeAllergy
        y = polyShapePrice
        col = ax1.scatter(x1, x2,marker='+', s=150, linewidths=4, c='r', cmap=plt.cm.coolwarm)
        cola = ax1.scatter(x, y,marker='+', s=150, linewidths=4, c='b', cmap=plt.cm.coolwarm)
        for i, txt in enumerate(polyShapeName):
            ax1.annotate(txt, (x[i],y[i]))   
        plt.legend((col,cola),
            ('You (Ideal)', 'Each Restaurant'),
            scatterpoints=1,
            loc='lower left',
            ncol=3,
            fontsize=8)
        fig.savefig('C:\Users\IMSA Student\Desktop\iEatOut.github.io\python\outputprice.jpg')

#data = priceGraph("715 Techwood Drive", "Atlanta", "30332", ["Gluten-Free"], ["Low Sodium"])
