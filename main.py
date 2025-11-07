import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    #player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_list = pygame.sprite.Group()
    shots_list = pygame.sprite.Group()
    Shot.containers = (shots_list, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_list, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.timer <= 0:
                        player.shoot(dt)
            elif event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        player.timer -= dt
        if len(asteroids_list) >= 1:
            for ast in asteroids_list:
                for shot in shots_list:
                    if shot.check_collision(ast):
                        ast.split()
                        shot.kill()
                if player.check_collision(ast):
                    print("Game over!")
                    sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = (game_clock.tick(60)/1000)
        
if __name__ == "__main__":
    main()
