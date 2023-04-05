from pygame.sprite import Sprite
from dino_runner.utils.constants import(
    JUMPING,
    RUNNING,
    DUCKING,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    DEFAULT_TYPE,
    SHIELD_TYPE)
import pygame

class Dinosaur(Sprite):

    POS_x = 80
    POS_Y = 310
    DUCK_POS_Y = 350
    JUMP_VEL = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.image = self.run_img[DEFAULT_TYPE][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jump_vel = self.JUMP_VEL
        self.setup_state_variables()

    def setup_state_variables(self):
        self.has_powerup = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_Y
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.DUCK_POS_Y
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.jumping:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -=  0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jump_vel = self.JUMP_VEL

    def update(self, user_input):
        if self.jumping:
            self.jump()
        elif self.ducking:
            self.duck()
        elif self.running:
            self.run()

        if user_input[pygame.K_DOWN] and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] and not self.jumping:
            self.running = False
            self.ducking = False
            self.jumping = True
        elif not self.jumping:
            self.running = True
            self.ducking = False
            self.jumping = False

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.show_text:
                    #codigo mostrar tiempo q falta time_to_show
                    pass
            else:
                self.shield = False
                self.update_to_default(SHIELD_TYPE)

    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE
