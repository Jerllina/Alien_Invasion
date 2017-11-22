import pygame.font
from pygame.sprite import Group
from ship import Ship

"""计分板"""
class Scoreboard():

    def __init__(self,ai_settings,screen,stats):
        #初始化记分显示的属性
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        #记分显示的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        #设置初始得分图像,最高分图像(文本转图像），当前等级图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    #实时得分
    def prep_score(self):
        #得分文本转换为图像
        rounded_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #得分放在右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    #最高分
    def prep_high_score(self):
        #得分文本转图像
        high_score=int(round(self.stats.high_score,-1))
        high_score_str='{:,}'.format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #位置：屏幕顶部中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

    #等级
    def prep_level(self):
        #等级文本转图像
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        #位置：当前得分的下方
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    #飞船剩余数
    def prep_ships(self):
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    #显示等级,得分,飞船剩余数
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

