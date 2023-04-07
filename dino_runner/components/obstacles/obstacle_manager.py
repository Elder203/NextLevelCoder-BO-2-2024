import random 
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD
import pygame


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
            
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type_list = [Cactus(), Bird()]
            self.obstacles.append(random.choice(self.obstacle_type_list))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break  
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        