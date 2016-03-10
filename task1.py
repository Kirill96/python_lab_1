"""The first task: text statistics"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


def  item1(input_text):
    """How many times each word is repeated in this text"""
    print "\nItem1: "

    dct = {}
    _list = input_text.replace(",", " ").replace(".", " ")\
                      .replace("!", " ").replace("?", " ").split()

    for elem in _list:
        if elem in dct:
            dct[elem] += 1
        else:
            dct[elem] = 1

    sorted_dct = [(k, v) for v, k in sorted([(v, k) \
                         for k, v in dct.items()])
                 ]

    return sorted_dct


def item2(input_text):
    """Average count of words in sentences"""
    print "\nItem2: "

    dct_sent = {}
    count_of_words = 0

    for elem in input_text.replace(",", ".").replace("!", ".")\
                          .replace("?", ".").split("."):
        elem = len(elem.split())
        count_of_words += elem

    for element in input_text.replace(",", ".").replace("!", ".")\
                             .replace("?", ".").split("."):
        if element in dct_sent:
            dct_sent[element] += 1
        else:
            dct_sent[element] = 1

    count_of_sent = len(dct_sent) - 1
    average_count = count_of_words/count_of_sent

    return average_count


def  item3(input_text):
    """Median count of words"""
    print "\nItem3: "

    dct = []

    for elem in input_text.replace(",", ".").replace("!", ".")\
                          .replace("?", ".").split("."):
        elem = len(elem.split())
        dct.append(elem)

    sort_dct = sorted(dct)
    median_count = len(sort_dct) / 2

    return sort_dct[median_count]


def item4(input_text):
    """top-K the most frequently recurring letters N-gram"""
    count_n_gram = int(raw_input("\nInput N: "))
    count_top_gram = int(raw_input("Input K: "))
    print "\nItem4: "

    sort_list = sorted(input_text.replace(".", " ").replace(",", " ")\
                            .replace("!", " ").replace("?", " ").split())
    dct = {}
    for elem in sort_list:
        for i in range(len(elem)):
            gram = elem[i:i+count_n_gram]
            if len(gram) >= count_n_gram:
                if gram in dct:
                    dct[gram] += 1
                else:
                    dct[gram] = 1

    sort_dct = sorted(dct.values(), reverse=True)
    gram_keys = dct.keys()

    if int(count_top_gram) > len(sort_dct):
        count_top_gram = len(sort_dct)

    dct_gram = {}
    for key in gram_keys:
        for top_gr in range(count_top_gram):
            if dct[key] == sort_dct[top_gr]:
                dct_gram[key] = sort_dct[top_gr]

    sorted_gram_dict = [(count_top_gram, v) for v, count_top_gram in sorted(\
                       [(v, count_top_gram)\
                        for count_top_gram, v in dct_gram.items()\
                       ], reverse=True)
                       ]

    return sorted_gram_dict
