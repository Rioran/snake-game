import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_SPEED,
    SNAKE_START_DIRECTION,
)
from food_functions import get_random_food_position
from snake_functions import (
    initiate_snake_tiles,
    is_snake_biting_itself,
    is_snake_offscreen,
    enlarge_snake_in_direction,
)
from utilities import (
    check_events_for_new_direction_or_quit,
    game_over,
    update_display,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = initiate_snake_tiles()
    direction = SNAKE_START_DIRECTION
    food_pos = get_random_food_position()

    while True:
        direction = check_events_for_new_direction_or_quit(direction)

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
