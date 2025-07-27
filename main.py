# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_sprites = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid_sprites, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for group_member in drawable:
            group_member.draw(screen)
        
        updateable.update(dt)

        for asteroid in asteroid_sprites:
            if asteroid.check_collision(player):
                print("Game Over!")
                return
            for bullet in shots:
                if asteroid.check_collision(bullet):
                    new_asteroids = ()
                    new_asteroids = asteroid.split()
                    if new_asteroids != None:
                        asteroid_sprites.add(new_asteroids[0], new_asteroids[1])

                    bullet.kill()
            
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()