# -*- coding: utf-8 -*-
import lexicon

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

    def return_sentence(self):
        return self.subject, self.verb, self.object

def peek(word_list):
    if word_list:
        word = word_list[0]
        # print(word[0])
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)#截取word_list，位置为[0]

        if word[0] == expecting:
            # print(word)
            return word
        else:
            # print('what?', expecting)
            return None
    else:
        print(word_list)
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        '''注意这里是一个while循环，只有匹配了word_type才继续执行。
        例如word_type == 'stop'时，会执行循环内容，使用match()函数吧'stop'过滤掉，
        直到遇到一个word不是‘stop’。
        '''
        match(word_list, word_type)

# word_list = lexicon.sentence
# print(word_list)
# skip(word_list, 'direction')
# print(word_list)

def parse_verb(word_list):#返回谓语
    skip(word_list, 'stop')#过滤‘stop’，

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

# parse_verb(lexicon.sentence)

def parse_object(word_list):#返回宾语，一个名词或者方位名词。
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError('Expected a noun or direction next.')

def parse_subject(word_list, subj):#返回了主谓宾
    verb = parse_verb(word_list)#返回谓语
    obj = parse_object(word_list)#返回宾语

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':#名词
        subj = match(word_list, 'noun')
        #如果句首是一个名词，那么这个词一定是主语。
        # re = parse_subject(word_list, subj)
        # print re.return_sentence()
        return parse_subject(word_list, subj)
    elif start == 'verb': #动词
        #如果局势是一个动词，那么主语默认为“player”
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject（主语）, object（宾语）, or verb（谓语） not: %s" % start)

# word_list = lexicon.scan('the bear is go to the east')
# print(word_list)
# print(parse_sentence(word_list))