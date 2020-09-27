import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import sys
import time
dt = 0.01
t = np.arange(0, 60+dt, dt)
g = 9.81
l = 2

x = np.zeros(len(t))
xd = np.zeros(len(t))
xdd = np.zeros(len(t))

for i in range(len(t)):
    if i == 0:
        x[i] = np.pi/6 # initial condition
        xd[i] = -4.3 # initial condition
        xdd[i] = -g/l*np.sin(x[i])
    else:
        xdd[i] = -g/l*np.sin(x[i-1])
        xd[i] = xd[i-1] + dt*xdd[i]
        x[i] = x[i-1] + dt*xd[i]

print(xdd[0:10])
print(xd[0:10])
print(x[0:10])

# plt.plot(t, x)
# plt.show()

w, h = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)

screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()



def update(a1_sim):
    scale = 100
    x1 = l*scale * np.sin(a1_sim) + 400
    y1 = l*scale * np.cos(a1_sim) + 400

    return x1, y1

def render(point_sim, m1):
    x1 = point_sim[0]
    y1 = point_sim[1]

    scale = 5

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (400, 400), (x1, y1), 5)
    pygame.draw.circle(screen, RED, (int(x1), int(y1)), int(m1*scale))

    return


a1 = np.pi/6

tStart = time.time()
tAccumulated = 0
for i in range(len(t)):
    tStep_start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Update step
    point = update(a1)

    # Render step
    render(point, m1=8)

    a1 = x[i]

    # clock.tick(60)
    pygame.display.update()
    tStep = time.time() - tStep_start
    if tStep < dt:
        time.sleep(dt-tStep)
    else:
        tAccumulated += tStep-dt
        print("Accumulated over pass time:", tAccumulated, "[s]")
tEnd = time.time()

print("Simulation time", (tEnd-tStart))
# while True:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     # Update step
#     point = update(a1)
#
#     # Render step
#     render(point, 5)
#
#     a1 += 0.01
#
#     clock.tick(60)
#     pygame.display.update()
