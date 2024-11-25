import pygame
import random


pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = 15

# Food settings
food_pos = [random.randrange(1, (screen_width // 10)) * 10,
            random.randrange(1, (screen_height // 10)) * 10]
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
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width // 10)) * 10,
                    random.randrange(1, (screen_height // 10)) * 10]
    food_spawn = True

    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > screen_width - 10 or snake_pos[1] < 0 or snake_pos[1] > screen_height - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    pygame.display.update()

    clock.tick(speed)
