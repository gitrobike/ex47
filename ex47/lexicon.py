# -*- coding: utf-8 -*-

# sentence = [('direction', 'north'), ('verb', 'go')]

# = raw_input('> ')
def scan(stuff):

    first_word = ('direction', 'north')
    second_word = ('verb', 'go')
    third_word = ('stop', 'the')
    fourth_word = ('noun', 'bear')
    fifth_word = ('number', '1234')
    sixth_word = ('error', 'ASDFADFASDF')
    sentence = [first_word, second_word, third_word, fourth_word, fifth_word, sixth_word]

    words = stuff.split()
    print('查看所有获得的词汇:'),
    print(words)
    print('\n')

    sentence_out = []
    word_sentence_0 = ''

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


    if word_sentence_0 != '':
        for word in words:
            print('===' * 10),
            print('当前词汇:'),
            print(word),
            print('===' * 10)

            sentence_out.append((word_sentence_0, word))
            print("+++")


    print(sentence_out)
    return sentence_out


# def scan_much(stuff):
#     sentence = [('direction', 'north'), ('verb', 'go')]
#     words = stuff.split()
#     # print(words)
#     for word in words:
#         print('===' * 10)
#         print(word)
#         for s_word in sentence:
#             print('--' * 10)
#             # print(s_word)
#             # print(s_word[1])
#             if s_word[1] == word:
#                 print("GOOD!")
#                 print(s_word)
#             else:
#                 print("WRONG!")
#                 print(s_word[1])
#                 print(word)


scan("south east north go")