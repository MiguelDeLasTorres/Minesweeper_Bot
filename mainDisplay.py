import sys
import pygame
import CVTest
import numpy as np
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
gridW = 9
gridH = 9
WINDOW_HEIGHT = 180
WINDOW_WIDTH = 180
startX, startY, endX, endY = 271, 398, 450, 577
templates_img=['Images/0.png', 'Images/1.PNG', 'Images/2.PNG','Images/3.PNG','Images/4.PNG', 'Images/5.PNG','Images/6.PNG','Images/7.PNG','Images/8.PNG', 'Images/Flag.PNG', 'Images/cell.PNG']
colours=[(128,128,128), (0,0,255), (0,255,0), (255,0,0), (200,0,200), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (255,255,255)]
img_load = [pygame.image.load(img) for img in templates_img]

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    #SCREEN.fill(WHITE)

    while True:

        img = CVTest.LoadImage(startX, startY, endX, endY)
        img_np = np.array(img)
        img_gray = CVTest.getImageGray(img_np)
        templates = CVTest.setupTemplates(templates_img)
        locs = CVTest.matching_templates(templates, img_gray, 0.88)

        grid = CVTest.locsToGrid(locs, endX - startX, endY - startY, gridW, gridH)
        drawGrid(grid, gridW, gridH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid(grid, gridW, gridH):
    blockSize = 20 #Set the size of the grid block
    for x in range(gridW):
        for y in range(gridH):
            i = grid[x + y * gridW]
            SCREEN.blit(img_load[i], (x*blockSize, y * blockSize))
            # rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            # i = grid[x+y*9]
            # pygame.draw.rect(SCREEN, colours[i], rect)
main()