import pygame
import constants

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Space Chase")

# Movement flags
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Load images
background = pygame.image.load("images/background_1.png")
zicro = pygame.image.load("images/zicro_1.png")
zicro = pygame.transform.scale(zicro, (150, 150))

# Player and background setup
player = pygame.Rect((100, 100, 50, 50))
background_pos = [-350, -250]
clock = pygame.time.Clock()

# Game loop
run = True
while run:
    clock.tick(constants.FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: moving_left = True
            if event.key == pygame.K_RIGHT: moving_right = True
            if event.key == pygame.K_UP: moving_up = True
            if event.key == pygame.K_DOWN: moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: moving_left = False
            if event.key == pygame.K_RIGHT: moving_right = False
            if event.key == pygame.K_UP: moving_up = False
            if event.key == pygame.K_DOWN: moving_down = False

    # Movement logic
    dx = dy = 0
    if moving_left: dx -= constants.SPEED
    if moving_right: dx += constants.SPEED
    if moving_up: dy -= constants.SPEED
    if moving_down: dy += constants.SPEED
    player = player.move(dx, dy)

    # Drawing
    screen.fill(constants.PINK)
    screen.blit(background, background_pos)
    screen.blit(zicro, (player.x, player.y))
    pygame.display.update()

pygame.quit()
