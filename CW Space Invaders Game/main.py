
import pygame
import os

pygame.mixer.init() # - SOUNDS
pygame.font.init() 

pygame.init()
screen = pygame.display.set_mode((900,500))

WIDTH  = 900
HEIGHT = 500

BULLET_FIRE = pygame.mixer.Sound("Assets\Gun+Silencer.mp3")
BULLET_HIT = pygame.mixer.Sound("Assets\Grenade+1.mp3")

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("arial", 80)

RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

VEL = 5
BULLET_VEL = 6
MAX_BULLET = 3

SHIP_W = 55
SHIP_H = 40

FPS = 60

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

yellowShip = pygame.image.load("Assets/spaceship_yellow.png")
yellowShip = pygame.transform.scale(yellowShip,(SHIP_W, SHIP_H))
yellowShip = pygame.transform.rotate(yellowShip, 90)

redShip = pygame.image.load("Assets/spaceship_red.png")
redShip = pygame.transform.scale(redShip,(SHIP_W, SHIP_H))
redShip = pygame.transform.rotate(redShip, 270)

bg = pygame.image.load("Assets/space.png")

def drawWindow(red, yellow, redB, yellowB, redH, yellowH):
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, BLACK, BORDER)
    screen.blit(yellowShip, (yellow.x, yellow.y))
    screen.blit(redShip, (red.x, red.y))
    redHealthText = HEALTH_FONT.render(f"health: {redH}", 1, WHITE) # - APPLYING the font NOT DISPLAYING
    yellowHealthText = HEALTH_FONT.render(f"health: {yellowH}", 1, WHITE)

    screen.blit(redHealthText, (WIDTH - redHealthText.get_width() - 10, 10))
    screen.blit(yellowHealthText, (10, 10))

    for bullet in redB:
        pygame.draw.rect(screen, RED, bullet)
    for bullet in yellowB:
        pygame.draw.rect(screen, YELLOW, bullet)

    pygame.display.update()

def yellowMovement(keysPressed, yellow):
    if keysPressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keysPressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keysPressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keysPressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20:
        yellow.y += VEL


def main():
    red = pygame.Rect(700,300, SHIP_W, SHIP_H)
    yellow = pygame.Rect(100,300, SHIP_W, SHIP_H)
    
    redB = []
    yellowB = []

    redH = 10
    yellowH = 10

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        drawWindow(red, yellow, redB, yellowB, redH, yellowH)


main()
    
    
