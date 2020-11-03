import numpy as np
import matplotlib.pyplot as plt
import pygame
from single_pendulum.animation import pygames_animation
from pygame.locals import *
import sys
import time

dt = 0.01
t = np.arange(0, 60 + dt, dt)
g = 9.81
l = 2.5
m = 50

p = np.zeros(len(t))
pd = np.zeros(len(t))
pdd = np.zeros(len(t))

for i in range(len(t)):
    if i == 0:
        rad = 170*np.pi/180
        p[i] = rad  # initial condition
        pd[i] = 0  # initial condition
        pdd[i] = 0
    else:
        pdd[i] = -(g / l) * np.sin(p[i - 1])
        pd[i] = pd[i - 1] + dt * pdd[i]
        p[i] = p[i - 1] + dt * pd[i]

figure, axis = plt.subplots(2)
axis[0].plot(t, p)
plt.show()

a = p[0]

tStart = time.time()
tAccumulated = 0
for i in range(len(t)):
    tStep_start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Update step
    point = pygames_animation.update(a, length=l)
    # Render step
    pygames_animation.render(point, m=m)

    a = p[i]

    # clock.tick(60)
    pygame.display.update()
    tStep = time.time() - tStep_start
    if tStep < dt:
        time.sleep(dt - tStep)
    else:
        tAccumulated += tStep - dt
        print("Accumulated over pass time:", tAccumulated, "[s]")
tEnd = time.time()

print("Simulation time", (tEnd - tStart))
