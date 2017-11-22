import pygame
from pygame.sprite import Sprite

#飞船发射子弹管理
class Bullet(Sprite):
    #子弹创建
    def __init__(self,ai_settings,screen,ship):
        #创建子弹对象（飞船位置
        super(Bullet,self).__init__()
        self.screen=screen

        #先在（0，0）处创建子弹形状，再设置到正确位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #存储子弹位置（小数表示）
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    #子弹向上移动
    def update(self):
        #更新子弹位置
        self.y-=self.speed_factor
        self.rect.y=self.y

    #子弹绘制
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

