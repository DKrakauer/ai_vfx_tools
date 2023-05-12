import pygame
import sys

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SAND_COLOR = (255, 204, 102)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Simulation")
clock = pygame.time.Clock()

sand_particles = []

def update_sand():
    for particle in sand_particles:
        # Gravity
        particle[1] += 1

        # Boundary check
        if particle[1] >= HEIGHT:
            particle[1] = HEIGHT - 1

        # Particle collisions
        for other_particle in sand_particles:
            if other_particle != particle:
                dx, dy = other_particle[0] - particle[0], other_particle[1] - particle[1]
                dist = (dx * dx + dy * dy) ** 0.5

                if dist < 2:
                    particle[1] -= 1

def draw_sand():
    for particle in sand_particles:
        pygame.draw.circle(screen, SAND_COLOR, (particle[0], particle[1]), 1)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # Add sand particles when the left mouse button is pressed
    if mouse_pressed[0]:
        sand_particles.append(list(mouse_pos))

    update_sand()
    draw_sand()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
