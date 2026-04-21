import pygame
import random
import time

from algorithms import algorithms

pygame.init()

WIDTH, HEIGHT = 1200, 800
ROWS, COLS = 2, 3

PANEL_WIDTH = WIDTH // COLS
PANEL_HEIGHT = HEIGHT // ROWS

N = 200
MIN_VAL, MAX_VAL = 10, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Comparison")
font = pygame.font.SysFont("Arial", 18, bold=True)

base_array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(N)]
arrays = [base_array.copy() for _ in range(len(algorithms))]

generators = [algo(arrays[i]) for i, (_, algo) in enumerate(algorithms)]
names = [name for name, _ in algorithms]

states = [(-1, -1, 0, N - 1) for _ in range(len(algorithms))]
finished = [False] * len(algorithms)

start_times = [time.time() for _ in range(len(algorithms))]
end_times = [None] * len(algorithms)
step_counts = [0] * len(algorithms)


def draw_panel(arr, panel_x, panel_y, name, state, is_finished, time_spent, start_time, steps):
    bar_width = PANEL_WIDTH / len(arr)
    max_val = max(arr) if arr else 1

    min_idx, max_idx, left, right = state

    for i, val in enumerate(arr):
        x = panel_x + i * bar_width
        height = (val / max_val) * (PANEL_HEIGHT - 95)
        y = panel_y + PANEL_HEIGHT - height

        if is_finished:
            color = (76, 175, 80)
        elif i < left or i > right:
            color = (76, 175, 80)
        elif i == min_idx:
            color = (33, 150, 243)
        elif i == max_idx:
            color = (244, 67, 54)
        else:
            color = (120, 120, 120)

        pygame.draw.rect(screen, color, (x, y, bar_width, height))

    pygame.draw.rect(screen, (60, 60, 60), (panel_x, panel_y, PANEL_WIDTH, PANEL_HEIGHT), 1)

    screen.blit(font.render(name, True, (255, 255, 255)), (panel_x + 10, panel_y + 10))

    if is_finished:
        t_str = f"Time: {time_spent:.2f} ms"
        color = (0, 255, 0)
    else:
        t_str = f"Time: {(time.time() - start_time) * 1000:.2f} ms"
        color = (255, 255, 0)

    screen.blit(font.render(t_str, True, color), (panel_x + 10, panel_y + 35))
    screen.blit(font.render(f"Steps: {steps}", True, (180, 180, 255)), (panel_x + 10, panel_y + 60))


clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, gen in enumerate(generators):
        if not finished[i]:
            try:
                states[i] = next(gen)
                step_counts[i] += 1
            except StopIteration:
                finished[i] = True
                end_times[i] = (time.time() - start_times[i]) * 1000

    for i in range(len(algorithms)):
        draw_panel(
            arrays[i],
            (i % COLS) * PANEL_WIDTH,
            (i // COLS) * PANEL_HEIGHT,
            names[i],
            states[i],
            finished[i],
            end_times[i],
            start_times[i],
            step_counts[i]
        )

    pygame.display.update()
    clock.tick(120)

pygame.quit()