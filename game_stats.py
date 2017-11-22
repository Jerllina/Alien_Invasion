import json

#跟踪统计游戏信息
class GameStats():
    #初始化
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        #游戏刚启动时 处于非活动状态
        self.game_active=False
        #初始化最高得分，任何情况均不重置
        filename='highestscore.json'
        try:
            with open(filename,'r') as f_obj:
                self.high_score=json.load(f_obj)

        except FileNotFoundError:
            self.high_score=0



    #重置统计信息 (玩家开始新游戏时也可使用）
    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        #记分 初始记分为0
        self.score=0
        #等级 初始等级为1
        self.level=1





