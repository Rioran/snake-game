from random import randrange

import pygame

from constants import (
    BLACK,
    GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_SPEED,
    SNAKE_START_X,
    SNAKE_START_Y,
    TILE_SIZE,
    WHITE,
)


pygame.init()

# Screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Snake settings
snake_pos = [SNAKE_START_X, SNAKE_START_Y]
snake_body = [
    [SNAKE_START_X, SNAKE_START_Y],
    [SNAKE_START_X - TILE_SIZE, SNAKE_START_Y],
    [SNAKE_START_X - 2 * TILE_SIZE, SNAKE_START_Y]
]
direction = 'RIGHT'
change_to = direction

# Food settings
food_pos = [randrange(1, (SCREEN_WIDTH // TILE_SIZE)) * TILE_SIZE,
            randrange(1, (SCREEN_HEIGHT // TILE_SIZE)) * TILE_SIZE]
food_spawn = True

# Set up clock
clock = pygame.time.Clock()


# Game Over
def game_over():
    pygame.quit()
    quit()


# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not direction == 'DOWN':
                    direction = 'UP'
            elif event.key == pygame.K_DOWN:
                if not direction == 'UP':
                    direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if not direction == 'RIGHT':
                    direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if not direction == 'LEFT':
                    direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= TILE_SIZE
    if direction == 'DOWN':
        snake_pos[1] += TILE_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= TILE_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += TILE_SIZE

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [randrange(1, (SCREEN_WIDTH // TILE_SIZE)) * TILE_SIZE,
                    randrange(1, (SCREEN_HEIGHT // TILE_SIZE)) * TILE_SIZE]
    food_spawn = True

    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], TILE_SIZE, TILE_SIZE))

    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - TILE_SIZE or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - TILE_SIZE:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    pygame.display.update()

    clock.tick(SNAKE_SPEED)
