import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.axis('equal')

radius_earth = 6371  # km
radius_orbit = radius_earth + 1150  # km
earth_mu = 398600.5  # Earth's gravitational constant

def plot_earth():
    radius = 6371  # km
    theta = np.linspace(0,2*np.pi, 1000)
    plt.plot(radius*np.cos(theta), radius*np.sin(theta), 'b')

def get_period(radius_orbit, planet_mu):
    plot_earth()
    return 2*np.pi*radius_orbit**(3/2)/np.sqrt(planet_mu)

def get_true_anomaly(period,t):
    return 2*np.pi/period*t

def get_cartesian(radius, theta):
    x = radius*np.cos(theta)
    y = radius*np.sin(theta)
    return {'x': x, 'y': y}

time = 0

def plot_orbit(i):
    global time
    time += 10
    period = get_period(radius_orbit, earth_mu)
    true_anomaly = get_true_anomaly(period,time)
    coords = get_cartesian(radius_orbit, true_anomaly)
    print('coords: ',coords)
    ax1.scatter(coords['x'], coords['y'], s=1, c='r')    

def main():
    plot_earth()
    ani = animation.FuncAnimation(fig, plot_orbit, interval=10)
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Keyboard Interrupt detected: exiting...')
