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
