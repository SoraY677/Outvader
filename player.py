import pyxel
from shotBallet import ShotBallet


class Player:

    def __init__(self, panelw, panelh):
        '''
        プレイヤーの初期化
        @param x&y 初期座標
        '''
        self.size = 16
        self.x = (panelw - self.size) / 2
        self.y = panelh - self.size - 5
        self.shotBallet = ShotBallet(-5, 5, 20)

    def update(self, panelw, panelh):
        '''
        移動を制御する
        '''
        # キーボード操作による移動
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 3
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 3
        if pyxel.btn(pyxel.KEY_SPACE):
            self.shotBallet.init(self.x + self.size/2, self.y)

        # 壁で止まる
        if self.x < 0:
            self.x = 0
        elif self.x > panelw-self.size:
            self.x = panelw-self.size

        self.shotBallet.update(panelh)

    def draw(self):
        '''
        プレイヤーの描画を行う
        '''
        pyxel.blt(self.x, self.y, 1, 16*3, 0, 16, 16, 0)
        self.shotBallet.draw()
