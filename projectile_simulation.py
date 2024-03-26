"""
Todo:
- keep it in the bounds of the screen
    - differentiate the function (twice) to find maximum and minima
- add suvat formulae
- add input stage (need horizontal movement)
- add trail
    - dotted line
- Positive is upwards
- starting angle
"""

import pygame

# pygame setup:
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen_colour = "white"
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
running = True
FPS = 60

# projectile details:
PROJECTILE_COLOUR = "black"
PROJECTILE_RADIUS = 8
PROJECTILE_STARTING_X = 0
PROJECTILE_STARTING_Y = 0 # changeable


try: 
    displacement = input("displacement = ")
except ValueError:
    has_displacement = False
try: 
    initial_velocity = input("initial_velocity = ")
except ValueError:
    has_initial_velocity = False
try: 
    final_velocity = input("final_velocity = ")
except ValueError:
    has_final_velocity = False
try: 
    acceleration = input("acceleration = ")
except ValueError:
    has_acceleration = False
try: 
    time = input("time = ")
except ValueError:
    has_time = False






# running
while running:
    # pygame.QUIT event means the user clicked X to close your window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # render the projectile
    pygame.draw.circle(SCREEN, PROJECTILE_COLOUR, )

    pygame.display.flip() # flip() the display to put the work on screen

    CLOCK.tick(FPS)# limits FPS to 60


pygame.quit()