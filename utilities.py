import pygame

from constants import (
    BLACK,
    GREEN,
    TILE_SIZE,
    WHITE,
)


def game_over():
    pygame.quit()
    quit()


def update_display(screen, snake, food_position):
    screen.fill(BLACK)

    for position in snake:
        rectangle = pygame.Rect(position[0], position[1], TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, GREEN, rectangle)

    rectangle = pygame.Rect(food_position[0], food_position[1], TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, WHITE, rectangle)

    pygame.display.update()


def check_events_for_new_direction_or_quit(direction):
    new_direction = direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over()
            if event.key in (pygame.K_UP, pygame.K_w):
                if not direction == 'DOWN':
                    new_direction = 'UP'
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                if not direction == 'UP':
                    new_direction = 'DOWN'
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                if not direction == 'RIGHT':
                    new_direction = 'LEFT'
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                if not direction == 'LEFT':
                    new_direction = 'RIGHT'

    return new_direction
