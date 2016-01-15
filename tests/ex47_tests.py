# -*- coding: utf-8 -*-

from nose.tools import *
from ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab.
                There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")  # 断言，判断是否相等，不等则抛出异常
    assert_equal(gold.paths, {})

    # print(gold.name)
    # print(gold.go(gold.name))
    # print(gold.paths)


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room int south")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
    # print(center.go('north'))
    # print(north)
    # print(north.name)
    # print(north.paths)
    # print("-" * 30)
    # print(center)
    # print(center.name)
    # print(center.paths)


def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, yo can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

    print("-" * 30)
    print('start paths 里面有：%r' % start.paths.keys())
    print('west paths 里面有：%r' % west.paths.keys())
    print('down paths 里面有：%r' % down.paths.keys())

    print("-" * 30)
    east = west.paths.get('east')
    # 其实没有实际声明过这个Room()类的实例east,east就是start。
    print(east)
    print(start)

    print("-" * 30)
    print('east paths 的Key值：%r' % west.paths.get('east').name)
    print('east paths 里面有：%r' % west.paths.get('east').paths.keys())

    print("-" * 30)
    def values_west():
        # 创建一个生成器
        for value in west.paths.keys():
            yield west.paths.get(value).name
            yield west.paths.get(value).paths.keys()

    for i in values_west():
        # 遍历这个生成器
        print i

    print("-" * 30)
    def values_start():
        # 创建一个生成器
        for value in start.paths.keys():
            yield start.paths.get(value).name
            yield start.paths.get(value).paths.keys()

    for i in values_start():
        # 遍历这个生成器
        print i


test_room()
test_room_paths()
test_map()
