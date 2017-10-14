from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [1,2,3,4,5,6,7,8,9,10]
Y = [5,6,2,3,13,4,1,2,4,8]
Z = [2,3,3,3,5,6,9,11,9,10]

def plot_3d():
    ax.scatter(X, Y, Z, c='r', marker='o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()

def update_x(X):
    return X + 0.5

def main():
    ani = animation.FuncAnimation(fig, plot_3d, interval=10)
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except Keyboardinterrupt:
        print('KeyboardInterrupt detected: exiting...')
