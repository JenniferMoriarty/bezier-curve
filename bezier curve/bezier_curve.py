
import pygame
from sys import exit
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800,800))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    p0 = (300,300)
    p1 = (600,500)
    p2 = (300,200)
    t = 0
    for i in np.arange(0,1,0.001):
            px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
            py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2  
            t = t + 0.01        
            pygame.draw.rect(screen,(255,0,0), (px,py,1,1))
            pygame.draw.circle(screen, (255, 255, 255), (300, 300), 10)
            pygame.draw.circle(screen, (255, 0, 255), (600,500), 10)
            pygame.draw.circle(screen, (0, 255, 255), (300, 200), 10)
    pygame.display.update()
