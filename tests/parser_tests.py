# -*- coding: utf-8 -*-

from nose.tools import *

from ex48 import parser, lexicon

def test_peek():
    assert_equal(parser.peek([('stop', '***Yes stop**8'), ('hello', 'Just hello!')]), 'stop')

# test_peek()

def test_match():
    print(lexicon.sentence)
    assert_equal(parser.match(lexicon.sentence, 'direction'), ('direction', 'north'))
    print(lexicon.sentence)
    assert_equal(parser.match(lexicon.sentence, 'direction'), ('direction', 'south'))
    print(lexicon.sentence)

# test_match()

def test_skip():
    word_list = lexicon.scan('the bear is go to the east')
    # word_list.extend(lexicon.sentence)#拼接字符串
    # print(word_list)
    parser.skip(word_list, 'stop')
    assert_equal(parser.peek(word_list), 'noun')
    # print(word_list)

# test_skip()

def test_parse_sentence():
    word_list = lexicon.scan('the bear is go to the east')

    def re_sentence(parser_sentence):
        subj = parser_sentence.subject
        verb = parser_sentence.verb
        obj = parser_sentence.object
        return subj, verb, obj

    result = re_sentence(parser.parse_sentence(word_list))
    print(result)

    assert_equal(result, ('bear', 'go', 'east'))
    assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'dog')])
    # print(parser.parse_verb([('noun', 'dog')]))

# test_parse_sentence()


