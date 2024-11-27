from random import randrange

import pygame

from constants import (
    BLACK,
    GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_SPEED,
    TILE_SIZE,
    WHITE,
)
from snake_functions import initiate_snake_tiles
from utilities import game_over


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Snake settings
    snake = initiate_snake_tiles()
    direction = 'RIGHT'

    # Food settings
    food_pos = [
        randrange(1, (SCREEN_WIDTH // TILE_SIZE)) * TILE_SIZE,
        randrange(1, (SCREEN_HEIGHT // TILE_SIZE)) * TILE_SIZE
    ]
    food_spawn = True

    # Main Function
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over()
                if event.key in (pygame.K_UP, pygame.K_w):
                    if not direction == 'DOWN':
                        direction = 'UP'
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    if not direction == 'UP':
                        direction = 'DOWN'
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if not direction == 'RIGHT':
                        direction = 'LEFT'
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if not direction == 'LEFT':
                        direction = 'RIGHT'

        next_snake_position = (snake[0]).copy()

        if direction == 'UP':
            next_snake_position[1] -= TILE_SIZE
        if direction == 'DOWN':
            next_snake_position[1] += TILE_SIZE
        if direction == 'LEFT':
            next_snake_position[0] -= TILE_SIZE
        if direction == 'RIGHT':
            next_snake_position[0] += TILE_SIZE

        snake.insert(0, next_snake_position)
        if snake[0] == food_pos:
            food_spawn = False
        else:
            snake.pop()

        if not food_spawn:
            food_pos = [
                randrange(1, (SCREEN_WIDTH // TILE_SIZE)) * TILE_SIZE,
                randrange(1, (SCREEN_HEIGHT // TILE_SIZE)) * TILE_SIZE
            ]
        food_spawn = True

        screen.fill(BLACK)

        for pos in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], TILE_SIZE, TILE_SIZE))

        pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], TILE_SIZE, TILE_SIZE))

        if snake[0][0] < 0 or snake[0][0] > SCREEN_WIDTH - TILE_SIZE or snake[0][1] < 0 or snake[0][1] > SCREEN_HEIGHT - TILE_SIZE:
            game_over()

        for block in snake[1:]:
            if snake[0] == block:
                game_over()

        pygame.display.update()

        clock.tick(SNAKE_SPEED)


if __name__ == '__main__':
    main()
