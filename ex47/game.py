# -*- coding: utf-8 -*-

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        #传入房间名，进入房间，获取value值。
        return self.paths.get(direction)
        # return self.paths.get(direction, None)#默认值是None，应该可以不写

    def add_paths(self, paths):
        #在paths字典中增加一组键值对
        self.paths.update(paths)
#
# def ss(s):
#     print(s)