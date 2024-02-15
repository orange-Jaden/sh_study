import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jaden IoT")

# mqtt client, callback 생성 
def turnOn():
    # To-Do
    print("Turn on")

def turnOff():
    # To-Do
    print("Turn off")

# load images
class Button: 
    def __init__(self, x, y, image, callback):
        pygame.sprite.Sprite.__init__(self)
        self.clicked = False
        self.image = image
        self.callback = callback
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self) -> bool:
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not(self.clicked):
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                self.callback()
        elif not(self.rect.collidepoint(pos)) and self.clicked:
            self.clicked = False
        
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

# create restart button instance
## load image
on_button_img = pygame.image.load('img/btn_on.png')
off_button_img = pygame.image.load('img/btn_off.png')

## create button
button_1 = Button(screen_width // 2, screen_height // 2 - 100, on_button_img, turnOn)
button_2 = Button(screen_width // 2, screen_height // 2 + 100, on_button_img, turnOff)

run  = True
while run:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw button
    button_1.draw()
    button_2.draw()

    pygame.display.update()

pygame.quit()
