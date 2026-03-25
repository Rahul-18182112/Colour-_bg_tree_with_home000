import pygame
import math
import random
import time
import sys

# 1. Setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
clock = pygame.time.Clock()

# समय का हिसाब रखने के लिए
start_time = time.time() 

def draw_strong_tree(x, y, angle, depth, length, thickness, leaf_color):
    if depth == 0:
        pygame.draw.circle(screen, leaf_color, (int(x), int(y)), 12)
        return
    x2 = x + math.cos(math.radians(angle)) * length
    y2 = y - math.sin(math.radians(angle)) * length
    
    # मजबूत तना
    trunk_color = (60, 30, 10) if depth > 4 else (90, 60, 40)
    pygame.draw.line(screen, trunk_color, (x, y), (x2, y2), int(thickness))

    sway = math.sin(time.time() * 10) * 2
    draw_strong_tree(x2, y2, angle - 25 + sway, depth - 1, length * 0.78, thickness * 0.75, leaf_color)
    draw_strong_tree(x2, y2, angle + 25 + sway, depth - 1, length * 0.78, thickness * 0.75, leaf_color)

def draw_simple_house(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 100, 80))
    pygame.draw.polygon(screen, (180, 50, 50), [(x-10, y), (x+50, y-50), (x+110, y)])
    pygame.draw.rect(screen, (40, 20, 10), (x+35, y+40, 30, 40))

def draw_small_boy(x, y, color):
    pygame.draw.circle(screen, (255, 220, 180), (x, y), 8)
    pygame.draw.line(screen, color, (x, y+8), (x, y+30), 4)
    pygame.draw.line(screen, color, (x, y+12), (x-12, y+25), 2)
    pygame.draw.line(screen, color, (x, y+12), (x+12, y+25), 2)
    pygame.draw.line(screen, (20, 20, 80), (x, y+30), (x-8, y+45), 3)
    pygame.draw.line(screen, (20, 20, 80), (x, y+30), (x+8, y+45), 3)

# 2. Main Loop
running = True
last_color_update = time.time()
dynamic_color = (255, 255, 255)
bg_color = (20, 20, 40)

while running:
    current_time = time.time()
    elapsed_time = current_time - start_time # कितना समय बीत गया

    # --- 10 सेकंड बाद बंद होने का लॉजिक ---
    if elapsed_time > 10:
        running = False

    # --- 0.1 सेकंड में रंग बदलने का लॉजिक ---
    if current_time - last_color_update > 0.1:
        bg_color = (random.randint(30, 80), random.randint(30, 80), random.randint(80, 150))
        dynamic_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        last_color_update = current_time

    screen.fill(bg_color)

    # जमीन
    pygame.draw.rect(screen, (34, 100, 34), (0, HEIGHT-120, WIDTH, 120))

    # चीजें ड्रा करें
    draw_strong_tree(WIDTH // 2 - 100, HEIGHT - 120, 90, 8, HEIGHT // 7, 22, dynamic_color)
    draw_simple_house(WIDTH // 2 + 50, HEIGHT - 200, dynamic_color)
    draw_small_boy(WIDTH // 2 + 100, HEIGHT - 165, (255, 255, 255))

    # समय दिखाने के लिए (Optional)
    font = pygame.font.SysFont("Arial", 30)
    timer_text = font.render(f"Time Left: {int(10 - elapsed_time)}s", True, (255, 255, 255))
    screen.blit(timer_text, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
