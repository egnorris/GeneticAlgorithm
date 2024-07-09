import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from time import time
from skimage import filters


N = 20
RadiusBoundary = (50,80)
Domain = (180, 180)
CenterPoint = (int(Domain[0]/2), int(Domain[1]/2))
ThetaList = np.random.rand(N) * 2*np.pi
RadiusList = np.random.rand(N) * (RadiusBoundary[1] - RadiusBoundary[0]) + RadiusBoundary[0]
X = (RadiusList * np.cos(ThetaList))  + CenterPoint[0]
Y = (RadiusList* np.sin(ThetaList)) + CenterPoint[1]
df = zip(X, Y, ThetaList)
df = sorted(df, key = lambda x:x[2])
X, Y, _ = list(zip(*df))
X = list(X)
Y = list(Y)
X.append(X[0])
Y.append(Y[0])
#plt.plot(X, Y)
#plt.xlim([0,180])
#plt.ylim([0,180])
poly = Polygon(zip(X, Y))
A = np.zeros(Domain)
t = time()

for i in np.arange(CenterPoint[0]-RadiusBoundary[1],CenterPoint[0]+RadiusBoundary[1]):
    for j in np.arange(CenterPoint[1]-RadiusBoundary[1],CenterPoint[1]+RadiusBoundary[1]):
        if poly.contains(Point(j,i)):
            A[i,j] = 1
A = np.round(filters.gaussian(A, 5))
plt.imshow(A)
plt.show()