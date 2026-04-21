import pygame
import time
import random

from algorithms import algorithms

pygame.init()
screen = pygame.display.set_mode((1000, 600))
font = pygame.font.SysFont(None, 24)

def generate_array(n):
    return [random.randint(10, 100) for _ in range(n)]

def draw_array(arr, x, y, w, h):
    bar_w = w // len(arr)
    for i, val in enumerate(arr):
        pygame.draw.rect(screen, (100, 100, 100),
                         (x + i * bar_w, y + h - val * 3, bar_w - 1, val * 3))

def draw_text(text, x, y):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (x, y))

base = generate_array(50)

arrays = []
times = []
ops = []
names = []

for name, algo in algorithms:
    arr = base.copy()

    start = time.time()
    operations = algo(arr)
    end = time.time()

    arrays.append(arr)
    times.append(round(end - start, 4))
    ops.append(operations)
    names.append(name)

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    w = 500
    h = 300

    for i in range(len(arrays)):
        x = (i % 2) * w
        y = (i // 2) * h

        draw_array(arrays[i], x, y, w, h)

        draw_text(names[i], x + 10, y + 10)
        draw_text(f"time: {times[i]} s", x + 10, y + 30)
        draw_text(f"ops: {ops[i]}", x + 10, y + 50)

    pygame.display.update()

pygame.quit()
