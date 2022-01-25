import numpy as np
import math
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def GetPoints(DIRECTORY):
    f = open(DIRECTORY, "r")
    LINES, LINE = [],[]
    contents = f.readlines()
    for k in range(0,len(contents)):
        if contents[k][0] == "l":
            if LINE != []:
                LINES.append(LINE)
            LINE=[]
        else:
            LINE.append(contents[k].split("\n")[0].split(","))
    return LINES

def GetLines(PL):
    N = len(PL)
    VECTORS=[]
    for j in range(0,N):
        VECTOR=[]
        for k in range (1, len(PL[j])):
            VECTOR.append([float(PL[j][k][0])-float(PL[j][k-1][0]),float(PL[j][k][1])-float(PL[j][k-1][1]),float(PL[j][k][2])-float(PL[j][k-1][2])])
        VECTORS.append(VECTOR)
    return VECTORS

def DotProduct3D(VECT1, VECT2):
    product = (VECT1[0]*VECT2[0])+(VECT1[1]*VECT2[1])+(VECT1[2]*VECT2[2])
    return product

def VectorRejection(VECT1, VECT2):
    MAG = math.sqrt((VECT1[0]-VECT2[0])**2+(VECT1[1]-VECT2[1])**2+(VECT1[2]-VECT2[2])**2)
    return MAG


def main():
    directory = '../lines.txt'

    toggleplot=1
    points_list = GetPoints(directory)
    line_list = GetLines(points_list)

    radius =5
    N_view = 120
    theta_inc = 2*math.pi/N_view
    azi_inc = theta_inc

    ViewPoints = np.empty((N_view, N_view, 3))
    Norms = np.empty((N_view, N_view, 3))
    Lengths = np.empty((N_view, N_view, len(line_list[0])))
    surprise = np.empty((N_view, N_view, 1))

    #Load the ViewPoints array, Norms array, and compute projection lengths
    for th in range(0,N_view):
        for az in range(0,N_view):
            ViewPoints[th, az] = [radius*math.cos(th*theta_inc)*math.sin(az*azi_inc),radius*math.sin(th*theta_inc)*math.sin(az*azi_inc),radius*math.cos(az*azi_inc)]
            Norms[th, az] = [-math.cos(th*theta_inc)*math.sin(az*azi_inc),-math.sin(th*theta_inc)*math.sin(az*azi_inc),-math.cos(az*azi_inc)]
            for inc1 in range(0,len(line_list)):
                LEN=0
                for inc2 in range(0,len(line_list[inc1])):
                    Projection = DotProduct3D(Norms[th, az],line_list[inc1][inc2])
                    Rejection = VectorRejection(line_list[inc1][inc2],Projection*Norms[th, az])
                    LEN+=Rejection
                Lengths[th, az, inc1] = LEN
            surprise[th, az, 0] = Lengths[th, az, 1] - Lengths[th, az, 0]

    if toggleplot ==1:
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.scatter3D(ViewPoints[:,:,0], ViewPoints[:,:,1], ViewPoints[:,:,2], color="green")
        plt.title("View Points")
        plt.show()
        plt.close()
        fig = plt.figure()
        ax1 = plt.axes(projection="3d")
        plt.title("Apparent Lengths")
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_zlabel('z')
        colors = cm.ScalarMappable(cmap="Blues").to_rgba(Lengths[:,:,0])
        ax1.plot_surface(ViewPoints[:,:,0], ViewPoints[:,:,1],ViewPoints[:,:,2],rstride=1,cstride=1,facecolors=colors)
        plt.show()
        plt.close()
        fig = plt.figure()
        ax1 = plt.axes(projection="3d")
        plt.title("Apparent Lengths")
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_zlabel('z')
        colors = cm.ScalarMappable(cmap="Reds").to_rgba(Lengths[:,:,1])
        ax1.plot_surface(ViewPoints[:,:,0], ViewPoints[:,:,1],ViewPoints[:,:,2],rstride=1,cstride=1,facecolors=colors)
        plt.show()
        plt.close()
        fig = plt.figure()
        ax1 = plt.axes(projection="3d")
        plt.title("Apparent Length Delta")
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_zlabel('z')
        colors = cm.ScalarMappable(cmap="seismic").to_rgba(surprise[:,:,0])
        ax1.plot_surface(ViewPoints[:,:,0], ViewPoints[:,:,1],ViewPoints[:,:,2],rstride=1,cstride=1,facecolors=colors)
        plt.show()
        plt.close()
        plt.hist(Lengths[:,:,0].reshape(N_view*N_view), bins=100, alpha=0.5, color='blue', density=True)
        plt.show()
        plt.close()
        plt.hist(Lengths[:,:,1].reshape(N_view*N_view), bins=100, alpha=0.5, color='red', density=True)
        plt.show()
        plt.close()
        plt.hist(surprise[:,:,0].reshape(N_view*N_view), bins=100, density=True)
        plt.show()


if __name__ == '__main__':
    main()
