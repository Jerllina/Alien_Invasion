class Settings():
    """存储本游戏所有设置的类"""
    def __init__(self):

        """初始化游戏静态设置"""
        # 屏幕设置
        # 尺寸
        self.screen_width=800
        self.screen_height=600
        # 浅灰色(230)
        self.bg_color=(230,230,230)

        #飞船设置 （数量）
        self.ship_limit=0

        #子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        #限制最大子弹数
        self.bullets_allowed=10

        #外星人设置
        self.fleet_drop_speed=10


        """初始化动态设置"""
        #加快游戏速度
        self.speedup_scale=1.1
        #加快记分速度
        self.score_scale=1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        # 初始化随游戏变化的速度
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1

        #fleet_direction为1表示右移  -1表示左移
        self.fleet_direction=1

        #记分
        self.alien_points=50

    #升级时的游戏体验提升(提速,提分）
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)