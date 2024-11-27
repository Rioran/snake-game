from random import randrange

from constants import (
    SCREEN_HORIZONTAL_TILES,
    SCREEN_VERTICAL_TILES,
    TILE_SIZE,
)


def get_random_food_position():
    x_tile = randrange(1, SCREEN_HORIZONTAL_TILES)
    x_pos = x_tile * TILE_SIZE

    y_tile = randrange(1, SCREEN_VERTICAL_TILES)
    y_pos = y_tile * TILE_SIZE

    result = [x_pos, y_pos]

    return result
