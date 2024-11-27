import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_SPEED,
)
from food_functions import get_random_food_position
from snake_functions import (
    initiate_snake_tiles,
    is_snake_biting_itself,
    is_snake_offscreen,
    enlarge_snake_in_direction,
)
from utilities import (
    game_over,
    update_display,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = initiate_snake_tiles()
    direction = 'RIGHT'

    food_pos = get_random_food_position()

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

        enlarge_snake_in_direction(snake, direction)

        if snake[0] == food_pos:
            food_pos = get_random_food_position()
        else:
            snake.pop()

        if is_snake_biting_itself(snake) or is_snake_offscreen(snake):
            game_over()

        update_display(screen, snake, food_pos)

        clock.tick(SNAKE_SPEED)


if __name__ == '__main__':
    main()
