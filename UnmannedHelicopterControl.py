import kd_tree
from time import sleep
import matplotlib.pyplot as plt

def average_point(knn_points):
    x = 0
    y = 0
    z = 0
    for point in knn_points:
        x += point[0]
        y += point[1]
        z += point[2]
    return [x/len(knn_points), y/len(knn_points), z/len(knn_points)]

def point_difference(point2, point1):
    return [point1[0]-point2[0], point1[1]-point2[1], point1[2]-point2[2]]

def normalize_vector(vector):
    v_ = (sum([i**2 for i in vector]))**0.5
    return [vector[0]/v_, vector[1]/v_, vector[2]/v_]

def fly(points, helicopter, target):
    path = [helicopter]
    flag = True

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    fig.show()

    while (flag):
        plt.pause(1)
        plt.cla()
        print("Helicopter: ", helicopter)

        tree = kd_tree.make_kd_tree(points+[helicopter]+[target], 3)
        # add points to plot
        for point in points:
            ax.scatter(point[0], point[1], point[2], color='blue')

        # helicopter
        ax.scatter(helicopter[0], helicopter[1], helicopter[2], color='red')
        # target
        ax.scatter(target[0], target[1], target[2], color='green')

        ax.plot([helicopter[0], target[0]], [helicopter[1], target[1]], [helicopter[2], target[2]], color='black')

        temp = kd_tree.get_knn(tree, helicopter, 5, 3, kd_tree.euclidean_distance)
        normal_mode = all([i[0] > 1 for i in temp])
        temp = [item[1] for item in temp]
        # camino no directo
        if (not normal_mode):            
            temp = average_point(temp)
        temp = point_difference(temp, target)
        # si la distancia es menor a 1, flag FALSE
        if (all (i < 1 for i in temp)):
            flag = False
        temp = normalize_vector(temp)
        temp = [ (helicopter[i]+ temp[i]) for i in range(3)]
        helicopter = temp
        path.append(helicopter)

        # draw lines from path 
        for i in range(len(path)-1):
            ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], [path[i][2], path[i+1][2]], color='black')

        #show figure
        plt.draw()
        
        
        # sleep(1)