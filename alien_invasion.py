import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button


#为game_function模块指定别名（方便用）
import game_functions as gf

def run_game():



    #游戏初始化 屏幕对象创建
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button=Button(ai_settings,screen,"PLAY")

    #创建存储游戏统计信息的实例 创建记分板
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats,)

    #飞船对象创建
    ship=Ship(ai_settings,screen)

    #子弹编组创建
    bullets=Group()

    #外星人群组创建

    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #游戏主循环
    while True:


        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
