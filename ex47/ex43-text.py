# -*- coding: utf-8 -*-

from sys import exit
from random import randint

"""重写 ex43.py ，去除Map类"""

class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        print("此'场景'尚未配置，通过子类继承它，实现enter()方法。")
        exit(1)#有错误的退出


class Death(Scene):
    """死亡场景"""
    quips = [
        "You died. You kinds suck at this.",
        "Your mom would bu proud...if the were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])#为毛用Death.,不用self. ？得有个老师问问。
        #randint获取0到序列长度范围的随机数
        exit(1)

class CentralCorridor(Scene):
    """中央走廊"""
    def enter(self):

        print("The Gothons of Planet ...")
        print("escape pod.")
        print("\n")
        print("you...")

        action = raw_input("输入shoot，dodge或tell a joke：> ")

        if action == "shoot!":
            print("Quick on the draw you yank out ...")
            print("you are dead. Then he eats you.")
            return 'death'

        elif action == "dodge!":
            print("Like a world class boxer you dodge, ....")
            print("... and eats you.")
            return 'death'

        elif action == "tell a joke":
            print("Lucky for you the made you learn Gothon instults in the acadeny. ...")
            print("putting him down , then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'#返回Key值 激光武库

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    """激光武器库"""
    def enter(self):
        print("get the bomb. The code is 3 digits.")

        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        #搞一个随机的三位正整数，我靠，拿到炸弹的概率太尼玛低了吧？坑爹呢？

        guess = raw_input("猜一个三位整数，猜11次，[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = raw_input(("猜一个三位数，猜11次，[keypad]>"))

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out. ...")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'#返回Key值，主控舱（舰桥）
        else:
            print("The lock buzzs ...")
            print("ship from their ship and you die.")
            return 'death'


class TheBridge(Scene):
    """主控舱"""
    def enter(self):
        print("You burst onto the Bridge ...")

        action = raw_input("输入throw the bomb或slowly place the bomb> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons...")
            return 'death'

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm ...")
            print("Now that the bomb is lpaced you runt o the escape pod to "
                  "get off this tin can.")
            return 'escape_pod'#救生舱（逃逸舱）
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):
    """救生舱"""
    def enter(self):
        print("You rush through the ship ...")
        print("There's 5 pods, which one do you take?")

        good_pod = randint(1, 5)
        guess = raw_input("猜数：1~5[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button.") % guess
            print("The pod escapes out into the void of space, ...")
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button.") % guess
            print("The pod easily slides out into space heading to "
                  "the planet below. ..."
                  " You won!")
            return 'finished'

# class Map(object):
#
#     scenes = {
#         'central_corridor': CentralCorridor(),
#         'laser_weapon_armory': LaserWeaponArmory(),
#         'the_bridge': TheBridge(),
#         'escape_pod': EscapePod(),
#         'death': Death()
#     }
#
#     # def __init__(self, start_scene):
#     #     #获得scene（场景）名,得到self.start_scene
#     #     self.start_scene = start_scene
#
#     def next_scene(self, scene_name):
#         #Map类核心功能，传入key值，返回value值,value值是一个Scene子类
#         return self.scenes.get(scene_name)
#
#     # def opening_scene(self):
#     #     #默认传入key值为self.start_scene，返回value值
#     #     return self.next_scene(self.start_scene)


class Engine(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, scene_name):
        #传入Map值
        # self.scene_map = scene_map
        self.scene_name = scene_name

    def play(self):
        # current_scene = self.scene_map.opening_scene()
        current_scene = self.scenes.get(self.scene_name)
        #调用Map()实例的opening_scene()方法，获得具体的Scene子类实例，用于进入游戏开始场景

        while True:
            #while循环保证可以在各个Scene场景之间切换
            print("\n--------")

            next_scene_name = current_scene.enter()
            #调用一个Scene子类实例的enter()方法，获取下一步的Key值

            # current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene = self.scenes.get(next_scene_name)
            #继续调用Map实例的next_scene()方法，获取下一步的Value值，也就是下一个Scene子类实例。

# a_map = Map('central_corridor') #实例化一个Map
# a_map = Map()
# a_game = Engine(a_map) #引用Map，实例化一个Engine（引擎）
a_game = Engine('central_corridor')
a_game.play() #调用Engine的play方法