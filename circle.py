#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:20:49 2021

@author: enzelin
"""
import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
PINK = (255,182,193)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("😍Happy Time")

done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.circle(screen, PINK, [20, 20], 1)
    
    pygame.draw.line(screen, BLACK, [0, 250], [700, 250], 3)
    
    pygame.draw.line(screen, BLACK, [350, 0], [350, 500], 3)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

