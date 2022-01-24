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

def main():
    directory = '../cube.txt'
    toggleplot=1
    points_list = GetPoints(directory)
    XLINES=[]
    YLINES=[]
    ZLINES=[]
    for inc_lines in range(0,len(points_list)):
        X, Y, Z = [], [],[]
        for inc_pts in range(0, len(points_list[inc_lines])):
            X.append(float(points_list[inc_lines][inc_pts][0]))
            Y.append(float(points_list[inc_lines][inc_pts][1]))
            Z.append(float(points_list[inc_lines][inc_pts][2]))
        XLINES.append(X)
        YLINES.append(Y)
        ZLINES.append(Z)


    if toggleplot ==1:
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot(XLINES[0], YLINES[0], ZLINES[0], color="red")
        ax.plot(XLINES[1], YLINES[1], ZLINES[1], color="blue")
        ax.plot(XLINES[2], YLINES[2], ZLINES[2], color="black", alpha=0.25)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
        plt.close()

if __name__ == '__main__':
    main()
