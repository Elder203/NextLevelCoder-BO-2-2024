from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        self.fly = 0 #indicador de vuelo
        super().__init__(BIRD, self.type)
        self.rect.y = random.randint(100, 310)


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed 
        self.obs_to_draw = BIRD[0] if self.fly < 10 else BIRD[1] 
        self.fly += 1
        if self.fly >= 20:
            self.fly = 0
        
        if self.rect.x < -self.rect.width:
            obstacles.pop() 