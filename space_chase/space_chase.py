import pygame
import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Space Chase")

#create clock for maintaining frame rate
clock = pygame.time.Clock()

#define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

player = pygame.Rect((200, 200, 50, 50))

#game loop
run = True
while run:

	clock.tick(constants.FPS)
	screen.fill(constants.ORANGE)

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
#take keyboard presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = True
			if event.key == pygame.K_d:
				moving_right = True
			if event.key == pygame.K_w:
				moving_up = True
			if event.key == pygame.K_s:
				moving_down = True
		#keyboard buttone released
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				moving_left = False
			if event.key == pygame.K_d:
				moving_right = False
			if event.key == pygame.K_w:
				moving_up = False
			if event.key == pygame.K_s:
				moving_down = False
		#calculate player movement
	dx = 0
	dy = 0
	if moving_right:
		dx = constants.SPEED
	if moving_left:
		dx = -constants.SPEED
	if moving_up:
		dy = -constants.SPEED
	if moving_down:
		dy = constants.SPEED

	
	#move player
	player = player.move(dx, dy)
	pygame.draw.rect(screen, (constants.PINK), player)
	pygame.display.update()
pygame.quit()
