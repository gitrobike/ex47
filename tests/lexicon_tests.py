# -*- coding: utf-8 -*-

from nose.tools import *
from ex47 import lexicon
# from ex47 import game
#
# game.ss("sss")

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    #需要返回一个包含元组的列表
    result = lexicon.scan("north south east ASDFADFASDF")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east'),
                          ('error', 'ASDFADFASDF')
                          ])

test_directions()
