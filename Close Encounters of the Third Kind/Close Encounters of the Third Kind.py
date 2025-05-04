# Close Encounters of the Third Kind
# Copyright (C) 2024, Sourceduty - All Rights Reserved.
# Interactive light board with a 5x6 grid of cells, where each cell can display various colors.
# Users can activate different patterns by pressing keys (1 through 6) on the keyboard.

import pygame
import time
import random

pygame.init()

cols, rows = 5, 6
grid_width = 220

screen_width = cols * grid_width
screen_height = 600  
grid_height = screen_height // rows  

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Close Encounters Light Board")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
PINK = (255, 105, 180)

light_colors = [
    [BLACK for _ in range(cols)] for _ in range(rows)
]

patterns = [
    [
        [YELLOW, BLACK, BLACK, GREEN, BLACK],
        [BLACK, BLACK, BLACK, BLACK, WHITE],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK]
    ],
    [
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, ORANGE, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, ORANGE, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK]
    ],
    [
        [PINK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, PURPLE, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK]
    ],
    [
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, PURPLE],
        [BLACK, BLACK, BLACK, BLACK, BLACK]
    ],
    [
        [YELLOW, BLACK, BLACK, GREEN, BLACK],
        [BLACK, ORANGE, BLACK, BLACK, BLACK],
        [PINK, BLACK, BLACK, PURPLE, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK]
    ]
]

sounds = [
    pygame.mixer.Sound('1.mp3'),
    pygame.mixer.Sound('2.mp3'),
    pygame.mixer.Sound('3.mp3'),
    pygame.mixer.Sound('4.mp3'),
    pygame.mixer.Sound('5.mp3')
]

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, light_colors[row][col], [col * grid_width, row * grid_height, grid_width, grid_height])

def apply_pattern(pattern_index):
    pattern = patterns[pattern_index]
    
    for row in range(rows):
        for col in range(cols):
            light_colors[row][col] = pattern[row][col]
    
    draw_grid()
    pygame.display.update()

    sounds[pattern_index].play()

def play_random_sequence():
    sequence = list(range(5))
    random.shuffle(sequence)

    for index in sequence:
        apply_pattern(index)
        time.sleep(0.5)
    
    for row in range(rows):
        for col in range(cols):
            light_colors[row][col] = BLACK
    
    draw_grid()
    pygame.display.update()

running = True
current_pattern = None

while running:
    screen.fill(BLACK)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_pattern = 0
                apply_pattern(0)
            elif event.key == pygame.K_2:
                current_pattern = 1
                apply_pattern(1)
            elif event.key == pygame.K_3:
                current_pattern = 2
                apply_pattern(2)
            elif event.key == pygame.K_4:
                current_pattern = 3
                apply_pattern(3)
            elif event.key == pygame.K_5:
                current_pattern = 4
                apply_pattern(4)
            elif event.key == pygame.K_6:
                play_random_sequence()

        if event.type == pygame.KEYUP:
            if current_pattern is not None:
                for row in range(rows):
                    for col in range(cols):
                        light_colors[row][col] = BLACK
                
                draw_grid()
                pygame.display.update()

                sounds[current_pattern].stop()
                current_pattern = None

    pygame.display.flip()

pygame.quit()
