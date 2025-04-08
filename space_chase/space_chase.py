import pygame
import constants
pygame.init

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Gem Rush")

clock = pygame.time.Clock()
player = pygame.Rect((100, 100, 50, 50))

#game loop
run = True
while run:
	clock.tick(constants.FPS)
	screen.fill(constants.PINK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.draw.rect(screen, (constants.RED), player)
	pygame.display.update()
pygame.quit()