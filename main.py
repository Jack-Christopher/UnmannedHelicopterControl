import numpy as np
import UnmannedHelicopterControl as UHC

#populate kd-tree
points = np.random.rand(30, 3)
# convert numpy array to list
points = points.tolist()
#round points to 2 decimal places
points = [[round(point[0]*20, 1), round(point[1]*20, 1), round(point[2]*20, 1)] for point in points]
print(points)

helicopter = points[0]
target = points[-1]

points = points[1:-1]


# plot path 
UHC.fly(points, helicopter, target)