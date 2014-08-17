
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
def simData():
# this function is called as the argument for
# the simPoints function. This function contains
# (or defines) and iterator---a device that computes
# a value, passes it back to the main program, and then
# returns to exactly where it left off in the function upon the
# next call. I believe that one has to use this method to animate
# a function using the matplotlib animation package.
#
    t_max = 1000
    dt = 0.05
    x = 0.0
    t = 0.0
    while t < t_max:
        t = t + dt
        print t
        x = (2*np.cos(4*t)) * np.cos(t)
        y = (2*np.cos(4*t)) * np.sin(t)
        #x = 5 + 3 * np.sin(np.radians(t))
        #y = 5 + 3 * np.cos(np.radians(t))
        yield y,x
 
def simPoints(simData):
    x, t = simData[0], simData[1]
    time_text.set_text(time_template%(t))
    line.set_data(t, x)
    return line, time_text
 
##
##   set up figure for plotting:
##
fig = plt.figure()
ax = fig.add_subplot(111)
# I'm still unfamiliar with the following line of code:
line, = ax.plot([], [], 'bs', ms=10)
ax.set_ylim(-5, 5)
ax.set_xlim(-6, 6)
##
time_template = 'Time = %.1f s'    # prints running simulation time
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
## Now call the animation package: (simData is the user function
## serving as the argument for simPoints):
ani = animation.FuncAnimation(fig, simPoints, simData, blit=False,\
     interval=10, repeat=True)
#mywriter = animation.MencoderWriter(fps=60,bitrate=30)
#ani.save('/home/heitor/uhuhuhu.mp4',writer=mywriter)
plt.show()