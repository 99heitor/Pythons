
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
def simData():
    t_max = 1000
    dt = 0.04
    x = 0.0
    t = 0.0
    while t < t_max:
        t = t + dt
        #x = (1 + 4*np.cos(t)) * np.cos(t)
        #y = (1 + 4*np.cos(t)) * np.sin(t)
        s = t/(np.pi)

        if s%2 < 0.02:
            print t
        x = (t) * np.cos(t)
        y = (t) * np.sin(t)
        #x = (2*np.sin(3*t)) * np.cos(t)
        #y = (2*np.sin(3*t)) * np.sin(t)
        #x = 5 + 3 * np.sin(np.radians(t))
        #y = 5 + 3 * np.cos(np.radians(t))
        yield y,x

xdata, ydata = [], []

def simPoints(simData):
    x, t = simData[0], simData[1]
    xdata.append(x)
    ydata.append(t)
    time_text.set_text(time_template%(t))
    #line.set_data(t, x)
    line.set_data(ydata, xdata)
    return line, time_text
 
##
##   set up figure for plotting:
##
fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot([], [], 'bx', ms=10)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 5)

time_template = 'Time = %.1f s'    # prints running simulation time
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
## Now call the animation package: (simData is the user function
## serving as the argument for simPoints):
ani = animation.FuncAnimation(fig, simPoints, simData, blit=False,\
     interval=5, repeat=True)
#mywriter = animation.MencoderWriter(fps=60,bitrate=30)
#ani.save('/home/heitor/uhuhuhu.mp4',writer=mywriter)
plt.show()
