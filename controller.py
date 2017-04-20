import pygame
import view
import model

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()

data = model.get_data
bc = view.BarChart(screen.get_rect(), values=data)

# display loop
done = False
while not done:
	screen.fill(view.BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	bc.draw(screen)
	pygame.display.update()

pygame.quit()
quit()
