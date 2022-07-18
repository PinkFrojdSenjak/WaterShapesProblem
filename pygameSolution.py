import pygame
import math

class Ball:
    def __init__(self, dis, angle, v0) -> None:
        self.dis = dis
        self.x = dis.get_width() // 2
        self.y = dis.get_height() // 2
        self.x_speed = v0 * math.cos(angle) 
        self.y_speed = v0 * math.sin(angle)
        self.radius = 3
        self.color = (255, 255, 255)

    def draw(self, dis) -> None:
        pygame.draw.circle(dis, self.color, (self.x, self.y), self.radius)
    
    def update(self) -> None:
        self.x += self.x_speed
        self.y += self.y_speed
        self.y_speed -= g
        if self.x > dis.get_width() or self.x < 0:
            self.x_speed = -self.x_speed
        if self.y > dis.get_height() or self.y < 0:
            self.y_speed = -self.y_speed


def drawGrid(display, w, h):
    blockSize = 20 #Set the size of the grid block
    for x in range(w):
        for y in range(h):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(display, WHITE, rect, 1)

    xaxis = pygame.Rect(0, screen_h//2, w*blockSize, 1)
    pygame.draw.rect(display, BLACK, xaxis, 2)
    yaxis = pygame.Rect(screen_w//2, 0, 1, h*blockSize)
    pygame.draw.rect(display, BLACK, yaxis, 2)


pygame.init()
screen_w = 1000
screen_h = 800
dis=pygame.display.set_mode((screen_w,screen_h))

pygame.display.set_caption('Mali peder')
game_over=False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


angle = 0
g = 0.1
BACKGROUND_COLOR = (201, 201, 201)

font = pygame.font.Font('freesansbold.ttf', 20)

balls = []
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
 
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        angle = angle - 1
    if keys_pressed[pygame.K_LEFT]:
        angle = angle + 1
    
    new_ball = Ball(dis, angle, 1)
    balls.append(new_ball)
    text = font.render(f"Angle: {angle}", True, BLACK, BACKGROUND_COLOR)

  
    dis.fill(BACKGROUND_COLOR)

    for ball in balls:
        ball.draw(dis)
        ball.update()
    drawGrid(dis, screen_w, screen_h)
    dis.blit(text, (screen_w - 100, 50))
    

    pygame.display.update()
