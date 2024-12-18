from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_START_SIZE,
    SNAKE_START_X,
    SNAKE_START_Y,
    TILE_SIZE,
)


def initiate_snake_tiles():
    snake_tiles = [[SNAKE_START_X, SNAKE_START_Y]]

    for _ in range(1, SNAKE_START_SIZE):
        next_tile = (snake_tiles[-1]).copy()
        next_tile[0] = next_tile[0] - TILE_SIZE
        snake_tiles.append(next_tile)

    return snake_tiles


def enlarge_snake_in_direction(snake_tiles, direction):
    snake_head = snake_tiles[0]
    next_snake_position = snake_head.copy()

    if direction == 'UP':
        next_snake_position[1] -= TILE_SIZE
    if direction == 'DOWN':
        next_snake_position[1] += TILE_SIZE
    if direction == 'LEFT':
        next_snake_position[0] -= TILE_SIZE
    if direction == 'RIGHT':
        next_snake_position[0] += TILE_SIZE

    snake_tiles.insert(0, next_snake_position)


def is_snake_biting_itself(snake_tiles):
    result = snake_tiles[0] in snake_tiles[1:]
    return result


def is_snake_offscreen(snake_tiles):
    head_x, head_y = snake_tiles[0]
    checks = [
        head_x < 0,
        head_x + TILE_SIZE > SCREEN_WIDTH,
        head_y < 0,
        head_y + TILE_SIZE > SCREEN_HEIGHT,
    ]
    result = any(checks)
    return result
