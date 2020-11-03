import numpy as np
import pygame
import sys
import time


# pendulum
w, h = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)

screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()


def update(a, length):
    scale = 100
    # x = length * scale * np.sin(a)
    x = length * scale * np.sin(a) + w/2
    # y = length * scale * np.cos(a)
    y = length * scale * np.cos(a) + h/2
    return x, y


def render(point_sim, m):
    x = point_sim[0]
    y = point_sim[1]

    scale = 2.5

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (w/2, h/2), (x, y), 5)  # Line from center to pendulum ball
    pygame.draw.circle(screen, RED, (int(x), int(y)), int(m))  # pendulum ball
    pygame.draw.circle(screen, (128, 128, 128), (int(w/2), int(h/2)), 10)

    return

