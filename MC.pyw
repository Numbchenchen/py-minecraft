"""
作者:Numbeen
作者邮箱:Numbchenchen@outlook.com  欢迎联系我
教程:编程侯老师
"""
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import time

app = Ursina()

grass_t = load_texture("assets/grass_block.png")

stone_t = load_texture("assets/stone_block.png")

brick_t = load_texture("assets/brick_block.png")

dirt_t = load_texture("assets/dirt_block.png")

cobblestone_t = load_texture("assets/cobblestone_block.png")

plank_t = load_texture("assets/plank_block.png")

log_t = load_texture("assets/log_block.png")

gold_t = load_texture("assets/gold_block.png")

bedrock_t = load_texture("assets/bedrock_block.png")

ancient_debris_t = load_texture("assets/ancient_debris_block.png") 

sky_texture=load_texture("assets/skybox.png")

arm_texture=load_texture("assets/arm_texture.png")

mouse_t=load_texture("assets/mouse.png")

punch_sound = Audio("assets/punch_sound.wav",loop=False,autoplay=False)
window.fps_counter.enabled=False
window.exit_button.visible = False
block_p = 1

scene.fog_color=color.white
scene.fog_density=0.028

def input(key):
    if key == "escape": quit()

def update():
    global block_p
    if held_keys['1']:block_p = 1
    if held_keys['2']:block_p = 2
    if held_keys['3']:block_p = 3
    if held_keys['4']:block_p = 4
    if held_keys['5']:block_p = 5
    if held_keys['6']:block_p = 6
    if held_keys['7']:block_p = 7
    if held_keys['8']:block_p = 8
    if held_keys['9']:block_p = 9

    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

class Block(Button):
    def __init__(self,texture,position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block",
            origin_y=0.5,
            texture = texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=0.5
         )
        
    def input(self,key):
        if self.hovered:
            if key == "right mouse down":
                punch_sound.play()
                if block_p ==1:block =Block(position= self.position+mouse.normal,texture=grass_t)
                if block_p ==2:block =Block(position= self.position+mouse.normal,texture=stone_t)
                if block_p ==3:block =Block(position= self.position+mouse.normal,texture=brick_t)
                if block_p ==4:block =Block(position= self.position+mouse.normal,texture=dirt_t)
                if block_p ==5:block =Block(position= self.position+mouse.normal,texture=cobblestone_t)
                if block_p ==6:block =Block(position= self.position+mouse.normal,texture=plank_t)
                if block_p ==7:block =Block(position= self.position+mouse.normal,texture=log_t)
                if block_p ==8:block =Block(position= self.position+mouse.normal,texture=gold_t)
                if block_p ==9:block =Block(position= self.position+mouse.normal,texture=ancient_debris_t)
            if key == "left mouse down":
                punch_sound.play()
                destroy(self)
                
class Bedrock(Button):
    def __init__(self,texture,position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block",
            origin_y=0.5,
            texture = texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=0.5
         )
        
    def input(self,key):
        if self.hovered:
            if key == "right mouse down":
                punch_sound.play()
                if block_p ==1:block =Block(position= self.position+mouse.normal,texture=grass_t)
                if block_p ==2:block =Block(position= self.position+mouse.normal,texture=stone_t)
                if block_p ==3:block =Block(position= self.position+mouse.normal,texture=brick_t)
                if block_p ==4:block =Block(position= self.position+mouse.normal,texture=dirt_t)
                if block_p ==5:block =Block(position= self.position+mouse.normal,texture=cobblestone_t)
                if block_p ==6:block =Block(position= self.position+mouse.normal,texture=plank_t)
                if block_p ==7:block =Block(position= self.position+mouse.normal,texture=log_t)
                if block_p ==8:block =Block(position= self.position+mouse.normal,texture=gold_t)
                if block_p ==9:block =Block(position= self.position+mouse.normal,texture=ancient_debris_t)
            
class sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = sky_texture,
            scale=150,
            double_sided = True
        )

class hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "assets/arm",
            texture = arm_texture,
            scale=0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.8,-0.6)
        )
    def active(self):
        self.position = Vec2(0.7,-0.6)
    def passive(self):
        self.position = Vec2(0.8,-0.6)

class mouse_(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model="cube",
            texture = mouse_t,
            scale=0.07,
        )
        
noise=PerlinNoise(octaves=3,seed=int(time.perf_counter()))
scale=24
dx=12#大小这里调

for z in range(dx):
    for x in range(dx):
        yy=int(noise([x/scale,z/scale])*8)
        block = Block(grass_t,position=(x,yy,z))
        block_d=Block(dirt_t,position=(x,yy-1,z))
        block_d=Block(dirt_t,position=(x,yy-2,z))
        for sy in range(yy-2+7):
             block_s=Block(stone_t,position=(x,yy-3-sy,z))
             
for bz in range(dx):
    for bx in range(dx):
            bedrock = Bedrock(bedrock_t,position=(bx,-8,bz))

player= FirstPersonController()
sky=sky()
player.cursor.enabled=False#隐藏鼠标
mouse_=mouse_()
hand=hand()
editor_camera=EditorCamera(enabled=False)

app.run()
