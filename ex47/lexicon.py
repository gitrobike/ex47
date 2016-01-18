# -*- coding: utf-8 -*-

def scan(stuff):
    sentence = [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east'),
        ('verb', 'go'),
        ('stop', 'the'),
        ('noun', 'bear'),
        ('number', '1234'),
        ('error', 'ASDFADFASDF')
    ]

    sentence_out = []
    words = stuff.split()

    for word in words:
        for sentence_word in sentence:
            if sentence_word[1] == word:
                sentence_out.append(sentence_word)

    print(sentence_out)
    return sentence_out

'''#需求理解错误，需更正

def scan(stuff= raw_input('> ')):

    first_word = ('direction', 'north')
    second_word = ('verb', 'go')
    third_word = ('stop', 'the')
    fourth_word = ('noun', 'bear')
    fifth_word = ('number', '1234')
    sixth_word = ('error', 'ASDFADFASDF')
    sentence = [first_word, second_word, third_word, fourth_word, fifth_word, sixth_word]
    # sentence = {'direction': 'north', 'verb': 'go'}

    words = stuff.split()
    print('查看所有获得的词汇:'),
    print(words)
    print('\n')

    sentence_out = []#用于输出最终结果的列表
    word_sentence_0 = ''#用于储存word_sentence[1]匹配后的word_sentence[0]值

    for word_sentence in sentence:
        print('--' * 10),
        print('当前元组：'),
        print(word_sentence),
        print('--' * 10)

        for word in words:
            if word_sentence[1] == word:
                print('元组的第二个词汇和获得的词汇匹配了:'),
                print(word),
                print('\n')

                word_sentence_0 = word_sentence[0]
                print(word_sentence_0),
                print('\n')
                break
                # word_sentence_1 = word_sentence[1]
                # print(word_sentence_1)
            else:
                print('sorry!')
#
#
#     if word_sentence_0 != '':
#         for word in words:
#             print('===' * 10),
#             print('当前词汇:'),
#             print(word),
#             print('===' * 10)
#
#             sentence_out.append((word_sentence_0, word))
#             print("+++")
#
#
#     print(sentence_out)
#     return sentence_out
'''

scan("south east north go")