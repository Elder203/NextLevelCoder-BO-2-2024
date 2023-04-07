
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
import random

class Cactus(Obstacle):
    def __init__(self):
        self.cac_types = [LARGE_CACTUS, SMALL_CACTUS] #constantes
        self.cactus_size = random.choice(self.cac_types)
        self.type = random.randint(0, 2)
        super().__init__(self.cactus_size, self.type)
        
        if self.cactus_size == SMALL_CACTUS: #posicion de los cactus
            self.rect.y = 310
        else: 
            
            self.rect.y = 325
 