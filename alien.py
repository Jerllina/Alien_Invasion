import pygame
from pygame.sprite import Sprite

#导入单个外星人
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        #外星人初始化 初始位置设置
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #外星人图像载入
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #坐标设置（左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #存储准确位置(转浮点
        self.x=float(self.rect.x)

    #绘制外星人
    def blitme(self):
        self.screen.blit(self.image,self.rect)



    #检查边缘碰撞
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    # 左/右移动外星人
    def update(self):
        self.x +=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x

