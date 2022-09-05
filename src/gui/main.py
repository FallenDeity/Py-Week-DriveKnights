import pygame

resolution = pygame.display.Info()
s_width, s_height = resolution.current_w, resolution.current_h

pygame.display.init()
pygame.display.set_caption("The Red Planet")
screen = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

bg = pygame.image.load(os.path.join('assets','bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

while running:
    redrawWindow()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.flip()

def redrawWindow():
    win.blit(bg, (bgX, 0))  # draws our first bg image
    win.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pygame.display.update()