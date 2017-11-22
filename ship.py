import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """飞船初始化及初始位置设置"""
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #加载飞船图像 获取外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #新飞船location：屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #在属性center中存入小数值
        self.center=float(self.rect.centerx)

        #获取移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志移动飞船位置"""
        #更新飞船center值（而不是只能为int的rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor

        #根据self.center 更新 rect对象(只存储整数部分）
        self.rect.centerx=self.center

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """飞船屏幕居中"""
        self.center=self.screen_rect.centerx






