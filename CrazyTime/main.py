import pyglet
import random
from pyglet.window import key
import time

class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__()

        # Variabili Locali
        self.stato = 0
        self.pulsante = 0
        self.money = 1000
        self.on1 = 0
        self.on2 = 0
        self.on5 = 0
        self.on10 = 0
        self.oncoin = 0
        self.onpac = 0
        self.oncash = 0
        self.oncrazy = 0
        self.decelerazione = 20
        self.velocita_rotazione = 0
        self.spinning = False
        self.err = False
        self.finita_rotazione = False
        self.win = 0

        # Velocita' rotazione per vincita
        self.ones = [540, 560, 535, 545]
        self.twos = [500, 530, 515, 525]
        self.fives = [590, 575]
        self.tens = [510, 505, 502]
        self.crazys = [550]
        self.coins = [503, 514]
        self.pacs = [535.2]
        self.cashs = [539.8]

        # Creazione Finestra
        self.set_size(1280, 720)
        self.icon = pyglet.image.load("gfx/icon.png")
        self.set_icon(self.icon)
        self.set_caption("Crazy Time - Lavoro Informatica")

        # Main Bg
        self.mainbg = pyglet.resource.image("gfx/bgmain.png")
        self.mainbg.anchor_x = self.mainbg.width // 2
        self.mainbg.anchor_y = self.mainbg.height // 2
        self.mainbg_sprite = pyglet.sprite.Sprite(img=self.mainbg, x=self.width//2, y=self.height//2)
        self.mainbg_sprite.scale = 0.7


        # Creazione Background
        self.puntino = pyglet.shapes.Rectangle(x=self.width // 2, y=600, width=20, height=100, color=(255, 0, 0))
        self.puntino.anchor_x = self.puntino.width//2
        self.puntino.anchor_y = self.puntino.height // 2

        self.background = pyglet.resource.image("gfx/background.jpg")
        self.background.anchor_x = self.background.width // 2
        self.background.anchor_y = self.background.height // 2
        self.background_sprite = pyglet.sprite.Sprite(img=self.background, x=self.width // 2, y=self.height // 2)
        self.background_sprite.scale = 2.26

        # Creazione Batch
        self.batch_bet = pyglet.graphics.Batch()
        self.batch_text = pyglet.graphics.Batch()

        # Caricamento font
        self.font = pyglet.resource.add_font("font/CasinoFlat.ttf")

        # Creazione Testo
        self.moneylabel = pyglet.text.Label(f"{self.money}€",
                                            font_name=self.font,
                                            font_size=36,
                                            x=140,
                                            y=655,
                                            z=0.8,
                                            anchor_y="center",
                                            anchor_x="center",
                                            color=(0, 0, 0, 255))

        self.betlabel1 = pyglet.text.Label(f"Bet on 1: {self.on1}",
                                            font_name=self.font,
                                            font_size=12,
                                            x=280,
                                            y=700,
                                            anchor_y="center",
                                            color=(255, 255, 255, 255),
                                            batch=self.batch_text)
        self.betlabel2 = pyglet.text.Label(f"Bet on 2: {self.on2}",
                                            font_name=self.font,
                                            font_size=12,
                                            x=280,
                                            y=669,
                                            anchor_y="center",
                                            color=(255, 255, 255, 255),
                                            batch=self.batch_text)
        self.betlabel5 = pyglet.text.Label(f"Bet on 5: {self.on5}",
                                            font_name=self.font,
                                            font_size=12,
                                            x=280,
                                            y=637,
                                            anchor_y="center",
                                            color=(255, 255, 255, 255),
                                            batch=self.batch_text)
        self.betlabel10 = pyglet.text.Label(f"Bet on 10: {self.on10}",
                                            font_name=self.font,
                                            font_size=12,
                                            x=280,
                                            y=605,
                                            anchor_y="center",
                                            color=(255, 255, 255, 255),
                                            batch=self.batch_text)
        self.betlabelcoin = pyglet.text.Label(f"Bet on Coin Flip: {self.oncoin}",
                                            font_name=self.font,
                                            font_size=12,
                                            x=480,
                                            y=700,
                                            anchor_y="center",
                                            color=(255, 255, 255, 255),
                                            batch=self.batch_text)
        self.betlabelpac = pyglet.text.Label(f"Bet on Pachinko: {self.onpac}",
                                              font_name=self.font,
                                              font_size=12,
                                              x=480,
                                              y=669,
                                              anchor_y="center",
                                              color=(255, 255, 255, 255),
                                              batch=self.batch_text)
        self.betlabelcash = pyglet.text.Label(f"Bet on Cash Hunt: {self.oncash}",
                                              font_name=self.font,
                                              font_size=12,
                                              x=480,
                                              y=637,
                                              anchor_y="center",
                                              color=(255, 255, 255, 255),
                                              batch=self.batch_text)
        self.betlabelcrazy = pyglet.text.Label(f"Bet on Crazy Time: {self.oncrazy}",
                                              font_name=self.font,
                                              font_size=12,
                                              x=480,
                                              y=605,
                                              anchor_y="center",
                                              color=(255, 255, 255, 255),
                                              batch=self.batch_text)


        self.nobet = pyglet.text.Label(f"Devi prima puntare",
                                       font_name=self.font,
                                       font_size=38,
                                       x=self.width//2,
                                       y=100,
                                       anchor_y="center",
                                       anchor_x="center",
                                       color=(255, 0, 0, 255))

        self.winlabel = pyglet.text.Label(f"{self.win}€",
                                       font_name=self.font,
                                       font_size=90,
                                       x=self.width // 2,
                                       y=220,
                                       anchor_y="center",
                                       anchor_x="center",
                                       color=(245, 194, 65, 255))

        # Caricamento Immagini - Sprites
        # Ruota
        self.wheel_img = pyglet.resource.image("gfx/ruota.png")
        self.wheel_img.anchor_x = self.wheel_img.width // 2
        self.wheel_img.anchor_y = self.wheel_img.height // 2
        self.wheel_sprite = pyglet.sprite.Sprite(img=self.wheel_img, x=640, y=360)

        # BG Generali
        self.bgmoney = pyglet.resource.image("gfx/money_space.png")
        self.bgmoney.anchor_x = self.bgmoney.width // 2
        self.bgmoney.anchor_y = self.bgmoney.height // 2
        self.bgmoney_sprite = pyglet.sprite.Sprite(img=self.bgmoney, x=140, y=650, z=0.5)

        self.bgbets = pyglet.resource.image("gfx/bets.png")
        self.bgbets.anchor_x = self.bgbets.width // 2
        self.bgbets.anchor_y = self.bgbets.height // 2
        self.bgbets_sprite = pyglet.sprite.Sprite(img=self.bgbets, x=1100, y=400, z=0.5)

        self.lastscenewin = pyglet.resource.animation("gfx/vincita.gif")
        self.lastscenewin_sprite = pyglet.sprite.Sprite(img=self.lastscenewin, x=0, y=0)
        self.lastscenewin_sprite.scale = 0.67

        self.perdita = pyglet.resource.animation("gfx/perdita.gif")
        self.perdita_sprite = pyglet.sprite.Sprite(img=self.perdita, x=0, y=0)
        self.perdita_sprite.scale = 0.67

        self.girare = pyglet.resource.animation("gfx/girare.gif")
        self.girare_sprite = pyglet.sprite.Sprite(img=self.girare, x=0, y=0)
        self.girare_sprite.scale = 0.67

        # Easter Eggs
        self.winimg = pyglet.resource.image("gfx/winimg.jpg")
        self.winimg.anchor_x = self.winimg.width // 2
        self.winimg.anchor_y = self.winimg.height // 2
        self.winimg_sprite = pyglet.sprite.Sprite(img=self.winimg, x=500, y=400)

        self.loseimg = pyglet.resource.image("gfx/loseimg.jpeg")
        self.loseimg.anchor_x = self.loseimg.width // 2
        self.loseimg.anchor_y = self.loseimg.height // 2
        self.loseimg_sprite = pyglet.sprite.Sprite(img=self.loseimg, x=500, y=400)

        # Bet
        self.bet1 = pyglet.resource.image("gfx/1.png")
        self.bet1.anchor_x = self.bet1.width // 2
        self.bet1.anchor_y = self.bet1.height // 2
        self.bet2 = pyglet.resource.image("gfx/2.png")
        self.bet2.anchor_x = self.bet2.width // 2
        self.bet2.anchor_y = self.bet2.height // 2
        self.bet5 = pyglet.resource.image("gfx/5.png")
        self.bet5.anchor_x = self.bet5.width // 2
        self.bet5.anchor_y = self.bet5.height // 2
        self.bet10 = pyglet.resource.image("gfx/10.png")
        self.bet10.anchor_x = self.bet10.width // 2
        self.bet10.anchor_y = self.bet10.height // 2
        self.betcoin_button = pyglet.resource.image("gfx/coin.png")
        self.betcoin_button.anchor_x = self.betcoin_button.width // 2
        self.betcoin_button.anchor_y = self.betcoin_button.height // 2
        self.betpach_button = pyglet.resource.image("gfx/pach.png")
        self.betpach_button.anchor_x = self.betpach_button.width // 2
        self.betpach_button.anchor_y = self.betpach_button.height // 2
        self.betcash_button = pyglet.resource.image("gfx/cash.png")
        self.betcash_button.anchor_x = self.betcash_button.width // 2
        self.betcash_button.anchor_y = self.betcash_button.height // 2
        self.betcrazy_button = pyglet.resource.image("gfx/crazy.png")
        self.betcrazy_button.anchor_x = self.betcrazy_button.width // 2
        self.betcrazy_button.anchor_y = self.betcrazy_button.height // 2
        self.bet_button = pyglet.resource.image("gfx/bet.png")
        self.bet_button.anchor_x = self.bet_button.width // 2
        self.bet_button.anchor_y = self.bet_button.height // 2

        self.bets = [pyglet.sprite.Sprite(img=self.bet1, x=self.width//2 - 475, y=300, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.bet2, x=self.width//2 - 475, y=200, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.bet5, x=self.width//2 - 275, y=300, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.bet10, x=self.width//2 - 275, y=200, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.bet_button, x=self.width//2, y=250, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.betcoin_button, x=self.width//2 + 275, y=300, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.betcash_button, x=self.width // 2 + 275, y=200, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.betpach_button, x=self.width//2 + 475, y=300, batch=self.batch_bet),
                    pyglet.sprite.Sprite(img=self.betcrazy_button, x=self.width//2 + 475, y=200, batch=self.batch_bet)
                    ]
        for e in self.bets:
            e.scale = 0.8

        # Caricamento Suoni
        self.theme = pyglet.resource.media("sounds/theme.mp3", streaming=False)
        self.click = pyglet.resource.media("sounds/clickbt.mp3", streaming=False)
        self.wins = pyglet.resource.media("sounds/winsound.mp3", streaming=False)
        self.loss = pyglet.resource.media("sounds/loss.mp3", streaming=False)
        self.spinningwheel = pyglet.resource.media("sounds/wheelspinning.mp3", streaming=False)
        self.suspance = pyglet.resource.media("sounds/suspance.mp3", streaming=False)
        self.playert = None
        self.playerm = pyglet.media.Player()
        self.players = pyglet.media.Player()
        self.playerm.volume = 0.7
        self.players.volume = 0.5



    def on_draw(self):
        self.clear()
        self.background_sprite.draw()
        if self.stato == 0:
            self.mainbg_sprite.draw()
        elif self.stato == 1:
            self.batch_bet.draw()
            self.bgmoney_sprite.draw()
            self.moneylabel.draw()
            self.batch_text.draw()
            if self.err:
                self.nobet.draw()
        elif self.stato == 2:
            self.girare_sprite.draw()
            self.wheel_sprite.draw()
            if self.finita_rotazione:
                time.sleep(1.1)
                self.winlabel.text = f"{self.win}€"
                if self.win > 0:
                    self.players.pause()
                    self.playerm.next_source()
                    self.playerm.queue(self.wins)
                    self.playerm.play()
                else:
                    self.players.pause()
                    self.playerm.next_source()
                    self.playerm.queue(self.loss)
                    self.playerm.play()
                self.money += self.win
                self.moneylabel.text = f"{self.money}€"
                self.stato = 3
        elif self.stato == 3:
            if self.win > 0:
                self.lastscenewin_sprite.draw()
                self.winlabel.draw()
            else:
                self.perdita_sprite.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.M:
            self.playert.volume = 0.0
        if symbol == key.N:
            self.playert.volume = 1.0
        if self.stato == 0:
            if symbol == key.ENTER:
                self.stato = 1
                self.bets[0].scale = 0.9
        elif self.stato == 1:
            if symbol == key.ENTER:
                if self.money >= 10:
                    if self.pulsante == 0:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.on1 += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabel1.text = f"Bet on 1: {self.on1}"
                    elif self.pulsante == 1:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.on2 += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabel2.text = f"Bet on 2: {self.on2}"
                    elif self.pulsante == 2:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.on5 += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabel5.text = f"Bet on 5: {self.on5}"
                    elif self.pulsante == 3:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.on10 += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabel10.text = f"Bet on 10: {self.on10}"
                    elif self.pulsante == 5:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.oncoin += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabelcoin.text = f"Bet on Coin Flip: {self.oncoin}"
                    elif self.pulsante == 6:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.oncash += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabelcash.text = f"Bet on Cash Hunt: {self.oncash}"
                    elif self.pulsante == 7:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.onpac += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabelpac.text = f"Bet on Pachinko: {self.onpac}"
                    elif self.pulsante == 8:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.money -= 10
                        self.oncrazy += 10
                        self.moneylabel.text = f"{self.money}€"
                        self.betlabelcrazy.text = f"Bet on Crazy Time: {self.oncrazy}"
                if self.pulsante == 4:
                    if self.on1 == 0 and self.on2 == 0 and self.on5 == 0 and self.on10 == 0 and self.oncoin == 0 and self.oncash == 0 and self.onpac == 0 and self.oncrazy == 0:
                        self.err = True
                    else:
                        self.playerm.pause()
                        self.playerm.next_source()
                        self.playerm.queue(self.click)
                        self.playerm.play()
                        self.stato = 2
                        for i in range(len(self.bets)):
                            self.bets[i].scale = 0.8
            elif symbol == key.RIGHT:
                if self.pulsante + 2 == 4 or self.pulsante + 2 == 5:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante = 4
                elif self.pulsante == 4:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante += 1
                elif self.pulsante + 2 >= 9:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante = 0
                else:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante += 2

                self.bets[self.pulsante].scale = 0.9
            elif symbol == key.LEFT:
                if self.pulsante - 2 < 0:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante = 7
                elif self.pulsante - 2 == 3 or self.pulsante - 2 == 4:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante = 4
                else:
                    self.bets[self.pulsante].scale = 0.8
                    self.pulsante -= 2

                self.bets[self.pulsante].scale = 0.9
            elif symbol == key.UP:
                if self.pulsante != 4:
                    if self.pulsante - 1 == -1 or self.pulsante - 1 == 1 or self.pulsante - 1 == 4 or self.pulsante - 1 == 6:
                        self.bets[self.pulsante].scale = 0.8
                        self.pulsante += 1
                    else:
                        self.bets[self.pulsante].scale = 0.8
                        self.pulsante -= 1

                self.bets[self.pulsante].scale = 0.9
            elif symbol == key.DOWN:
                if self.pulsante != 4:
                    if self.pulsante + 1 == 2 or self.pulsante + 1 == 4 or self.pulsante + 1 == 7 or self.pulsante + 1 == 9:
                        self.bets[self.pulsante].scale = 0.8
                        self.pulsante -= 1
                    else:
                        self.bets[self.pulsante].scale = 0.8
                        self.pulsante += 1

                self.bets[self.pulsante].scale = 0.9

        elif self.stato == 2:
            if symbol == key.SPACE:
                if not self.spinning:
                    n = estrai_numero()
                    if n == 1:
                        self.velocita_rotazione = random.choice(self.ones)
                        self.win = self.on1
                    elif n == 2:
                        self.velocita_rotazione = random.choice(self.twos)
                        self.win = self.on2 * 2
                    elif n == 5:
                        self.velocita_rotazione = random.choice(self.fives)
                        self.win = self.on5 * 5
                    elif n == 10:
                        self.velocita_rotazione = random.choice(self.tens)
                        self.win = self.on10 * 10
                    elif n == -1:
                        self.velocita_rotazione = random.choice(self.coins)
                        self.win = self.oncoin * 20
                    elif n == -2:
                        self.velocita_rotazione = random.choice(self.pacs)
                        self.win = self.onpac * 40
                    elif n == -3:
                        self.velocita_rotazione = random.choice(self.cashs)
                        self.win = self.oncash * 40
                    else:
                        self.velocita_rotazione = random.choice(self.crazys)
                        self.win = self.oncrazy * 100
                    pyglet.clock.schedule_interval(self.update, 1/60.0)
                    self.spinning = True
                    self.playerm.pause()
                    self.playerm.next_source()
                    self.playerm.queue(self.spinningwheel)
                    self.playerm.play()
                    self.playert.volume = 0
                    self.players.next_source()
                    self.players.queue(self.suspance)
                    self.players.play()
        elif self.stato == 3:
            if symbol == key.ENTER:
                self.stato = 1
                self.resetta_variabili()


    def resetta_variabili(self):
        self.pulsante = 0
        self.on1 = 0
        self.on2 = 0
        self.on5 = 0
        self.on10 = 0
        self.oncoin = 0
        self.onpac = 0
        self.oncash = 0
        self.oncrazy = 0
        self.decelerazione = 20
        self.velocita_rotazione = 0
        self.spinning = False
        self.err = False
        self.finita_rotazione = False
        self.win = 0
        self.winlabel.text = f"{self.win}€"
        self.betlabel1.text = f"Bet on 1: {self.on1}"
        self.betlabel2.text = f"Bet on 2: {self.on2}"
        self.betlabel5.text = f"Bet on 5: {self.on5}"
        self.betlabel10.text = f"Bet on 10: {self.on10}"
        self.betlabelcoin.text = f"Bet on Coin Flip: {self.oncoin}"
        self.betlabelcash.text = f"Bet on Cash Hunt: {self.oncash}"
        self.betlabelpac.text = f"Bet on Pachinko: {self.onpac}"
        self.betlabelcrazy.text = f"Bet on CrazyTime: {self.oncrazy}"
        self.wheel_sprite.rotation = 0

    def start_music(self):
        self.playert = self.theme.play()
        self.playert.loop = True

    def update(self, dt):
        if self.velocita_rotazione > 0:
            self.velocita_rotazione -= self.decelerazione * dt
            if self.velocita_rotazione < 0:
                self.velocita_rotazione = 0
                self.finita_rotazione = True
                pyglet.clock.unschedule(self.update)

        self.wheel_sprite.rotation += self.velocita_rotazione * dt

def estrai_numero():
    n = random.randint(0, 49)
    if n < 20:
        return 1
    elif n < 33:
        return 2
    elif n < 40:
        return 5
    elif n < 44:
        return 10
    elif n < 48:
        return -1
    elif n < 50:
        return -2
    elif n < 52:
        return -3
    elif n < 53:
        return -4

if __name__ == '__main__':
    window = GameWindow()
    window.start_music()
    pyglet.app.run()